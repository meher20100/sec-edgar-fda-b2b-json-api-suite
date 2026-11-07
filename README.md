# 📊 SEC EDGAR, FDA Biotech & US B2B Intelligence JSON API Suite (Python, REST & MCP)

A collection of **20 high-speed, cloud-hosted REST APIs and Claude/Cursor MCP Servers** for extracting structured **JSON, CSV, and Excel** datasets from **SEC EDGAR (Form 4, 13F, N-PORT, 10-K/10-Q XBRL, 8-K, 13D/13G, S-1, Form 144, DEF 14A, 20-F/6-K, Form D)**, **US FDA & ClinicalTrials.gov**, **US Federal Government Contracts (DoD)**, and **Verified US B2B Healthcare & Banking Registries**.

Built and maintained by **[Mehdad DataLabs on Apify](https://apify.com/mehdad-datalabs)**.

---

## ⚡ Why Use These APIs Instead of Raw SEC/FDA Scraping?

- **Strips SEC XSLT Wrappers Automatically:** Parses raw `<nonDerivativeTransaction>`, `<infoTable>`, and `<invstOrSecur>` XML nodes into flat, ready-to-query JSON rows.
- **Standardized US-GAAP XBRL Normalization:** Converts messy 10-K and 10-Q XBRL tags into uniform financial statement columns (`revenueUsd`, `netIncomeUsd`, `netProfitMarginPct`, `epsDiluted`, `totalAssetsUsd`).
- **Zero SEC Rate-Limit Blocks or Proxy Fees:** Cloud-hosted on Apify with compliant headers and sub-5-second execution.
- **Native AI Agent (MCP) & n8n Support:** Plug any of the 20 endpoints directly into **Claude Desktop, Cursor, LangChain, Clay, Make, or n8n**.

---

## 🗂️ Complete 20-API Directory & Live Endpoints

### 1. Wall Street & SEC EDGAR Intelligence APIs (10 APIs)

| API Name | Actor ID (`mehdad-datalabs/...`) | Key Data Extracted | Live API & Playground |
| :--- | :--- | :--- | :--- |
| **SEC Form 4 Insider Trading XML API** | `sec-form-4-insider-trading-scraper-xml-parser-api` | CEO/CFO/Director buys (`P`) & sales (`S`), exact shares, price, total USD value | [Try API ↗](https://apify.com/mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api) |
| **SEC Form 13F Hedge Fund Whale API** | `sec-13f-institutional-holdings-hedge-fund-whale-scraper` | Berkshire Hathaway, Burry, Citadel 13F-HR XML holdings, portfolio weight %, Put/Call | [Try API ↗](https://apify.com/mehdad-datalabs/sec-13f-institutional-holdings-hedge-fund-whale-scraper) |
| **SEC Form N-PORT ETF & Mutual Fund API** | `sec-nport-etf-mutual-fund-holdings-xml-scraper` | Vanguard, BlackRock iShares & Fidelity ETF holdings, CUSIP, ISIN, net asset % | [Try API ↗](https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper) |
| **SEC 10-K & 10-Q XBRL Financials API** | `sec-10k-10q-xbrl-financial-statements-earnings-api` | Audited quarterly/annual Revenue, Net Income, Margin %, EPS, Cash Flow, Assets, Debt | [Try API ↗](https://apify.com/mehdad-datalabs/sec-10k-10q-xbrl-financial-statements-earnings-api) |
| **SEC Form 8-K Material Events & M&A API** | `sec-8k-corporate-events-ma-executive-change-scraper` | Decodes Item `5.02` CEO changes, `2.02` Earnings, `1.01/2.01` M&A, `1.05` Cyber breaches | [Try API ↗](https://apify.com/mehdad-datalabs/sec-8k-corporate-events-ma-executive-change-scraper) |
| **SEC Schedule 13D & 13G Activist API** | `sec-schedule-13d-13g-activist-investor-ownership-api` | Hostile takeover campaigns (`13D`), activist amendments (`13D/A`) & 5%+ whale stakes (`13G`) | [Try API ↗](https://apify.com/mehdad-datalabs/sec-schedule-13d-13g-activist-investor-ownership-api) |
| **SEC Form S-1 IPO & Form 144 Sale API** | `sec-ipo-s1-form144-insider-sale-scraper` | Rule 144 restricted stock dumps, `S-1/F-1` IPO filings, `S-3` dilution & `EFFECT` notices | [Try API ↗](https://apify.com/mehdad-datalabs/sec-ipo-s1-form144-insider-sale-scraper) |
| **SEC Form DEF 14A CEO Pay & Proxy API** | `sec-def14a-ceo-executive-compensation-proxy-scraper` | Annual proxy statements (`DEF 14A`), merger proxies (`DEFM14A`) & activist proxy fights | [Try API ↗](https://apify.com/mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper) |
| **SEC Form 20-F & 6-K Global ADR API** | `sec-20f-6k-foreign-adr-international-stock-scraper` | International & ADR stocks (`TSM`, `ASML`, `NVO`, `BABA`) annual `20-F` & monthly `6-K` filings | [Try API ↗](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper) |
| **SEC Form D Startup VC Funding API** | `sec-form-d-startup-funding-vc-b2b-lead-scraper` | Newly funded private startups, exact USD raised, Founder/CEO names, direct phones & HQ | [Try API ↗](https://apify.com/mehdad-datalabs/sec-form-d-startup-funding-vc-b2b-lead-scraper) |

---

### 2. Biotech, Pharma, MedTech & FDA Catalyst APIs (4 APIs)

| API Name | Actor ID (`mehdad-datalabs/...`) | Key Data Extracted | Live API & Playground |
| :--- | :--- | :--- | :--- |
| **FDA Drug Approvals (NDA/BLA/ANDA) API** | `fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper` | Official Drugs@FDA approvals, Priority Review status, active ingredients & sponsors | [Try API ↗](https://apify.com/mehdad-datalabs/fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper) |
| **ClinicalTrials.gov Phase 1-3 API** | `clinical-trials-biotech-catalyst-cro-b2b-lead-scraper` | Active Phase 1/2/3 trials, completion readout dates & study director contact emails/phones | [Try API ↗](https://apify.com/mehdad-datalabs/clinical-trials-biotech-catalyst-cro-b2b-lead-scraper) |
| **FDA 510(k) Medical Device Clearances API** | `fda-510k-medical-device-clearances-medtech-b2b-scraper` | Cleared medical devices, MedTech company names, named contact persons & HQ addresses | [Try API ↗](https://apify.com/mehdad-datalabs/fda-510k-medical-device-clearances-medtech-b2b-scraper) |
| **FDA Drug, Device & Food Recalls API** | `fda-product-recalls-safety-enforcement-b2b-scraper` | Class I, II & III FDA recalls, recalling manufacturers, defect reasons & unit quantities | [Try API ↗](https://apify.com/mehdad-datalabs/fda-product-recalls-safety-enforcement-b2b-scraper) |

---

### 3. B2B Lead Generation, GovCon & Banking APIs (6 APIs)

| API Name | Actor ID (`mehdad-datalabs/...`) | Key Data Extracted | Live API & Playground |
| :--- | :--- | :--- | :--- |
| **US Federal & DoD Contract Awards API** | `us-federal-government-contract-awards-dod-b2b-scraper` | Pentagon (DoD) & federal contract winners, obligated USD amounts & awarding agencies | [Try API ↗](https://apify.com/mehdad-datalabs/us-federal-government-contract-awards-dod-b2b-scraper) |
| **US Doctor, Dentist & Clinic B2B Leads API** | `us-doctor-dentist-clinic-healthcare-b2b-lead-scraper` | Verified physicians, dentists & clinics with Clinic Owner name, direct phone & license | [Try API ↗](https://apify.com/mehdad-datalabs/us-doctor-dentist-clinic-healthcare-b2b-lead-scraper) |
| **US Pharmacy, Clinical Lab & DME Leads API** | `us-pharmacy-medical-lab-dme-b2b-lead-scraper` | Independent pharmacies, diagnostic labs & DME suppliers with Owner direct phone & DBA | [Try API ↗](https://apify.com/mehdad-datalabs/us-pharmacy-medical-lab-dme-b2b-lead-scraper) |
| **FDIC US Bank Directory & Financials API** | `fdic-us-bank-directory-deposits-assets-b2b-scraper` | Active US commercial/community banks, Total Assets, Deposits, ROA/ROE %, branches & URL | [Try API ↗](https://apify.com/mehdad-datalabs/fdic-us-bank-directory-deposits-assets-b2b-scraper) |
| **CFPB Fintech & Bank Complaints API** | `cfpb-fintech-bank-consumer-complaint-b2b-scraper` | Consumer disputes & regulatory risk disclosures for Coinbase, Robinhood, PayPal & banks | [Try API ↗](https://apify.com/mehdad-datalabs/cfpb-fintech-bank-consumer-complaint-b2b-scraper) |
| **US Public Company B2B Enrichment API** | `us-public-company-b2b-profile-sic-hq-phone-scraper` | Enriches stock tickers with Corporate HQ Phone, Street Address, IRS EIN Tax ID & SIC code | [Try API ↗](https://apify.com/mehdad-datalabs/us-public-company-b2b-profile-sic-hq-phone-scraper) |

---

## 🐍 Python Quickstart (`quickstart.py`)

Install the official Apify Python client:

```bash
pip install apify-client pandas
Run any of the 20 APIs in 10 lines of Python (get your free API token at console.apify.com/settings/integrations):
Python
from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your Apify API token
client = ApifyClient("YOUR_APIFY_API_TOKEN")

# Example 1: Extract real-time SEC Form 4 CEO & Director Insider Stock Buys
run = client.actor("mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api").call(
    run_input={
        "tickers": ["NVDA", "AAPL", "MSFT", "PLTR"],
        "transactionCodes": ["P", "S"],
        "minDollarValue": 50000,
        "maxFilingsPerTicker": 15,
    }
)

# Fetch the parsed JSON records into a Pandas DataFrame
items = client.dataset(run["defaultDatasetId"]).list_items().items
df = pd.DataFrame(items)
print(df[["ticker", "filingDate", "insiderName", "insiderRole", "transactionCode", "totalDollarValue"]])
df.to_csv("sec_form4_insider_trades.csv", index=False)
🤖 Using with Claude Desktop & Cursor (MCP Server)
All 20 Actors support Apify's Model Context Protocol (MCP) server out of the box. You can connect Claude Desktop or Cursor directly to these tools using @apify/actors-mcp-server:
JSON
{
  "mcpServers": {
    "sec-and-b2b-intelligence": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api,mehdad-datalabs/sec-13f-institutional-holdings-hedge-fund-whale-scraper,mehdad-datalabs/sec-10k-10q-xbrl-financial-statements-earnings-api,mehdad-datalabs/sec-form-d-startup-funding-vc-b2b-lead-scraper"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_API_TOKEN"
      }
    }
  }
}
📄 License & Support
MIT License. Built by Mehdad DataLabs. Open an issue in this repository or on the Apify Actor page if you need additional SEC forms or custom B2B fields!
