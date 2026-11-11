// Usage: APIFY_TOKEN=... node node/run.mjs [ads|espn|phone|business]
import { ApifyClient } from 'apify-client';

const examples = {
    ads: ['gbm11/google-ads-transparency-scraper-competitor-ads-by-domain', { queries: ['nike.com'], country: 'US', maxAdsPerQuery: 100 }],
    espn: ['gbm11/espn-scores-standings-odds', { leagues: ['basketball/nba'], dataTypes: ['games', 'standings'] }],
    phone: ['gbm11/bulk-phone-number-validator-format-line-type-carrier', { phoneNumbers: ['+1 415 555 2671', '020 7946 0958'], defaultCountry: 'GB' }],
    business: ['gbm11/new-business-registrations-secretary-of-state-search', { states: ['TX'], maxPerState: 500 }],
};

const [actorId, input] = examples[process.argv[2] ?? 'ads'];
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor(actorId).call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} results`);
console.log(JSON.stringify(items.slice(0, 3), null, 2));
