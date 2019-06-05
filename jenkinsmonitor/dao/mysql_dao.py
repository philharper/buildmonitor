import configparser
import json

import mysql.connector


class MySqlDao:

    config = configparser.ConfigParser()
    config.read('application.properties')

    if config.has_section('MYSQL'):
        mysql_db = mysql.connector.connect(
            host=config['MYSQL']['host'],
            user=config['MYSQL']['user'],
            port=int(config['MYSQL']['port']),
            password=config['MYSQL']['password'],
            database=config['MYSQL']['database'],
            auth_plugin='mysql_native_password')

    def get_monitor(self, monitor_id):
        cursor = self.mysql_db.cursor()
        cursor.execute("SELECT monitor FROM monitors WHERE id = " + monitor_id)
        result = cursor.fetchall()
        return json.loads(result[0][0])

    def get_monitors(self):
        cursor = self.mysql_db.cursor()
        cursor.execute("SELECT * FROM monitors")
        result = cursor.fetchall()

        monitor_list = []

        for monitor in result:
            monitor_dict = json.loads(monitor[1])
            monitor_dict["_id"] = monitor[0]
            monitor_list.append(monitor_dict)

        return monitor_list

    def create_monitor(self, monitor):
        cursor = self.mysql_db.cursor()
        sql = "INSERT INTO monitors (monitor) VALUES ('%s')"
        monitor = monitor.__dict__
        del monitor["id"]
        cursor.execute(sql, json.dumps(monitor))

        self.mysql_db.commit()
