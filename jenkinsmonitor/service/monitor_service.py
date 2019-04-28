from jenkinsmonitor.dao.mongo_dao import MongoDao


class MonitorService:

    @staticmethod
    def get_monitor(monitor):
        mongo_dao = MongoDao()
        if monitor == 1:
            return mongo_dao.get_monitor("5cc338388af8fb49d870a72b")
        if monitor == 2:
            return mongo_dao.get_monitor("5cc36dc5e5de66bb9da603ec")
        if monitor == 3:
            return mongo_dao.get_monitor("5cc36dc5e5de66bb9da603ed")
        return mongo_dao.get_monitor("5cc338388af8fb49d870a72b")
