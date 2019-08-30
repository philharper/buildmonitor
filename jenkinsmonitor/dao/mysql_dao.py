import configparser
import json

import mysql.connector

from jenkinsmonitor.dao.dao_interface import Dao


class MySqlDao(Dao):

    config = configparser.ConfigParser()
    config.read('application.properties')
    mysql_db = ""

    def get_monitor(self, monitor_id):
        cursor = self.connect()

        cursor.execute("SELECT monitor FROM monitors WHERE id = " + monitor_id)

        result = cursor.fetchall()
        self.close_connection(cursor)
        return json.loads(result[0][0])

    def get_monitors(self):
        cursor = self.connect()
        cursor.execute("SELECT * FROM monitors")
        result = cursor.fetchall()
        self.close_connection(cursor)

        monitor_list = []

        for monitor in result:
            monitor_dict = json.loads(monitor[1])
            monitor_dict["_id"] = monitor[0]
            monitor_list.append(monitor_dict)

        return monitor_list

    def create_monitor(self, monitor):
        cursor = self.connect()
        monitor = monitor.__dict__
        del monitor["id"]

        sql = "INSERT INTO monitors (monitor) VALUES ('" + json.dumps(monitor) + "')"

        cursor.execute(sql)

        self.mysql_db.commit()
        self.close_connection(cursor)

    def delete_monitor(self, monitor_id):
        cursor = self.connect()

        cursor.execute("DELETE FROM monitors WHERE id = " + monitor_id)

        self.mysql_db.commit()
        self.close_connection(cursor)

    def update_monitor(self, monitor):
        cursor = self.connect()
        monitor_id = monitor.id
        monitor = monitor.__dict__
        del monitor["id"]

        cursor.execute("UPDATE monitors SET monitor = '" + json.dumps(monitor) + "' WHERE id = " + monitor_id)

        self.mysql_db.commit()
        self.close_connection(cursor)

    def close_connection(self, cursor):
        cursor.close()
        self.mysql_db.close()

    def connect(self):
        self.mysql_db = mysql.connector.connect(
            host=self.config['MYSQL']['host'],
            user=self.config['MYSQL']['user'],
            port=int(self.config['MYSQL']['port']),
            password=self.config['MYSQL']['password'],
            database=self.config['MYSQL']['database'],
            auth_plugin='mysql_native_password')
        return self.mysql_db.cursor()

