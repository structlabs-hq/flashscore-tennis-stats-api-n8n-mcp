"""Run Flashscore Tennis Stats API on Apify and print the first rows."""
import json
import os
import urllib.request

TOKEN = os.environ.get("APIFY_TOKEN")
if not TOKEN:
    raise SystemExit("Set APIFY_TOKEN first")

payload = json.loads(
    r'''{
  "dayOffsets": ["0"],
  "tours": ["atp", "wta"],
  "matchStatuses": ["finished"],
  "maxItems": 10
}'''
)

req = urllib.request.Request(
    "https://api.apify.com/v2/acts/structlabs~flashscore-tennis-stats-api/run-sync-get-dataset-items",
    data=json.dumps(payload).encode(),
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=300) as response:
    items = json.load(response)

for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False)[:500])
print(f"{len(items)} items")
