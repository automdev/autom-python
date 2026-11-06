"""Call the featured endpoint and print the JSON result."""

import json
import os

from autom import AutomClient

with AutomClient(os.environ["AUTOM_API_KEY"]) as client:
    response = client.google_search(query="web scraping api")
    print(json.dumps(response.data, indent=2))
