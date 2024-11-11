#!/usr/bin/python3

import pandas as pd
import torch
import transformers
from transformers import BertTokenizer, BertModel, AutoTokenizer, AutoModelForSequenceClassification


# DATASET PATH
DATASET_PATH = "../Datasets/"

gdpr_path = DATASET_PATH + "gdpr4.csv"
gdpr = pd.read_csv(gdpr_path)

# MODEL PATH
MODEL_PATH = "../TrainedModels/"

# BERT MODEL
