# How to Automate Monthly ETF & Mutual Fund Portfolio Holdings (SEC Form N-PORT) in Python, n8n & Claude MCP (Nov 07, 2026)

**Read on Dev.to:** [https://dev.to/mehdadsharifi/how-to-automate-monthly-etf-mutual-fund-portfolio-holdings-sec-form-n-port-in-python-n8n--4n1h](https://dev.to/mehdadsharifi/how-to-automate-monthly-etf-mutual-fund-portfolio-holdings-sec-form-n-port-in-python-n8n--4n1h)

Extracting and normalizing **Monthly ETF & Mutual Fund Portfolio Holdings (SEC Form N-PORT)** is one of the highest-leverage data pipelines for quantitative researchers, B2B growth engineers, and AI agent builders—especially for **parsing Vanguard, BlackRock iShares, and Fidelity ETF holdings XML tables with ISINs, CUSIPs, and exact net asset weights**.

Instead of maintaining fragile local scrapers, XSLT parsers, or expensive proxy networks, you can pull clean, structured **JSON, CSV, or Excel** datasets in under 5 seconds using the **[SEC Form N-PORT Mutual Fund & ETF Portfolio Holdings API](https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper)** by **Mehdad DataLabs**.

---

## Live Market & Regulatory Snapshot (Nov 07, 2026)

Here is a live sample of recent SEC EDGAR activity across tracked benchmark tickers (`NVDA, AAPL, MSFT, AMZN`):

| Ticker | Company Name | Industry / SIC | Latest SEC Form | Filing Date | Verified Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `NVDA` | NVIDIA CORP | Semiconductors & Related Devices | `4` | 2026-11-06 | [View Filing](https://www.sec.gov/Archives/edgar/data/1045810/000119764726000013/0001197647-26-000013-index.htm) |
| `AAPL` | Apple Inc. | Electronic Computers | `4` | 2026-11-05 | [View Filing](https://www.sec.gov/Archives/edgar/data/320193/000114036126042149/0001140361-26-042149-index.htm) |
| `MSFT` | MICROSOFT CORP | Services-Prepackaged Software | `144` | 2026-11-05 | [View Filing](https://www.sec.gov/Archives/edgar/data/789019/000195917326007778/0001959173-26-007778-index.htm) |
| `AMZN` | AMAZON COM INC | Retail-Catalog & Mail-Order Houses | `4` | 2026-11-04 | [View Filing](https://www.sec.gov/Archives/edgar/data/1018724/000193600626000028/0001936006-26-000028-index.htm) |

---

## Quickstart: Run This API in Python (`apify-client`)

Install the official client:

    pip install apify-client pandas

Call the **[SEC Form N-PORT Mutual Fund & ETF Portfolio Holdings API](https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper)** endpoint directly from Python:

    from apify_client import ApifyClient
    import pandas as pd

    client = ApifyClient("YOUR_APIFY_API_TOKEN")

    # Run the Actor and wait for results
    run = client.actor("mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper").call()

    # Load clean JSON records into a Pandas DataFrame
    items = client.dataset(run["defaultDatasetId"]).list_items().items
    df = pd.DataFrame(items)
    print(df.head())

---

## Connect Directly to Claude Desktop, Cursor (MCP) & n8n

This Actor is natively compatible with Apify's **Model Context Protocol (MCP)** server (`@apify/actors-mcp-server`). You can also trigger it on a daily schedule inside **n8n, Make, Clay, or Zapier** to route real-time alerts into Slack, Telegram, HubSpot, or Google Sheets.

- **Try the Live API Playground:** [https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper](https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper)
- **Open-Source Python SDK & Examples on GitHub:** [https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite](https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite)

---

## Explore the Full 20-API Financial, Biotech & B2B Intelligence Suite

- [SEC Form 4 Insider Trading Scraper & XML Parser API](https://apify.com/mehdad-datalabs/sec-form-4-insider-trading-scraper-xml-parser-api)
- [SEC Form 13F Institutional Holdings & Hedge Fund Whale Scraper](https://apify.com/mehdad-datalabs/sec-13f-institutional-holdings-hedge-fund-whale-scraper)
- [SEC Form 8-K Corporate Events, M&A & Executive Change Scraper](https://apify.com/mehdad-datalabs/sec-8k-corporate-events-ma-executive-change-scraper)
- [SEC 10-K & 10-Q XBRL Financial Statements & Earnings API](https://apify.com/mehdad-datalabs/sec-10k-10q-xbrl-financial-statements-earnings-api)
- [SEC Schedule 13D & 13G Activist Investor & 5%+ Ownership API](https://apify.com/mehdad-datalabs/sec-schedule-13d-13g-activist-investor-ownership-api)
- [SEC Form S-1 IPO Pipeline & Form 144 Insider Sale Notice API](https://apify.com/mehdad-datalabs/sec-ipo-s1-form144-insider-sale-scraper)
- [SEC Form D Startup Funding, VC Raise & Founder B2B Lead API](https://apify.com/mehdad-datalabs/sec-form-d-startup-funding-vc-b2b-lead-scraper)
- [SEC Form N-PORT Mutual Fund & ETF Portfolio Holdings API](https://apify.com/mehdad-datalabs/sec-nport-etf-mutual-fund-holdings-xml-scraper)
- [SEC DEF 14A Executive Compensation & Proxy Statement API](https://apify.com/mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper)
- [SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper)
- [US Federal Government Contract Awards & DoD B2B Lead Scraper](https://apify.com/mehdad-datalabs/us-federal-government-contract-awards-dod-b2b-scraper)
- [FDA Drug Approvals, NDA/BLA Biotech Catalyst & Pharma API](https://apify.com/mehdad-datalabs/fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper)
- [ClinicalTrials.gov Phase 1-3 Biotech Catalyst & B2B Lead API](https://apify.com/mehdad-datalabs/clinical-trials-biotech-catalyst-cro-b2b-lead-scraper)
- [FDA 510(k) Medical Device Clearances & MedTech B2B Lead API](https://apify.com/mehdad-datalabs/fda-510k-medical-device-clearances-medtech-b2b-scraper)
- [FDA Drug, Device & Food Recall Enforcement & Legal Lead API](https://apify.com/mehdad-datalabs/fda-product-recalls-safety-enforcement-b2b-scraper)
- [US Doctor, Dentist & Medical Clinic B2B Lead Scraper API](https://apify.com/mehdad-datalabs/us-doctor-dentist-clinic-healthcare-b2b-lead-scraper)
- [US Pharmacy, Clinical Lab & Medical Supply B2B Lead API](https://apify.com/mehdad-datalabs/us-pharmacy-medical-lab-dme-b2b-lead-scraper)
- [FDIC US Bank Directory, Deposits, Assets & B2B Lead API](https://apify.com/mehdad-datalabs/fdic-us-bank-directory-deposits-assets-b2b-scraper)
- [CFPB Fintech & Bank Consumer Complaint Intelligence API](https://apify.com/mehdad-datalabs/cfpb-fintech-bank-consumer-complaint-b2b-scraper)
- [US Public Company B2B Directory, SIC & HQ Phone API](https://apify.com/mehdad-datalabs/us-public-company-b2b-profile-sic-hq-phone-scraper)
