from django.shortcuts import render

from jenkinsmonitor.service.jenkins_service import JenkinsService
from jenkinsmonitor.service.monitor_service import MonitorService


def index(request):
    return ""


def monitor(request, monitor_id):
    jenkins_service = JenkinsService()
    monitor_service = MonitorService()

    jenkins_jobs = []
    monitor = monitor_service.get_monitor(monitor_id)

    for job in monitor['jobs']:
        job = jenkins_service.get_jenkins_job(job)
        jenkins_jobs.append(job)

    return render(request, 'jenkins/monitor.html', {'jobs': jenkins_jobs, 'title': monitor['title']})
