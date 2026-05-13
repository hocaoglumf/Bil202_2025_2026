class JobView:
    @staticmethod
    def show_jobs(jobs):
        print("--- AKTİF İŞ LİSTESİ ---")
        for job in jobs:
            print(f"ID: {job['id']} | İş: {job['name']} | Vade: {job['due_date']}")

    @staticmethod
    def show_message(message):
        print(f"Sistem Mesajı: {message}")