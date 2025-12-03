from mongo_setup import MongoSetup
from config.settings import PRODUCT_COLLECTION
import json

mongo_setup = MongoSetup()

products = json.load(open('products.json', 'r', encoding='utf-8'))

mongo_setup.insert_many_documents(
    collection_name=PRODUCT_COLLECTION,
    datas=products
)

docs = mongo_setup.find_all_docs(PRODUCT_COLLECTION, query={})

for doc in docs:
    print(doc)