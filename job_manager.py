from job import Job
import csv

class JobManager:

    def __init__(self, jobs=None):
        self.jobs = jobs or []

    def get_jobs(self):
        return self.jobs

    def __str__(self):
        return "\n".join(str(job) for job in self.jobs)

    def __repr__(self):
        return f"JobManager(jobs={self.jobs})"

    def add_job(self, job):
        current_hours = sum(
            j.get_hours() for j in self.jobs
            if j.get_name() == job.get_name() and j.get_date() == job.get_date()
        )
        if current_hours + job.get_hours() > 8:
            raise ValueError(f"Total hours for {job.get_name()} on {job.get_date()} cannot exceed 8")
        self.jobs.append(job)

    def remove_job(self, job):
        self.jobs.remove(job)

    def edit_job(self, old_job, new_job):
        if old_job not in self.jobs:
            raise ValueError("Job does not exist")

            # Hours for this worker on this date excluding the old job
        current_hours = sum(
            j.get_hours() for j in self.jobs
            if j.get_name() == old_job.get_name() and j.get_date() == old_job.get_date() and j != old_job
        )

        if current_hours + new_job.get_hours() > 8:
            raise ValueError(f"Total hours for {new_job.get_name()} on {new_job.get_date()} cannot exceed 8")

        index = self.jobs.index(old_job)
        self.jobs[index] = new_job

        index = self.jobs.index(old_job)
        self.jobs[index] = new_job

    def search_by_category(self, category):
        return [job for job in self.jobs if job.get_category() == category]

    def search_by_rate(self, rate):
        return [job for job in self.jobs if job.get_rate() == rate]

    def search_by_name_and_date(self, name, date):
        return [job for job in self.jobs if job.get_name() == name and job.get_date() == date]

    def get_total_cost_per_name(self, names):
        result = {}
        for name in names:
            total_cost = sum(job.get_rate() * job.get_hours() for job in self.jobs if job.get_name() == name)
            result[name] = total_cost
        return result

    def get_category_count_per_name(self):
        result = {}
        for job in self.jobs:
            name = job.get_name()
            category = job.get_category()
            if name not in result:
                result[name] = {}
            if category not in result[name]:
                result[name][category] = 0
            result[name][category] += 1
        return result

    def load_from_file(self, file_name):
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                name, category, rate, date, hours = row
                job = Job(name, category, float(rate), date, int(hours))
                self.add_job(job)

    def save_to_file(self, file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "category", "rate", "date", "hours"])  # header
            for job in self.jobs:
                writer.writerow([job.get_name(), job.get_category(),
                                 job.get_rate(), job.get_date(), job.get_hours()])
