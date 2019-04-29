from jenkinsmonitor.dao.mongo_dao import MongoDao
from jenkinsmonitor.entities.monitor import Monitor


class MonitorService:

    @staticmethod
    def get_monitor(monitor_id):
        mongo_dao = MongoDao()
        return mongo_dao.get_monitor(monitor_id)

    @staticmethod
    def get_monitors():
        mongo_dao = MongoDao()

        monitors = []

        for monitor in mongo_dao.get_monitors():
            monitors.append(Monitor(monitor['_id'], monitor['title'], monitor['jobs'], monitor['sonar_key']))

        return monitors

    @staticmethod
    def create_monitor(monitor):
        mongo_dao = MongoDao()
        mongo_dao.create_monitor(monitor)

