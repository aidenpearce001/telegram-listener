import pymongo

class MongoDBManager:
    def __init__(self, url_string, database):
        self.client = pymongo.MongoClient(url_string)
        self.db = self.client[database]

    def insert_one(self, collection, document):
        return self.db[collection].insert_one(document)

    def insert_many(self, collection, documents):
        return self.db[collection].insert_many(documents)

    def find_one(self, collection, filter=None):
        return self.db[collection].find_one(filter)

    def find(self, collection, filter=None):
        return self.db[collection].find(filter)

    def update_one(self, collection, filter, update):
        return self.db[collection].update_one(filter, update)

    def update_many(self, collection, filter, update):
        return self.db[collection].update_many(filter, update)

    def delete_one(self, collection, filter):
        return self.db[collection].delete_one(filter)

    def delete_many(self, collection, filter):
        return self.db[collection].delete_many(filter)

    def drop_collection(self, collection):
        return self.db[collection].drop()

    def drop_database(self):
        return self.client.drop_database(self.db.name)
