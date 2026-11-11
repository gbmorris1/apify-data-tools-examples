"""Split a phone list into mobile and landline numbers."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("gbm11/bulk-phone-number-validator-format-line-type-carrier").call(run_input={"phoneNumbers": ["+1 415 555 2671", "020 7946 0958", "+49 30 901820"], "defaultCountry": "GB"})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["input"], "|", item["valid"], "|", item.get("type"), "|", item.get("e164"))
