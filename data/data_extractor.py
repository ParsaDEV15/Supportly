from datasets import load_dataset

ds = load_dataset("MakTek/Customer_support_faqs_dataset", split="train")
df = ds.to_pandas()

df.to_csv("raw_data/FAQs.csv", index=False)