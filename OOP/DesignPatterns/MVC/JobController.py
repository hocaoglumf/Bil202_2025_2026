class JobController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def list_jobs(self):
        jobs = self.model.get_all_jobs()
        self.view.show_jobs(jobs)

    def create_job(self, name, due_date):
        self.model.add_job(name, due_date)
        self.view.show_message(f"'{name}' başarıyla eklendi.")

        