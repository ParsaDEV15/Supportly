from pymongo import MongoClient
from config.settings import MONGODB_URI, DB_NAME


class MongoSetup:
    def __init__(self):
        client = MongoClient(MONGODB_URI)
        self.db = client[DB_NAME]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def insert_one_document(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def insert_many_documents(self, collection_name, datas):
        collection = self.db[collection_name]
        collection.insert_many(datas)

    def find_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)