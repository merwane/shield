import pymongo
from config import DATABASE_HOST, DATABASE_CLIENT
from mongoengine import connect

class Database:
    def __init__(self):
        self.host = DATABASE_HOST
        self.client = DATABASE_CLIENT
        connect(DATABASE_CLIENT, host=DATABASE_HOST, retryWrites=False, tls=True, tlsAllowInvalidCertificates=True)

    def light(self):
        client = pymongo.MongoClient(host=self.host, retryWrites=False, tls=True, tlsAllowInvalidCertificates=True)
        database = client[self.client]
        return database