# Apify data tools: usage examples

Copy-paste examples for four data tools on the Apify Store. Each one returns clean JSON, CSV or Excel, needs no login to the source site, and is billed per result.

| Tool | What it returns | Price |
|---|---|---|
| [Google Ads Transparency Scraper](https://apify.com/gbm11/google-ads-transparency-scraper-competitor-ads-by-domain) | Every Search, YouTube and Display ad a company runs, by domain or advertiser name | $1.50 per 1,000 ads |
| [ESPN Scores, Standings and Odds](https://apify.com/gbm11/espn-scores-standings-odds) | Scores, schedules, betting lines, standings, teams and news for NBA, NFL, MLB, NHL, college and soccer | $1.00 per 1,000 rows |
| [Bulk Phone Number Validator](https://apify.com/gbm11/bulk-phone-number-validator-format-line-type-carrier) | Valid or not, E.164 format, line type (mobile, landline, VoIP), carrier, region, timezone | $0.50 per 1,000 numbers |
| [New Business Registrations](https://apify.com/gbm11/new-business-registrations-secretary-of-state-search) | Newly registered businesses from Secretary of State records in NY, TX, CO, OR and CT | $1.00 per 1,000 records |

## Setup

1. Create a free [Apify account](https://apify.com) and copy your API token from Settings, then API and Integrations.
2. Put it in an environment variable:

```bash
export APIFY_TOKEN=your_token_here
```

## One-line call with curl

This runs a tool and returns the results in the same response.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/gbm11~google-ads-transparency-scraper-competitor-ads-by-domain/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries": ["nike.com"], "country": "US", "maxAdsPerQuery": 50}'
```

## Python

```bash
pip install apify-client
python python/google_ads_competitor.py
```

- [python/google_ads_competitor.py](python/google_ads_competitor.py): every Google ad a competitor is running
- [python/nba_scores_odds.py](python/nba_scores_odds.py): today's NBA games with betting lines
- [python/validate_phone_list.py](python/validate_phone_list.py): split a phone list into mobile and landline
- [python/new_texas_businesses.py](python/new_texas_businesses.py): businesses registered in Texas in the last 7 days

## Node.js

```bash
npm install apify-client
node node/run.mjs
```

[node/run.mjs](node/run.mjs) runs any of the four tools with an example input.

## Inputs at a glance

**Google Ads Transparency Scraper**

```json
{ "queries": ["nike.com", "Shopify"], "country": "US", "format": "all", "maxAdsPerQuery": 200, "includeDetails": false }
```

`queries` accepts a domain, an advertiser name, or an advertiser ID. `country` is a two-letter code or `ANY`.

**ESPN Scores, Standings and Odds**

```json
{ "leagues": ["basketball/nba", "football/nfl"], "dataTypes": ["games", "standings"], "dateFrom": "2026-11-01", "dateTo": "2026-11-07" }
```

Leagues are written as `sport/league`, for example `baseball/mlb`, `hockey/nhl`, `soccer/eng.1`, `football/college-football`.

**Bulk Phone Number Validator**

```json
{ "phoneNumbers": ["+1 415 555 2671", "020 7946 0958"], "defaultCountry": "GB", "onlyValid": false }
```

**New Business Registrations**

```json
{ "states": ["TX", "NY"], "registeredFrom": "2026-11-01", "nameContains": "roofing", "maxPerState": 1000 }
```

Leave the dates empty to get the last 7 days.

## Notes

These tools read public pages and official open data only. They are not affiliated with Google, ESPN or any state government.
