from django.shortcuts import render

from jenkinsmonitor.service.jenkins_service import JenkinsService
from jenkinsmonitor.service.monitor_service import MonitorService
from jenkinsmonitor.service.sonar_service import SonarService


def index(request):
    return ""


def monitor(request, monitor_id):
    jenkins_service = JenkinsService()
    monitor_service = MonitorService()
    sonar_service = SonarService()

    jenkins_jobs = []
    monitor = monitor_service.get_monitor(monitor_id)

    for job in monitor['jobs']:
        job = jenkins_service.get_jenkins_job(job)
        if job != "":
            jenkins_jobs.append(job)

    context = {
        'jobs': jenkins_jobs,
        'title': monitor['title'],
        'sonar': sonar_service.get_job_metrics(monitor['sonar_key']),
        'monitor_id': monitor_id,
    }

    return render(request, 'jenkins/monitor.html', context)
