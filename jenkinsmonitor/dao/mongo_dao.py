import configparser

import pymongo
from bson import ObjectId

from jenkinsmonitor.dao.dao_interface import Dao


class MongoDao(Dao):

    config = configparser.ConfigParser()
    config.read('application.properties')

    connection_string = "mongodb://{}:{}@{}:{}".format(
        config['MONGO']['user'],
        config['MONGO']['password'],
        config['MONGO']['host'],
        config['MONGO']['port'])

    print (connection_string)

    mongo_client = pymongo.MongoClient(connection_string)
    
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

    def update_monitor(self, monitor):
        query = {"_id": ObjectId(monitor.id)}
        self.mongo_collection.update(query, {"$set": monitor.__dict__})
