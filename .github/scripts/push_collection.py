import json
import os
import sys
import urllib.request

COLLECTION_UID = "46918506-c61b35ec-a44a-44c8-9150-b7d3f388f05c"

api_key = os.environ["POSTMAN_API_KEY"]

with open("collection.json") as f:
    data = json.load(f)

payload = data if "collection" in data else {"collection": data}

req = urllib.request.Request(
    f"https://api.getpostman.com/collections/{COLLECTION_UID}",
    data=json.dumps(payload).encode(),
    headers={
        "X-Api-Key": api_key,
        "Content-Type": "application/json",
    },
    method="PUT",
)

with urllib.request.urlopen(req) as res:
    print(res.read().decode())