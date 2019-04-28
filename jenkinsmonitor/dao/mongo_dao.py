import configparser

import pymongo
from bson import ObjectId


class MongoDao:

    config = configparser.ConfigParser()
    config.read('application.properties')

    def get_monitor(self, monitor_id):

        mongo_client = pymongo.MongoClient(
            "mongodb://" + self.config['MONGO']['host'] + ":" + self.config['MONGO']['port'])
        mongo_database = mongo_client["buildmonitor"]
        mongo_collection = mongo_database["monitor"]
        query = {"_id": ObjectId(monitor_id)}
        return mongo_collection.find_one(query)
