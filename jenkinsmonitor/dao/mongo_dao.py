import configparser

import pymongo
from bson import ObjectId

from jenkinsmonitor.dao.dao import Dao


class MongoDao(Dao):

    config = configparser.ConfigParser()
    config.read('application.properties')

    mongo_client = pymongo.MongoClient(
        "mongodb://" + config['MONGO']['host'] + ":" + config['MONGO']['port'])
    mongo_database = mongo_client["buildmonitor"]
    mongo_collection = mongo_database["monitor"]

    def get_monitor(self, monitor_id):
        query = {"_id": ObjectId(monitor_id)}
        return self.mongo_collection.find_one(query)

    def get_monitors(self):
        monitors = self.mongo_collection.find()
        for monitor in monitors:
            print(monitor)
        return self.mongo_collection.find()

    def create_monitor(self, monitor):
        self.mongo_collection.insert_one(monitor.__dict__)

    def delete_monitor(self, monitor_id):
        self.mongo_collection.delete_one(self.get_monitor(monitor_id))
