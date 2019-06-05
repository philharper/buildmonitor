import configparser

from jenkinsmonitor.entities.monitor import Monitor


class MonitorService:

    dao = ""

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('application.properties')

        if config.has_section('MONGO'):
            from jenkinsmonitor.dao.mongo_dao import MongoDao
            self.dao = MongoDao()
        if config.has_section('MYSQL'):
            from jenkinsmonitor.dao.mysql_dao import MySqlDao
            self.dao = MySqlDao()

    def get_monitor(self, monitor_id):
        return self.dao.get_monitor(monitor_id)

    def get_monitors(self):
        monitors = []

        for monitor in self.dao.get_monitors():
            monitors.append(Monitor(monitor['_id'], monitor['title'], monitor['jobs'], monitor['sonar_key']))

        return monitors

    def create_monitor(self, monitor):
        self.dao.create_monitor(monitor)


