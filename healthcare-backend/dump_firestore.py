from google.cloud import firestore
import json

db = firestore.Client()

collections = ["members", "claims", "eligibility", "benefits",
               "providers", "preauthorizations", "policies", "test"]

out = {}
for col in collections:
    try:
        docs = list(db.collection(col).stream())
        out[col] = [{**d.to_dict(), "_id": d.id} for d in docs]
        print(f"{col}: {len(out[col])} docs")
    except Exception as e:
        print(f"{col}: skipped ({e})")

with open("firestore_data.json", "w") as f:
    json.dump(out, f, indent=2, default=str)

print("Saved firestore_data.json")
