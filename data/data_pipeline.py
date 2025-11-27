from datasets import load_dataset
import pandas as pd
import os

HUGGINGFACE_FILE_PATH = "MakTek/Customer_support_faqs_dataset"
RAW_SAVE_PATH = "raw_data/"
CLEANED_SAVE_PATH = "cleaned_data/"
DATA_NAME = "FAQs.csv"

os.makedirs(RAW_SAVE_PATH, exist_ok=True)
os.makedirs(CLEANED_SAVE_PATH, exist_ok=True)

ds = load_dataset(HUGGINGFACE_FILE_PATH, split="train")
df = ds.to_pandas()

cleaned_df = df.dropna()
cleaned_df = cleaned_df.drop_duplicates()

df.to_csv(os.path.join(RAW_SAVE_PATH, DATA_NAME), index=False)
cleaned_df.to_csv(os.path.join(CLEANED_SAVE_PATH, DATA_NAME), index=False)

print(f"Raw and cleaned datasets saved to {RAW_SAVE_PATH} and {CLEANED_SAVE_PATH}")