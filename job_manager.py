from job import Job
import csv

class JobManager:
    """
    Class for managing jobs in a single worker
    Ensures a worker can not have more than 8 hours of work.
    Has functionalities for adding, editing and removing jobs.
    """
    def __init__(self, jobs=None):
        self._jobs = jobs or []

    def get_jobs(self):
        return self._jobs

    def __str__(self):
        return "\n".join(str(job) for job in self._jobs)

    def __repr__(self):
        return f"JobManager(jobs={self._jobs})"

    # Adds a job ensuring the hours do not exceed 8. Raises a value error if so
    def add_job(self, job):
        current_hours = sum(
            j.get_hours() for j in self._jobs
            if j.get_name() == job.get_name() and j.get_date() == job.get_date()
        )
        if current_hours + job.get_hours() > 8:
            raise ValueError(f"Total hours for {job.get_name()} on {job.get_date()} cannot exceed 8")
        self._jobs.append(job)

    def remove_job(self, job):
        self._jobs.remove(job)

    # Changes old_job to new_job ensuring the hours do not exceed 8
    def edit_job(self, old_job, new_job):
        if old_job not in self._jobs:
            raise ValueError("Job does not exist")

        # Compute total hours for this worker on the same date, excluding old_job
        current_hours = sum(
            j.get_hours() for j in self._jobs
            if j.get_name() == old_job.get_name() and j.get_date() == old_job.get_date() and j != old_job
        )

        if current_hours + new_job.get_hours() > 8:
            raise ValueError(f"Total hours for {new_job.get_name()} on {new_job.get_date()} cannot exceed 8")

        index = self._jobs.index(old_job)
        self._jobs[index] = new_job


    # Returns all jobs with the category that exactly matches category
    def search_by_category(self, category):
        return [job for job in self._jobs if job.get_category() == category]

    # Returns all jobs with the rate that exactly matches rate
    def search_by_rate(self, rate):
        return [job for job in self._jobs if job.get_rate() == rate]

    # Returns all jobs with the name and date that exactly matches name and date
    def search_by_name_and_date(self, name, date):
        return [job for job in self._jobs if job.get_name() == name and job.get_date() == date]

    # Returns the total cost of every single job a worker has
    def get_total_cost_per_name(self, names):
        result = {}
        for name in names:
            total_cost = sum(job.get_rate() * job.get_hours() for job in self._jobs if job.get_name() == name)
            result[name] = total_cost
        return result

    # Returns the count of jobs a worker has
    def get_category_count_per_name(self):
        result = {}
        for job in self._jobs:
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
            for job in self._jobs:
                writer.writerow([job.get_name(), job.get_category(),
                                 job.get_rate(), job.get_date(), job.get_hours()])
