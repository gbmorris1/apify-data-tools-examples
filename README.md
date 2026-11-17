# Apify data tools: usage examples

Copy-paste examples for data tools on the Apify Store. Each one returns clean JSON, CSV or Excel, needs no login to the source site, and is billed per result.

| Tool | What it returns | Price |
|---|---|---|
| [Google Ads Transparency Scraper](https://apify.com/gbm11/google-ads-transparency-scraper-competitor-ads-by-domain) | Every Search, YouTube and Display ad a company runs, by domain or advertiser name | $1.50 per 1,000 ads |
| [ESPN Scores, Standings and Odds](https://apify.com/gbm11/espn-scores-standings-odds) | Scores, schedules, betting lines, standings, teams and news for NBA, NFL, MLB, NHL, college and soccer | $1.00 per 1,000 rows |
| [Bulk Phone Number Validator](https://apify.com/gbm11/bulk-phone-number-validator-format-line-type-carrier) | Valid or not, E.164 format, line type (mobile, landline, VoIP), carrier, region, timezone | $0.50 per 1,000 numbers |
| [New Business Registrations](https://apify.com/gbm11/new-business-registrations-secretary-of-state-search) | Newly registered businesses from Secretary of State records in NY, TX, CO, OR and CT | $1.00 per 1,000 records |
| [Google News Scraper](https://apify.com/gbm11/google-news-scraper-search-by-keyword-date-and-country) | Google News articles by keyword, country, language and date range | $1.00 per 1,000 articles |
| [Website Contact Finder](https://apify.com/gbm11/website-contact-finder-emails-phones-and-social-links) | Emails, phone numbers and social links that companies publish on their own websites | $2.00 per 1,000 websites |
| [Email Validator](https://apify.com/gbm11/email-validator-syntax-mx-disposable-and-typo-check) | Syntax, mail server, disposable domain and typo checks for any email list | $0.50 per 1,000 emails |
| [Google Trending Searches](https://apify.com/gbm11/google-trends-trending-searches-today-by-country) | What people are searching for on Google right now, by country, with traffic and news | $1.00 per 1,000 trends |
| [Google Play Scraper](https://apify.com/gbm11/google-play-scraper-search-apps-and-get-app-details) | Android apps by keyword with rating, installs, price and developer | $1.00 per 1,000 apps |
| [App Store Scraper](https://apify.com/gbm11/app-store-scraper-search-apps-and-get-app-details) | iOS apps by keyword with rating, price, developer and release date | $1.00 per 1,000 apps |
| [App Store Reviews Scraper](https://apify.com/gbm11/app-store-reviews-scraper-ios-app-ratings-and-reviews) | Ratings and reviews for any iOS app, by country | $0.50 per 1,000 reviews |
| [Google Play Reviews Scraper](https://apify.com/gbm11/google-play-reviews-scraper-android-app-reviews) | Reviews for any Android app with version and developer reply | $0.50 per 1,000 reviews |
| [Shopify Products Scraper](https://apify.com/gbm11/shopify-products-scraper-any-store-prices-and-variants) | The full catalog of any Shopify store with prices, variants and stock | $1.00 per 1,000 products |
| [Job Board Scraper](https://apify.com/gbm11/job-board-scraper-greenhouse-lever-and-ashby-jobs) | Open jobs from companies that hire through Greenhouse, Lever or Ashby | $1.50 per 1,000 jobs |
| [Telegram Channel Scraper](https://apify.com/gbm11/telegram-channel-scraper-posts-views-and-media) | Posts, views and media from public Telegram channels | $1.00 per 1,000 posts |

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

**Google News Scraper**

```json
{ "queries": ["Tesla", "artificial intelligence"], "country": "US", "language": "en", "dateFrom": "2026-11-01", "dateTo": "2026-11-07", "maxItemsPerQuery": 500 }
```

Set both dates to search day by day and get past the 100-article limit of a single search.

**New Business Registrations**

```json
{ "states": ["TX", "NY"], "registeredFrom": "2026-11-01", "nameContains": "roofing", "maxPerState": 1000 }
```

Leave the dates empty to get the last 7 days.

**Website Contact Finder**

```json
{ "websites": ["allbirds.com", "bombas.com"], "maxPagesPerSite": 5, "sameDomainEmailsOnly": true }
```

**Email Validator**

```json
{ "emails": ["jane.doe@gmail.com", "test@gmial.com", "someone@mailinator.com"], "onlyValid": false, "removeDuplicates": true }
```

**Google Trending Searches**

```json
{ "countries": ["US", "GB"] }
```

**Google Play Scraper** and **App Store Scraper**

```json
{ "searchTerms": ["workout tracker"], "country": "us", "maxAppsPerSearch": 30 }
```

**App Store Reviews Scraper**

```json
{ "apps": ["Headspace"], "countries": ["us", "gb"], "sort": "mostrecent", "maxReviewsPerApp": 100 }
```

`apps` accepts an App Store link, a numeric app ID or an app name.

**Google Play Reviews Scraper**

```json
{ "apps": ["com.calm.android"], "country": "us", "language": "en", "sort": "newest", "maxReviewsPerApp": 100 }
```

**Shopify Products Scraper**

```json
{ "stores": ["gymshark.com"], "maxProductsPerStore": 100, "oneRowPerVariant": true }
```

**Job Board Scraper**

```json
{ "companies": ["stripe", "https://jobs.lever.co/spotify", "https://jobs.ashbyhq.com/openai"], "titleContains": "engineer" }
```

**Telegram Channel Scraper**

```json
{ "channels": ["durov", "https://t.me/telegram"], "maxPostsPerChannel": 100 }
```

## Notes

These tools read public pages and official open data only. They are not affiliated with Google, Apple, ESPN, Shopify, Telegram, any job board or any state government.
