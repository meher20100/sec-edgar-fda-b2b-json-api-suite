```python
"""
Quickstart script for the Mehdad DataLabs SEC EDGAR, FDA & B2B Intelligence API Suite.
Full portfolio: https://apify.com/mehdad-datalabs

Install dependencies:
    pip install apify-client pandas
"""

import os
import pandas as pd
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_API_TOKEN")
client = ApifyClient(APIFY_TOKEN)


def fetch_sec_form4_insider_trades():
    print("1. Fetching SEC Form 4 Insider Trades (NVDA, AAPL, MSFT)...")
    run = client.actor("mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api").call(
        run_input={
            "tickers": ["NVDA", "AAPL", "MSFT"],
            "transactionCodes": ["P", "S"],
            "minDollarValue": 25000,
            "maxFilingsPerTicker": 10,
        }
    )
    items = client.dataset(run["defaultDatasetId"]).list_items().items
    return pd.DataFrame(items)


def fetch_sec_13f_whale_holdings():
    print("2. Fetching SEC Form 13F Whale Holdings (Berkshire Hathaway & Scion)...")
    run = client.actor("mehdad-datalabs/sec-13f-institutional-holdings-hedge-fund-whale-scraper").call(
        run_input={
            "institutions": ["0001067983", "0001649339"],
            "minHoldingValueUsd": 1000000,
            "maxHoldingsPerInstitution": 25,
        }
    )
    items = client.dataset(run["defaultDatasetId"]).list_items().items
    return pd.DataFrame(items)


def fetch_sec_10k_10q_financials():
    print("3. Fetching SEC 10-K & 10-Q XBRL Financial Statements (NVDA, AAPL)...")
    run = client.actor("mehdad-datalabs/sec-10k-10q-xbrl-financial-statements-earnings-api").call(
        run_input={
            "tickers": ["NVDA", "AAPL"],
            "periodType": "ALL",
            "maxPeriodsPerTicker": 8,
        }
    )
    items = client.dataset(run["defaultDatasetId"]).list_items().items
    return pd.DataFrame(items)


def fetch_newly_funded_startups_form_d():
    print("4. Fetching Newly Funded Startups from SEC Form D XML...")
    run = client.actor("mehdad-datalabs/sec-form-d-startup-funding-vc-b2b-lead-scraper").call(
        run_input={
            "searchKeywords": ["AI", "Software", "Biotech"],
            "minAmountRaisedUsd": 500000,
            "maxResults": 20,
        }
    )
    items = client.dataset(run["defaultDatasetId"]).list_items().items
    return pd.DataFrame(items)


if __name__ == "__main__":
    df_insiders = fetch_sec_form4_insider_trades()
    print(f"Extracted {len(df_insiders)} insider transactions.")
    if not df_insiders.empty:
        print(df_insiders.head(5))
