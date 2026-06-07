import json
import os
from datetime import datetime

import requests

API_KEY = os.environ["SERP_API_KEY"]
SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"]

# Fetch the author's profile via SerpApi's official Google Scholar Author API.
# This avoids scraping Google directly (which blocks GitHub runner IPs).
params = {
    "engine": "google_scholar_author",
    "author_id": SCHOLAR_ID,
    "api_key": API_KEY,
    "num": 100,
    "sort": "pubdate",
}
resp = requests.get("https://serpapi.com/search", params=params, timeout=60)
resp.raise_for_status()
data = resp.json()

if "error" in data:
    raise SystemExit(f"SerpApi error: {data['error']}")

# Total citations: cited_by.table -> first row -> citations.all
total_citations = 0
for row in data.get("cited_by", {}).get("table", []):
    if "citations" in row:
        total_citations = row["citations"].get("all", 0) or 0
        break

# Per-paper citations, keyed by SerpApi citation_id (== Scholar author_pub_id,
# e.g. "cW-kkGwAAAAJ:LkGwnXOMwfcC"), matching the data-attrs in about.md.
publications = {}
for article in data.get("articles", []):
    cid = article.get("citation_id")
    if not cid:
        continue
    publications[cid] = {
        "num_citations": (article.get("cited_by") or {}).get("value", 0) or 0,
        "title": article.get("title"),
    }

result = {
    "citedby": total_citations,
    "publications": publications,
    "updated": str(datetime.now()),
}

os.makedirs("results", exist_ok=True)
with open("results/gs_data.json", "w") as outfile:
    json.dump(result, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{total_citations}",
}
with open("results/gs_data_shieldsio.json", "w") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print(f"OK: total={total_citations}, publications={len(publications)}")
