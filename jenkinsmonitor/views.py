from django.shortcuts import render

from jenkinsmonitor.service.jenkins_service import JenkinsService
from jenkinsmonitor.service.monitor_service import MonitorService


def index(request):
    return ""


def monitor(request, monitor_id):
    jenkins_service = JenkinsService()
    monitor_service = MonitorService()

    jobs_list = monitor_service.get_jobs_list(monitor_id)
    jenkins_jobs = []

    for job in jobs_list:
        job = jenkins_service.get_jenkins_job(job)
        jenkins_jobs.append(job)

    context = {
        'jobs': jenkins_jobs
    }

    return render(request, 'jenkins/monitor.html', context)
