import time
import jenkins
import configparser


class JenkinsService:
    jenkins_server = ""

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('application.properties')
        self.jenkins_server = jenkins.Jenkins(config['JENKINS']['url'], username=config['JENKINS']['username'],
                                              password=config['JENKINS']['token'])

    def get_jenkins_jobs(self):
        return self.jenkins_server.get_jobs()

    def get_jenkins_job(self, name):
        job = ""
        try:
            job = self.jenkins_server.get_job_info(name)
            job['latest_build'] = self.get_build_info(name, job['lastBuild']['number'])
            job['latest_build']['progress'] = self.calculate_progress(job['latest_build']['timestamp'],
                                                                      job['latest_build']['estimatedDuration'])
        except Exception as e:
            print("There was an error retrieving the job")
            print(e)

        return job

    def get_build_info(self, name, number):
        return self.jenkins_server.get_build_info(name, number, depth=0)

    @staticmethod
    def calculate_progress(timestamp, estimated_time):
        current_running_time = int(round(time.time() * 1000)) - timestamp
        progress = int(round(current_running_time / estimated_time * 100))
        return progress
