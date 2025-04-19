from pymongo import MongoClient
from decouple import config

class MongoDBConfig:
    def __init__(self):
        self.mongo_uri = config("MONGO_URI")
        self.database_name = config("DATABASE_NAME")

        if not self.mongo_uri or not self.database_name:
            raise ValueError("As variáveis MONGO_URI e DATABASE_NAME precisam estar definidas no .env")

        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.database_name]

    def get_db(self):
        return self.db

    def get_collection(self, name: str):
        return self.db[name]
