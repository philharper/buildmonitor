

class MonitorService:

    targeryen_jobs = {'title': 'House Targaryen - VI', 'jobs': ['VI Data Warehouse - Unit Test', 'Create Staging Tables', 'Run Stored Procedures',
                 'VI Data Warehouse - Integration Test', 'VI Data Warehouse Test',
                 'Transformation Runner - DAL TC (UAT)', 'Transformation Runner - DAL (LIVE)',
                 'Transformation Runner - DAL TC (LIVE)']}
    lannister_jobs = {'title': 'House Lannister - QualityNet', 'jobs': ['Deploy QualityNet to Test']}

    def get_monitor(self, monitor):
        if monitor == 1:
            return self.targeryen_jobs
        if monitor == 2:
            return self.lannister_jobs
        return []
