# n8n Workflow Templates (Powered by Mehdad DataLabs on Apify)

Ready-to-import **n8n** automation templates using lightweight, zero-browser **Apify Actors** by [Mehdad DataLabs](https://apify.com/mehdad-datalabs).

## Available Templates

| Template | Use Case | Apify Actor(s) Used |
|---|---|---|
| [`1_sec_form4_insider_telegram.json`](./1_sec_form4_insider_telegram.json) | Daily SEC Form 4 insider buying alerts routed by trade size ($50K+ / $500K+) to Telegram | [SEC Form 4 Insider Trading Scraper](https://apify.com/mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api) |
| [`2_shopify_competitor_price_sheets.json`](./2_shopify_competitor_price_sheets.json) | Automated Shopify competitor catalog & price-drop monitor logged to Google Sheets | [Shopify Store Spy Scraper](https://apify.com/mehdad-datalabs/shopify-store-spy-product-catalog-price-b2b-scraper) |
| [`3_yc_startups_b2b_enrichment_sheets.json`](./3_yc_startups_b2b_enrichment_sheets.json) | Y Combinator startup batch scraper + B2B email & tech-stack enrichment to Google Sheets | [YC Startup Directory Scraper](https://apify.com/mehdad-datalabs/y-combinator-yc-startup-directory-b2b-lead-scraper) + [B2B Website Email & Tech Stack Enricher](https://apify.com/mehdad-datalabs/b2b-website-email-phone-social-links-tech-stack-scraper) |

## Quick Setup
1. Download any `.json` file above and import it into n8n (**Workflows -> Import from File**).
2. Open the **Set Config** node and paste your `YOUR_APIFY_API_TOKEN` from [Apify Console](https://console.apify.com/account/integrations).
3. Connect your Telegram or Google Sheets credentials and click **Execute workflow**.
