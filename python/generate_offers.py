import pandas as pd
import random

applications = pd.read_csv("data/applications.csv")
drives = pd.read_csv("data/placement_drives.csv")

offers = []

offer_id = 1

for _, app in applications.iterrows():

    if app["application_status"] not in ["Offered","Accepted"]:
        continue

    drive = drives[drives["drive_id"] == app["drive_id"]].iloc[0]

    offers.append({

        "offer_id": offer_id,

        "application_id": app["application_id"],

        "offered_ctc": drive["ctc"],

        "offer_date": f"2026-09-{random.randint(1,30):02d}",

        "accepted": app["application_status"]=="Accepted"

    })

    offer_id += 1

df = pd.DataFrame(offers)

df.to_csv("data/offers.csv",index=False)

print("Offers generated:",len(df))
