class JobModel:
    def __init__(self):
        self.jobs = [
            {'id': 1, 'name': 'Engine Reboring', 'due_date': '10h'},
            {'id': 2, 'name': 'Lathe Work', 'due_date': '12h'}
        ]

    def get_all_jobs(self):
        return self.jobs

    def add_job(self, name, due_date):
        self.jobs.append({'id': len(self.jobs)+1, 'name': name, 'due_date': due_date})