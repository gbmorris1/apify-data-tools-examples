"""List every Google ad a competitor is running."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("gbm11/google-ads-transparency-scraper-competitor-ads-by-domain").call(run_input={"queries": ["nike.com"], "country": "US", "maxAdsPerQuery": 100})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
