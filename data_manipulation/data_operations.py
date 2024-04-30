class DataOperations:
    def __init__(self, db_connection):
        self.connection = db_connection

    def insert_document(self, collection_name, document):
        collection = self.connection.get_collection(collection_name)
        collection.insert_one(document)

    def find_document(self, collection_name, query):
        collection = self.connection.get_collection(collection_name)
        return collection.find_one(query)

    # Additional CRUD operations can be added here
