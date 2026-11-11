"""Print today's NBA games with scores and betting lines."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("gbm11/espn-scores-standings-odds").call(run_input={"leagues": ["basketball/nba"], "dataTypes": ["games"]})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("name"), "|", item.get("status"), "|", (item.get("odds") or {}).get("details"))
