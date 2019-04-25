import configparser
import requests


class SonarService:

    def get_job_metrics(self, key):
        config = configparser.ConfigParser()
        config.read('application.properties')
        url = config['SONAR']['host'] + ":" + config['SONAR'][
            'port'] + '/api/measures/component?metricKeys=bugs,violations&componentKey=' + key
        return requests.get(url=url).json()
