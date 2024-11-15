#!/usr/bin/env python

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

# Path to the PDF file
file_path = os.path.join(os.path.expanduser("~"), "Documents/Hackathons/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf")

# Step 1: Load the PDF document
try:
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    print(f"Loaded {len(docs)} documents from PDF.")

except Exception as e:
    print(f"Error loading document: {e}")
    exit(1)

# Print a sample of the content
print("Sample content:", docs[0].page_content[:200])
print("Metadata:", docs[0].metadata)

# Step 2: Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print(f"Split into {len(splits)} text chunks.")

# Step 3: Initialize the embedding model using SentenceTransformer
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_model = SentenceTransformer(embedding_model_name)

# Define a function to embed text
def embed_texts(texts):
    return embedding_model.encode(texts, show_progress_bar=True)

# Step 4: Create an in-memory vector store using the embeddings
class EmbeddingWrapper:
    def __init__(self, embed_func):
        self.embed_func = embed_func

    def embed_documents(self, texts):
        return self.embed_func(texts)

embedding_wrapper = EmbeddingWrapper(embed_texts)

# Save embeddings to disk
embedding_file_path = os.path.join(os.path.expanduser("~"), "Documents/Hackathons/embeddings.faiss")
if os.path.exists(embedding_file_path):
    vectorstore = FAISS.load_local(embedding_file_path, embedding_wrapper)
else:
    vectorstore = FAISS.from_texts(
        texts=[doc.page_content for doc in splits],
        embedding=embedding_wrapper
    )
    vectorstore.save_local(embedding_file_path)

# Step 5: Initialize a local HuggingFace pipeline for LLM
llm_model_name = "tiiuae/falcon-7b-instruct"  # You can use any local model you have
llm_pipeline = pipeline("text-generation", model=llm_model_name, device=-1, max_length=512)
llm = HuggingFacePipeline(pipeline=llm_pipeline)

# Step 6: Set up the retriever for querying
retriever = vectorstore.as_retriever()

# Step 7: Example query
query = "What are the key points in the data protection regulations?"
print(f"Query: {query}")

# Retrieve relevant documents and generate a response
try:
    retrieved_docs = retriever.get_relevant_documents(query)
    context = " ".join([doc.page_content for doc in retrieved_docs])
    response = llm(context)
    print(f"Response: {response}")
except Exception as e:
    print(f"Error during querying: {e}")

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

# Example classification
for doc in retrieved_docs:
    classification = classify_compliance(doc.page_content)
    print(f"Document classification: {classification}")

# Step 9: Provide more information about the data section violations, subsection, and probable verdict
def extract_violation_details(text):
    # This is a placeholder function. You need to implement the logic to extract details.
    # For example, you can use regex or NLP techniques to extract sections, subsections, and verdicts.
    return {
        "section": "Section 1",
        "subsection": "Subsection A",
        "verdict": "Fine of $1000"
    }

# Example extraction
for doc in retrieved_docs:
    details = extract_violation_details(doc.page_content)
    print(f"Violation details: {details}")
