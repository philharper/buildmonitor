from jenkinsmonitor.dao.mongo_dao import MongoDao
from jenkinsmonitor.entities.monitor import Monitor


class MonitorService:

    @staticmethod
    def get_monitor(monitor_id):
        mongo_dao = MongoDao()
        # if monitor == 1:
        #     return mongo_dao.get_monitor("5cc338388af8fb49d870a72b")
        # if monitor == 2:
        #     return mongo_dao.get_monitor("5cc36dc5e5de66bb9da603ec")
        # if monitor == 3:
        #     return mongo_dao.get_monitor("5cc36dc5e5de66bb9da603ed")
        # return mongo_dao.get_monitor("5cc338388af8fb49d870a72b")
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

