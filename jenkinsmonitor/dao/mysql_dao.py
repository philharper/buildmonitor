import configparser
import json

import mysql.connector


class MySqlDao:

    config = configparser.ConfigParser()
    config.read('application.properties')
    mysql_db = ""

    def get_monitor(self, monitor_id):
        self.connect()
        cursor = self.mysql_db.cursor()
        cursor.execute("SELECT monitor FROM monitors WHERE id = " + monitor_id)
        result = cursor.fetchall()
        cursor.close()
        self.mysql_db.close()
        return json.loads(result[0][0])

    def get_monitors(self):
        self.connect()
        cursor = self.mysql_db.cursor()
        cursor.execute("SELECT * FROM monitors")
        result = cursor.fetchall()
        cursor.close()
        self.mysql_db.close()

        monitor_list = []

        for monitor in result:
            monitor_dict = json.loads(monitor[1])
            monitor_dict["_id"] = monitor[0]
            monitor_list.append(monitor_dict)

        return monitor_list

    def create_monitor(self, monitor):
        self.connect()
        cursor = self.mysql_db.cursor()
        monitor = monitor.__dict__
        del monitor["id"]
        sql = "INSERT INTO monitors (monitor) VALUES ('" + json.dumps(monitor) + "')"
        cursor.execute(sql)

        self.mysql_db.commit()
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

