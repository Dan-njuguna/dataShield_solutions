#!/usr/bin/env python

import os
import logging
import warnings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Suppress warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

# Path to the PDF file
file_path = os.path.join(os.path.expanduser("~"), "Documents/Hackathons/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf")

# Step 1: Load the PDF document
try:
    logger.info("Loading the PDF document...")
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    logger.info(f"Loaded {len(docs)} documents from PDF.")
except Exception as e:
    logger.error(f"Error loading document: {e}")
    exit(1)

# Print a sample of the content
logger.info(f"Sample content: {docs[0].page_content[:200]}")
logger.info(f"Metadata: {docs[0].metadata}")

# Step 2: Split the document into chunks
logger.info("Splitting the document into text chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
logger.info(f"Split into {len(splits)} text chunks.")

# Step 3: Initialize the embedding model using SentenceTransformer
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
logger.info(f"Initializing embedding model: {embedding_model_name}...")
embedding_model = SentenceTransformer(embedding_model_name)

# Define a function to embed text
def embed_texts(texts):
    return embedding_model.encode(texts, show_progress_bar=True)

# Step 4: Create or load the FAISS vector store
class EmbeddingWrapper:
    def __init__(self, embed_func):
        self.embed_func = embed_func

    def embed_documents(self, texts):
        return self.embed_func(texts)

embedding_wrapper = EmbeddingWrapper(embed_texts)
embedding_file_path = os.path.join(os.path.expanduser(".."), "../embeddings.faiss")

if os.path.exists(embedding_file_path):
    try:
        logger.info("Loading existing FAISS vector store...")
        vectorstore = FAISS.load_local(
            embedding_file_path,
            embedding_wrapper,
            allow_dangerous_deserialization=True
        )
        logger.info("Loaded FAISS vector store successfully.")
    except Exception as e:
        logger.warning(f"Error loading FAISS index: {e}. Rebuilding the vector store...")
        vectorstore = FAISS.from_texts(
            texts=[doc.page_content for doc in splits],
            embedding=embedding_wrapper
        )
        vectorstore.save_local(embedding_file_path)
else:
    logger.info("Creating a new FAISS vector store...")
    vectorstore = FAISS.from_texts(
        texts=[doc.page_content for doc in splits],
        embedding=embedding_wrapper
    )
    vectorstore.save_local(embedding_file_path)

# Step 5: Initialize a local HuggingFace pipeline for LLM
llm_model_name = "tiiuae/falcon-7b-instruct"
logger.info(f"Initializing HuggingFace LLM pipeline with model: {llm_model_name}...")
llm_pipeline = pipeline("text-generation", model=llm_model_name, device=-1, max_length=512)
llm = HuggingFacePipeline(pipeline=llm_pipeline)

# Step 6: Set up the retriever for querying
retriever = vectorstore.as_retriever()

# Step 7: Example query
query = "What are the key points in the data protection regulations?"
logger.info(f"Processing query: {query}")

try:
    retrieved_docs = retriever.get_relevant_documents(query)
    context = " ".join([doc.page_content[:1000] for doc in retrieved_docs])  # Truncate context
    response = llm(context)
    logger.info(f"Generated response: {response}")
except Exception as e:
    logger.error(f"Error during querying: {e}")

# Step 8: Classify information to compliance and non-compliance
def classify_compliance(text):
    compliance_keywords = ["compliance", "adherence", "conformity"]
    non_compliance_keywords = ["violation", "breach", "non-compliance"]
    
    if any(keyword in text.lower() for keyword in compliance_keywords):
        return "Compliance"
    elif any(keyword in text.lower() for keyword in non_compliance_keywords):
        return "Non-Compliance"
    else:
        return "Unknown"

logger.info("Classifying retrieved documents...")
for doc in retrieved_docs:
    classification = classify_compliance(doc.page_content)
    logger.info(f"Document classification: {classification}")

# Step 9: Extract violation details
def extract_violation_details(text):
    section_pattern = r"Section\s+(\d+)"
    subsection_pattern = r"Subsection\s+([A-Za-z])"
    fine_pattern = r"Fine of \$(\d+)"
    
    section = re.search(section_pattern, text)
    subsection = re.search(subsection_pattern, text)
    fine = re.search(fine_pattern, text)
    
    return {
        "section": section.group(1) if section else "Unknown",
        "subsection": subsection.group(1) if subsection else "Unknown",
        "verdict": f"Fine of ${fine.group(1)}" if fine else "Unknown"
    }

logger.info("Extracting violation details from retrieved documents...")
for doc in retrieved_docs:
    details = extract_violation_details(doc.page_content)
    logger.info(f"Violation details: {details}")
