# Automating International ADR Stocks & Semiconductor Monthly Revenue (SEC Form 20-F & 6-K) in Python & Claude MCP (Nov 09, 2026)

**Read on Dev.to:** [https://dev.to/mehdadsharifi/automating-international-adr-stocks-semiconductor-monthly-revenue-sec-form-20-f-6-k-in-python-2bba-temp-slug-6991002](https://dev.to/mehdadsharifi/automating-international-adr-stocks-semiconductor-monthly-revenue-sec-form-20-f-6-k-in-python-2bba-temp-slug-6991002)

Extracting and normalizing **International ADR Stocks & Semiconductor Monthly Revenue (SEC Form 20-F & 6-K)** is one of the highest-leverage data pipelines for quantitative researchers, B2B growth engineers, and AI agent builders—especially for **tracking TSMC monthly wafer revenue, ASML earnings, and Novo Nordisk updates on Forms 20-F and 6-K**.

Instead of maintaining fragile local XSLT/XML parsers or proxy networks, you can pull structured **JSON, CSV, or Excel** datasets in seconds using the **[SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper)** by **Mehdad DataLabs**.

---

## Live SEC EDGAR Activity Snapshot (Nov 09, 2026)

Here is a live sample of recent regulatory activity across tracked benchmark tickers (TSM, ASML, NVO, BABA):

**1. TAIWAN SEMICONDUCTOR MANUFACTURING CO LTD (TSM)** — Industry: Semiconductors & Related Devices | Latest Filing: Form 4 (Filed: 2026-11-09)

**2. ASML HOLDING NV (ASML)** — Industry: Special Industry Machinery, NEC | Latest Filing: Form 6-K (Filed: 2026-10-14)

**3. NOVO NORDISK A S (NVO)** — Industry: Pharmaceutical Preparations | Latest Filing: Form 6-K (Filed: 2026-11-09)

**4. Alibaba Group Holding Ltd (BABA)** — Industry: Services-Business Services, NEC | Latest Filing: Form 6-K (Filed: 2026-11-06)

---

## Quickstart: Run This API in Python (apify-client)

Install the official Python client:

```bash
pip install apify-client pandas
```

Call the **[SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper)** endpoint directly from Python:

```python
from apify_client import ApifyClient
import pandas as pd

client = ApifyClient("YOUR_APIFY_API_TOKEN")

# Run the Actor and wait for results
run = client.actor("mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper").call()

# Load clean JSON records into a Pandas DataFrame
items = client.dataset(run["defaultDatasetId"]).list_items().items
df = pd.DataFrame(items)
print(df.head())
```

---

## Connect Directly to Claude Desktop, Cursor (MCP) & n8n

This Actor is natively compatible with Apify's **Model Context Protocol (MCP)** server (`@apify/actors-mcp-server`). You can also trigger it on a daily schedule inside **n8n, Make, Clay, or Zapier** to route real-time alerts into Slack, Telegram, HubSpot, or Google Sheets.

**1. Live API Playground:** [SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper)

**2. Related API:** [US Federal Government Contract Awards & DoD B2B Lead Scraper](https://apify.com/mehdad-datalabs/us-federal-government-contract-awards-dod-b2b-scraper)

**3. Related API:** [FDA Drug Approvals, NDA/BLA Biotech Catalyst & Pharma API](https://apify.com/mehdad-datalabs/fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper)

**4. Open-Source Python SDK & Full 20-API Directory on GitHub:** [https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite](https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite)

---

## Complete 20-API Directory

**1.** [SEC Form 4 Insider Trading Scraper & XML Parser API](https://apify.com/mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api)

**2.** [SEC Form 13F Institutional Holdings & Hedge Fund Whale Scraper](https://apify.com/mehdad-datalabs/sec-13f-institutional-holdings-hedge-fund-whale-scraper)

**3.** [SEC Form 8-K Corporate Events, M&A & Executive Change Scraper](https://apify.com/mehdad-datalabs/sec-8k-corporate-events-ma-executive-change-scraper)

**4.** [SEC 10-K & 10-Q XBRL Financial Statements & Earnings API](https://apify.com/mehdad-datalabs/sec-10k-10q-xbrl-financial-statements-earnings-api)

**5.** [SEC Schedule 13D & 13G Activist Investor & 5%+ Ownership API](https://apify.com/mehdad-datalabs/sec-schedule-13d-13g-activist-investor-ownership-api)

**6.** [SEC Form S-1 IPO Pipeline & Form 144 Insider Sale Notice API](https://apify.com/mehdad-datalabs/sec-ipo-s1-form144-insider-sale-scraper)

**7.** [SEC Form D Startup Funding, VC Raise & Founder B2B Lead API](https://apify.com/mehdad-datalabs/sec-form-d-startup-funding-vc-b2b-lead-scraper)

**8.** [SEC Form N-PORT Mutual Fund & ETF Portfolio Holdings API](https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper)

**9.** [SEC DEF 14A Executive Compensation & Proxy Statement API](https://apify.com/mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper)

**10.** [SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper)

**11.** [US Federal Government Contract Awards & DoD B2B Lead Scraper](https://apify.com/mehdad-datalabs/us-federal-government-contract-awards-dod-b2b-scraper)

**12.** [FDA Drug Approvals, NDA/BLA Biotech Catalyst & Pharma API](https://apify.com/mehdad-datalabs/fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper)

**13.** [ClinicalTrials.gov Phase 1-3 Biotech Catalyst & B2B Lead API](https://apify.com/mehdad-datalabs/clinical-trials-biotech-catalyst-cro-b2b-lead-scraper)

**14.** [FDA 510(k) Medical Device Clearances & MedTech B2B Lead API](https://apify.com/mehdad-datalabs/fda-510k-medical-device-clearances-medtech-b2b-scraper)

**15.** [FDA Drug, Device & Food Recall Enforcement & Legal Lead API](https://apify.com/mehdad-datalabs/fda-product-recalls-safety-enforcement-b2b-scraper)

**16.** [US Doctor, Dentist & Medical Clinic B2B Lead Scraper API](https://apify.com/mehdad-datalabs/us-doctor-dentist-clinic-healthcare-b2b-lead-scraper)

**17.** [US Pharmacy, Clinical Lab & Medical Supply B2B Lead API](https://apify.com/mehdad-datalabs/us-pharmacy-medical-lab-dme-b2b-lead-scraper)

**18.** [FDIC US Bank Directory, Deposits, Assets & B2B Lead API](https://apify.com/mehdad-datalabs/fdic-us-bank-directory-deposits-assets-b2b-scraper)

**19.** [CFPB Fintech & Bank Consumer Complaint Intelligence API](https://apify.com/mehdad-datalabs/cfpb-fintech-bank-consumer-complaint-b2b-scraper)

**20.** [US Public Company B2B Directory, SIC & HQ Phone API](https://apify.com/mehdad-datalabs/us-public-company-b2b-profile-sic-hq-phone-scraper)
