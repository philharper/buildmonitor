

class Monitor:

    id = ""
    title = ""
    jobs = []
    sonar_key = ""

    def __init__(self, id, title, jobs, sonar_key):
        self.id = id
        self.title = title
        self.jobs = jobs
        self.sonar_key = sonar_key
