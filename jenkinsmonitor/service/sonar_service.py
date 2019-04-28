import configparser
import requests

from jenkinsmonitor.entities.sonar_metrics import SonarMetrics


class SonarService:

    def get_job_metrics(self, key):
        config = configparser.ConfigParser()
        config.read('application.properties')
        url = config['SONAR']['host'] + ":" + config['SONAR'][
            'port'] + '/api/measures/component?metricKeys=bugs,violations,vulnerabilities&componentKey=' + key

        response = requests.get(url=url).json()

        sonar_metrics = SonarMetrics()

        for measure in response['component']['measures']:
            if measure['metric'] == 'bugs':
                sonar_metrics.bugs = measure
            if measure['metric'] == 'violations':
                sonar_metrics.violations = measure
            if measure['metric'] == 'vulnerabilities':
                sonar_metrics.vulnerabilities = measure

        return sonar_metrics
