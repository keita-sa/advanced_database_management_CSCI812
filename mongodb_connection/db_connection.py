from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host='localhost', port=27017, db_name='my_database'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]
