import pandas as pd
import random

apps = pd.read_csv("data/applications.csv")

rows = []
round_id = 1

for _, app in apps.iterrows():

    if app["application_status"] in ["Rejected"]:
        continue

    for round_name in ["Technical 1","Technical 2","HR"]:

        rows.append({

            "round_id":round_id,

            "application_id":app["application_id"],

            "round_name":round_name,

            "round_date":
            f"2026-09-{random.randint(1,30):02d}",

            "result":"Pass"

        })

        round_id+=1

df=pd.DataFrame(rows)

df.to_csv("data/interview_rounds.csv",index=False)

print(df.head())
print("Interview Rounds:",len(df))