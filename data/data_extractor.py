from datasets import load_dataset
import os

FILE_PATH = "MakTek/Customer_support_faqs_dataset"

ds = load_dataset(FILE_PATH, split="train")
df = ds.to_pandas()

SAVE_PATH = "raw_data/"
DATA_NAME = "FAQs.csv"

os.makedirs(SAVE_PATH, exist_ok=True)

df.to_csv(os.path.join(SAVE_PATH, DATA_NAME), index=False)