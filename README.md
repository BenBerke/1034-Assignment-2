CS1034 Assignment 2




- This project implements a simple job allocation system.
Jobs can be added, removed, edited, searched and be saved to/loaded from a .csv file
It ensures no job exceeds 6 hours and no worker has more than 8 hours in total.


## Files

-job.py: Defines the job class, has methods for getting information. Raises error if data is from the wrong type

-job_manager.py: Defines the JobManager class which defines jobs. Includes methods for managing and searching jobs. And CSV load/save

-test_job_manager.py: Demonstrates all the functionalities using print statements

## How to run
- Make sure simple_data.csv is in the same folder as scripts
- Run the test script:
  - python test_job_manager.py

## Features
- Add, edit, remove jobs
- Validate job input
- Ensure no worker exceeds 8 hours per day
- Search through jobs
- Calculate total cost and category count per worker
- Load and save jobs from/to csv
