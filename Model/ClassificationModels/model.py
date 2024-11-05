#!/usr/bin/python3

import pandas as pd
import torch
import transformers
from transformers import BertTokenizer, BertModel, AutoTokenizer, AutoModelForSequenceClassification

# MODEL PATH
MODEL_PATH = "../TrainedModels/"

# BERT MODEL
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize_text_data(text):
    '''Tokenizes all text data in a specified column of a DataFrame

    - df: pd.DataFrame
    - column_name: str
    Return DataFrame with tokenized text
    '''
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Decode the output variables
label_encoders = {}
for column in ['Category', 'Description', 'Section in Act', 'Key Points']:
    le = LabelEncoder()
    kenya_train.loc[:, column] = le.fit_transform(kenya_train[column])
    label_encoders[column] = le