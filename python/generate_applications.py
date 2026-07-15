import random
import pandas as pd

NUM_APPLICATIONS = 45000
NUM_STUDENTS = 5000

DRIVES = list(range(101,108))      # 101-107

statuses = [
    "Applied",
    "Resume Shortlisted",
    "OA Cleared",
    "Interviewing",
    "Offered",
    "Rejected",
    "Accepted"
]

applications = []

for app_id in range(1, NUM_APPLICATIONS + 1):

    applications.append({

        "application_id": app_id,

        "student_id": f"ST{random.randint(1,NUM_STUDENTS):04d}",

        "drive_id": random.choice(DRIVES),

        "application_date":
            f"2026-08-{random.randint(1,30):02d}",

        "application_status":
            random.choices(
                statuses,
                weights=[10,20,20,15,10,20,5]
            )[0],

        "oa_score":
            random.randint(40,100)

    })

pd.DataFrame(applications).to_csv(
    "data/applications.csv",
    index=False
)

print("applications.csv generated")