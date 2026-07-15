import pandas as pd
import random

applications = pd.read_csv("data/applications.csv")

rows = []

round_id = 1

for _, app in applications.iterrows():

    status = app["application_status"]

    if status in ["Interviewing", "Offered", "Accepted"]:

        rounds = ["Technical 1", "Technical 2", "HR"]

    elif status == "OA Cleared":

        rounds = ["Technical 1"]

    else:

        continue

    for r in rounds:

        rows.append({

            "round_id": round_id,

            "application_id": app["application_id"],

            "round_name": r,

            "round_date": f"2026-09-{random.randint(1,30):02d}",

            "result": "Pass"

        })

        round_id += 1

df = pd.DataFrame(rows)

df.to_csv("data/interview_rounds.csv", index=False)

print("Interview rounds generated:", len(df))