# Build Monitor

A build monitor application that is able to display jobs from Jenkins. The monitor is able to show when the job is currently running and that the current status of that build is.

To run you'll need the following Python libraries installed.

- configparser
- python-jenkins
- requests
- pymongo

You will also need a properties file named application.properties in the root with the Jenkins, Sonar and DB properties in them as described below. Only place connection properties for one database so that the application is able to determine what type of datasource to use.

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
    
    [MYSQL]
    host=
    port=
    database=
    user=
    password=
