class MonitorService:
    targeryen_jobs = {'title': 'House Targaryen - VI',
                      'jobs': ['VI Data Warehouse - Unit Test', 'Deploy VI Tables and Stored Procedures',
                               'Run Stored Procedures (DEV)',
                               'VI Data Warehouse - Integration Test', 'VI Data Warehouse - Acceptance Test',
                               'Transformation Runner - DAL TC (UAT)', 'Transformation Runner - DAL (LIVE)',
                               'Transformation Runner - DAL TC (LIVE)'],
                      'sonar_key': 'com.vistair:vi:vi-data-warehouse'}
    lannister_jobs = {'title': 'House Lannister - QualityNet',
                      'jobs': ['Dev Build QualityNet Trunk', 'QualityNet-Sanity-Tests', 'QualityNet Sonar Analysis'],
                      'sonar_key': 'com.vistair:vi:vi-data-warehouse'}

    def get_monitor(self, monitor):
        if monitor == 1:
            return self.targeryen_jobs
        if monitor == 2:
            return self.lannister_jobs
        return []
