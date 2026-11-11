"""List businesses registered in Texas in the last 7 days."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("gbm11/new-business-registrations-secretary-of-state-search").call(run_input={"states": ["TX"], "maxPerState": 500})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
