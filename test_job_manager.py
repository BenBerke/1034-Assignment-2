from job import Job
from job_manager import JobManager

CSV_FILE = "sample_data.csv"

manager = JobManager()
manager.load_from_file(CSV_FILE)

print("Jobs loaded:", len(manager.get_jobs()))


#       ----
# Search by category
#       ----
category = "Research Activities"

results = manager.search_by_category(category)
print(f"\nJobs in category {category}: {len(results)}")
for job in results:
    print(job)

#       ----
# Search by name and date
#       ----
name = "Simonette Thirkettle"
date = "03/08/2024"

results = manager.search_by_name_and_date(name, date)
print(f"\nJobs for {name} on {date}: {len(results)}")
for job in results:
    print(job)

#       ----
# Test total cost per name
#       ----

names = ["Simonette Thirkettle", "Corissa Seid", "Marc Velti"]
costs = manager.get_total_cost_per_name(names)
print("\nTotal cost per name:")
for name, cost in costs.items():
    print(f"{name}: {cost}")

#       ----
# Test category count per name
#       ----
category_counts = manager.get_category_count_per_name()
print("\nCategory count per name:")
for name, categories in category_counts.items():
    print(name)
    for cat, count in categories.items():
        print(f"  {cat}: {count}")

#       ---
# Test adding a job that exceeds 8 hours for a worker
#       ----
try:
    # Find a worker's current total hours
    new_job = Job("Simonette Thirkettle", "Extra Work", 10.0, "03/08/2024", 5)
    manager.add_job(new_job)
except ValueError as e:
    print("\nExpected error when adding job exceeding 8 hours:", e)

#       ----
# Test editing a job
#       ----
old_job = manager.get_jobs()[0]
new_job = Job(old_job.get_name(), old_job.get_category(), old_job.get_rate(), old_job.get_date(), 1)
manager.edit_job(old_job, new_job)
print("\nAfter editing first job:")
print(manager.get_jobs()[0])