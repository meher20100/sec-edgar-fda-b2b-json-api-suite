# Automating CEO Compensation, Board Elections & Merger Proxies (SEC Form DEF 14A) in Python & Claude MCP (Nov 15, 2026)

**Read on Dev.to:** [https://dev.to/mehdadsharifi/automating-ceo-compensation-board-elections-merger-proxies-sec-form-def-14a-in-python-claude-1pba](https://dev.to/mehdadsharifi/automating-ceo-compensation-board-elections-merger-proxies-sec-form-def-14a-in-python-claude-1pba)

Extracting and normalizing **CEO Compensation, Board Elections & Merger Proxies (SEC Form DEF 14A)** is one of the highest-leverage data pipelines for quantitative researchers, B2B growth engineers, and AI agent builders—especially for **benchmarking C-suite executive compensation, golden parachutes (DEFM14A), and activist proxy fights**.

Instead of maintaining fragile local parsers or proxy networks, you can pull structured **JSON, CSV, or Excel** datasets in seconds using the **[SEC DEF 14A Executive Compensation & Proxy Statement API](https://apify.com/mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper)** by **Mehdad DataLabs**.

---

## Live Market & Regulatory Activity Snapshot (Nov 15, 2026)

Here is a live sample of recent activity across tracked benchmark tickers (NVDA, AAPL, TSLA, MSFT):

**1. NVIDIA CORP (NVDA)** — Industry: Semiconductors & Related Devices | Latest Filing: Form 8-K (Filed: 2026-11-12)

**2. Apple Inc. (AAPL)** — Industry: Electronic Computers | Latest Filing: Form 4 (Filed: 2026-11-12)

**3. Tesla, Inc. (TSLA)** — Industry: Motor Vehicles & Passenger Car Bodies | Latest Filing: Form 10-Q (Filed: 2026-10-22)

**4. MICROSOFT CORP (MSFT)** — Industry: Services-Prepackaged Software | Latest Filing: Form 4 (Filed: 2026-11-12)

---

## Quickstart: Run This API in Python (apify-client)

Install the official Python client:

```bash
pip install apify-client pandas
```

Call the **[SEC DEF 14A Executive Compensation & Proxy Statement API](https://apify.com/mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper)** endpoint directly from Python:

```python
from apify_client import ApifyClient
import pandas as pd

client = ApifyClient("YOUR_APIFY_API_TOKEN")

# Run the Actor and wait for results
run = client.actor("mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper").call()

# Load clean JSON records into a Pandas DataFrame
items = client.dataset(run["defaultDatasetId"]).list_items().items
df = pd.DataFrame(items)
print(df.head())
```

---

## Connect Directly to Claude Desktop, Cursor (MCP) & n8n

This Actor is natively compatible with Apify's **Model Context Protocol (MCP)** server (`@apify/actors-mcp-server`). You can also trigger it on a daily schedule inside **n8n, Make, Clay, or Zapier** to route real-time alerts into Slack, Telegram, HubSpot, or Google Sheets.

**1. Live API Playground:** [SEC DEF 14A Executive Compensation & Proxy Statement API](https://apify.com/mehdad-datalabs/sec-def14a-ceo-executive-compensation-proxy-scraper)

**2. Related API:** [SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API](https://apify.com/mehdad-datalabs/sec-20f-6k-foreign-adr-international-stock-scraper)

**3. Related API:** [US Federal Government Contract Awards & DoD B2B Lead Scraper](https://apify.com/mehdad-datalabs/us-federal-government-contract-awards-dod-b2b-scraper)

**4. Open-Source Python SDK & Full 41-API Directory on GitHub:** [https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite](https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite)

---

## Complete 41-API Directory

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

**21.** [Shopify Store Spy, Product Catalog & Price Scraper API](https://apify.com/mehdad-datalabs/shopify-store-spy-product-catalog-price-b2b-scraper)

**22.** [Greenhouse & Lever Tech Jobs & B2B Hiring Intent API](https://apify.com/mehdad-datalabs/greenhouse-lever-tech-jobs-hiring-intent-b2b-scraper)

**23.** [B2B Website Email, Phone, Social Links & Tech Stack API](https://apify.com/mehdad-datalabs/b2b-website-email-phone-social-links-tech-stack-scraper)

**24.** [Y Combinator (YC) Startup Directory & B2B Lead Scraper API](https://apify.com/mehdad-datalabs/y-combinator-yc-startup-directory-b2b-lead-scraper)

**25.** [Tech Startup Launches (Show HN) & Hiring B2B Lead API](https://apify.com/mehdad-datalabs/tech-startup-launches-hackernews-b2b-lead-scraper)

**26.** [B2B Podcast Host Email, Guest & Sponsorship Lead API](https://apify.com/mehdad-datalabs/b2b-podcast-host-email-guest-sponsorship-lead-scraper)

**27.** [GitHub AI & DevTools Repo & Developer B2B Lead API](https://apify.com/mehdad-datalabs/github-ai-devtools-repo-developer-b2b-lead-scraper)

**28.** [AI & Biotech R&D Scientist, Lab & Author B2B Lead API](https://apify.com/mehdad-datalabs/ai-biotech-research-scientist-lab-b2b-lead-scraper)

**29.** [Polymarket Live Odds, Volume & Arbitrage Prediction API](https://apify.com/mehdad-datalabs/polymarket-live-odds-volume-arbitrage-prediction-api)

**30.** [DeFi Protocol TVL, Crypto Liquidity & Web3 B2B Lead API](https://apify.com/mehdad-datalabs/defi-protocol-tvl-crypto-whale-web3-b2b-lead-scraper)

**31.** [Cursor Directory Scraper — Plugins, MCPs, Rules & AI Leads](https://apify.com/mehdad-datalabs/cursor-directory-plugins-mcp-rules-b2b-scraper)

**32.** [Cline & Roo Code MCP Marketplace Scraper & AI Leads API](https://apify.com/mehdad-datalabs/cline-mcp-marketplace-ai-plugins-scraper)

**33.** [LobeHub MCP & AI Agent Plugins Directory Scraper API](https://apify.com/mehdad-datalabs/lobehub-mcp-ai-agent-plugins-scraper)

**34.** [Dify AI Marketplace & Plugin Catalog Scraper API](https://apify.com/mehdad-datalabs/dify-ai-marketplace-plugins-catalog-scraper)

**35.** [Activepieces Automation Pieces & Integrations Scraper API](https://apify.com/mehdad-datalabs/activepieces-automation-pieces-actions-scraper)

**36.** [Composio AI Agent Toolkits & Integrations Scraper API](https://apify.com/mehdad-datalabs/composio-ai-agent-toolkits-actions-scraper)

**37.** [Dune Analytics Trending Dashboards & Web3 Queries API](https://apify.com/mehdad-datalabs/dune-analytics-web3-dashboards-queries-scraper)

**38.** [Make.com Automation Templates & App Integrations API](https://apify.com/mehdad-datalabs/make-com-automation-templates-integrations-scraper)

**39.** [Vercel Templates & Next.js AI Starter Ecosystem API](https://apify.com/mehdad-datalabs/vercel-templates-nextjs-starter-ecosystem-scraper)

**40.** [Langflow & Flowise AI Agent Workflow Templates API](https://apify.com/mehdad-datalabs/langflow-flowise-ai-agent-templates-scraper)

**41.** [Supabase Ecosystem Partners & Tech Integrations B2B API](https://apify.com/mehdad-datalabs/supabase-ecosystem-partners-integrations-b2b-scraper)
