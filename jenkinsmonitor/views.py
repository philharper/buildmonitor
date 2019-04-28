from django.shortcuts import render, redirect

from jenkinsmonitor.entities.monitor import Monitor
from jenkinsmonitor.service.jenkins_service import JenkinsService
from jenkinsmonitor.service.monitor_service import MonitorService
from jenkinsmonitor.service.sonar_service import SonarService


def index(request):

    monitor_service = MonitorService()

    context = {
        'monitors': monitor_service.get_monitors()
    }

    return render(request, 'jenkins/index.html', context)


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


def create(request):
    return render(request, 'jenkins/create.html', {})


def create_monitor(request):
    title = request.POST['monitor-title']
    sonar_key = request.POST['sonar-key']
    jobs = []

    i = 0
    while i < 9:
        if 'jenkins-job[' + str(i) + ']' in request.POST:
            jobs.append(request.POST['jenkins-job[' + str(i) + ']'])
        i += 1

    monitor_service = MonitorService()
    monitor_service.create_monitor(Monitor(0, title, jobs, sonar_key))

    return redirect('/jenkins')
