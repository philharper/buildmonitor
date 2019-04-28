# Build Monitor

A build monitor application that is able to display jobs from Jenkins. The monitor is able to show when the job is currently running and that the current status of that build is.

To run you'll need the following Python libraries installed.

- configparser
- python-jenkins
- requests
- pymongo

You will also need a properties file named application.properties in the root with the Jenkins, Sonar and Mongo properties in them as described below.

    [JENKINS]
    url=
    username=
    token=

    [SONAR]
    host=
    port=
    token=

    [MONGO]
    host=
    port=
    database=
    collection=
