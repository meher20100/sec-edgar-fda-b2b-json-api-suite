import os
import json
import datetime
import urllib.request

DEVTO_API_KEY = os.getenv("DEVTO_API_KEY", "").strip()

SEC_HEADERS = {
    "User-Agent": "MehdadDataLabsBot support@mehdaddatalabs.io",
    "Accept": "application/json",
}

ACTORS_ROTATION = [
    {
        "slug": "sec-form-4-insider-trading-scraper-xml-parser-api",
        "name": "SEC Form 4 Insider Trading Scraper & XML Parser API",
        "topic": "CEO & CFO Insider Stock Trading (SEC Form 4 XML)",
        "tags": ["python", "finance", "api", "ai"],
        "tickers": ["NVDA", "AAPL", "MSFT", "PLTR", "TSLA"],
        "use_case": "tracking real-time C-suite open-market stock purchases (Code P) and sales (Code S) before retail news coverage",
    },
    {
        "slug": "sec-13f-institutional-holdings-hedge-fund-whale-scraper",
        "name": "SEC Form 13F Institutional Holdings & Hedge Fund Whale Scraper",
        "topic": "Institutional Hedge Fund & Whale Portfolio Filings (SEC Form 13F-HR)",
        "tags": ["finance", "python", "api", "data"],
        "tickers": ["BRK-A", "BLK", "NVDA", "MSFT"],
        "use_case": "extracting quarterly institutional holdings, CUSIPs, portfolio weights (%), and Put/Call option positions",
    },
    {
        "slug": "sec-8k-corporate-events-ma-executive-change-scraper",
        "name": "SEC Form 8-K Corporate Events, M&A & Executive Change Scraper",
        "topic": "Breaking Corporate Catalysts, M&A & CEO Changes (SEC Form 8-K)",
        "tags": ["api", "python", "finance", "automation"],
        "tickers": ["AAPL", "NVDA", "META", "AMZN", "CRM"],
        "use_case": "decoding Item 5.02 executive appointments, Item 2.02 earnings releases, and Item 1.01 M&A agreements",
    },
    {
        "slug": "sec-10k-10q-xbrl-financial-statements-earnings-api",
        "name": "SEC 10-K & 10-Q XBRL Financial Statements & Earnings API",
        "topic": "Audited US-GAAP XBRL Financial Statements (SEC Form 10-K & 10-Q)",
        "tags": ["python", "finance", "ai", "api"],
        "tickers": ["MSFT", "NVDA", "GOOGL", "AAPL"],
        "use_case": "normalizing quarterly and annual Revenue, Net Income, Diluted EPS, Cash Flow, and Balance Sheet metrics",
    },
    {
        "slug": "sec-schedule-13d-13g-activist-investor-ownership-api",
        "name": "SEC Schedule 13D & 13G Activist Investor & 5%+ Ownership API",
        "topic": "Activist Hedge Fund Takeovers & 5%+ Whale Stakes (Schedule 13D & 13G)",
        "tags": ["finance", "python", "api", "trading"],
        "tickers": ["DIS", "INTC", "PYPL", "CRM"],
        "use_case": "monitoring hostile takeover campaigns (Schedule 13D) and 5%+ institutional block accumulations (Schedule 13G)",
    },
    {
        "slug": "sec-ipo-s1-form144-insider-sale-scraper",
        "name": "SEC Form S-1 IPO Pipeline & Form 144 Insider Sale Notice API",
        "topic": "Pre-IPO Tech Registrations & Rule 144 Restricted Stock Sales (Form S-1 & 144)",
        "tags": ["finance", "python", "api", "startups"],
        "tickers": ["PLTR", "RDDT", "ARM", "NVDA"],
        "use_case": "catching Rule 144 founder/VC proposed restricted stock sales and Form S-1/S-3 dilution filings early",
    },
    {
        "slug": "sec-form-d-startup-funding-vc-b2b-lead-scraper",
        "name": "SEC Form D Startup Funding, VC Raise & Founder B2B Lead API",
        "topic": "Newly Funded Startups & Venture Capital Raises (SEC Form D XML)",
        "tags": ["startups", "b2b", "api", "python"],
        "tickers": ["NVDA", "PLTR", "CRM", "SNOW"],
        "use_case": "extracting newly funded private startups, exact dollar amounts raised, and Founder/CEO contact names",
    },
    {
        "slug": "sec-nport-etf-mutual-fund-holdings-xml-scraper",
        "name": "SEC Form N-PORT Mutual Fund & ETF Portfolio Holdings API",
        "topic": "Monthly ETF & Mutual Fund Portfolio Holdings (SEC Form N-PORT)",
        "tags": ["finance", "python", "api", "etf"],
        "tickers": ["NVDA", "AAPL", "MSFT", "AMZN"],
        "use_case": "parsing Vanguard, BlackRock iShares, and Fidelity ETF holdings XML tables with ISINs and CUSIPs",
    },
    {
        "slug": "sec-def14a-ceo-executive-compensation-proxy-scraper",
        "name": "SEC DEF 14A Executive Compensation & Proxy Statement API",
        "topic": "CEO Compensation, Board Elections & Merger Proxies (SEC Form DEF 14A)",
        "tags": ["finance", "api", "python", "governance"],
        "tickers": ["NVDA", "AAPL", "TSLA", "MSFT"],
        "use_case": "benchmarking C-suite executive compensation, golden parachutes (DEFM14A), and activist proxy fights",
    },
    {
        "slug": "sec-20f-6k-foreign-adr-international-stock-scraper",
        "name": "SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API",
        "topic": "International ADR Stocks & Semiconductor Monthly Revenue (SEC Form 20-F & 6-K)",
        "tags": ["finance", "python", "api", "global"],
        "tickers": ["TSM", "ASML", "NVO", "BABA"],
        "use_case": "tracking TSMC monthly wafer revenue, ASML earnings, and Novo Nordisk updates on Forms 20-F and 6-K",
    },
    {
        "slug": "us-federal-government-contract-awards-dod-b2b-scraper",
        "name": "US Federal Government Contract Awards & DoD B2B Lead Scraper",
        "topic": "Pentagon (DoD) & US Federal Government Contract Winners (GovCon API)",
        "tags": ["govtech", "b2b", "api", "python"],
        "tickers": ["PLTR", "LMT", "BAH", "LDOS"],
        "use_case": "identifying newly funded defense, AI, and cybersecurity federal contractors for B2B subcontracting outreach",
    },
    {
        "slug": "fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper",
        "name": "FDA Drug Approvals, NDA/BLA Biotech Catalyst & Pharma API",
        "topic": "US FDA New Drug (NDA) & Biologics (BLA) Biotech Catalysts",
        "tags": ["biotech", "healthcare", "api", "python"],
        "tickers": ["LLY", "NVO", "PFE", "VRTX"],
        "use_case": "tracking FDA NDA, BLA, and ANDA drug approvals, Priority Review designations, and pharma sponsors",
    },
    {
        "slug": "clinical-trials-biotech-catalyst-cro-b2b-lead-scraper",
        "name": "ClinicalTrials.gov Phase 1-3 Biotech Catalyst & B2B Lead API",
        "topic": "Phase 1, 2 & 3 Clinical Trial Readout Catalysts & CRO B2B Leads",
        "tags": ["biotech", "healthcare", "python", "api"],
        "tickers": ["LLY", "MRNA", "VRTX", "REGN"],
        "use_case": "extracting active recruiting clinical trials, primary completion readout dates, and study contact emails/phones",
    },
    {
        "slug": "fda-510k-medical-device-clearances-medtech-b2b-scraper",
        "name": "FDA 510(k) Medical Device Clearances & MedTech B2B Lead API",
        "topic": "US FDA 510(k) Medical Device Clearances & MedTech B2B Contacts",
        "tags": ["medtech", "healthcare", "api", "python"],
        "tickers": ["ISRG", "MDT", "ABT", "SYK"],
        "use_case": "capturing newly cleared medical devices along with the MedTech Applicant Company Name and Contact Person",
    },
    {
        "slug": "fda-product-recalls-safety-enforcement-b2b-scraper",
        "name": "FDA Drug, Device & Food Recall Enforcement & Legal Lead API",
        "topic": "FDA Class I, II & III Product Recalls & Mass-Tort Litigation Leads",
        "tags": ["healthcare", "legaltech", "api", "python"],
        "tickers": ["ABT", "BAX", "MDT", "PFE"],
        "use_case": "monitoring critical Class I medical device, pharmaceutical, and food safety recalls for law firms and QA teams",
    },
    {
        "slug": "us-doctor-dentist-clinic-healthcare-b2b-lead-scraper",
        "name": "US Doctor, Dentist & Medical Clinic B2B Lead Scraper API",
        "topic": "Verified US Doctors, Dentists & Medical Clinics B2B Lead Generation (CMS NPI)",
        "tags": ["b2b", "healthcare", "api", "python"],
        "tickers": ["UNH", "HCA", "CVS", "ELV"],
        "use_case": "extracting NPI-2 dental and medical clinics with Clinic Owner / Authorized Official names and direct phones",
    },
    {
        "slug": "us-pharmacy-medical-lab-dme-b2b-lead-scraper",
        "name": "US Pharmacy, Clinical Lab & Medical Supply B2B Lead API",
        "topic": "Independent US Pharmacies, Diagnostic Labs & DME Suppliers B2B Leads",
        "tags": ["b2b", "healthcare", "python", "api"],
        "tickers": ["MCK", "COR", "CAH", "LH"],
        "use_case": "building verified outbound lists of independent pharmacies and clinical labs with Owner direct phones",
    },
    {
        "slug": "fdic-us-bank-directory-deposits-assets-b2b-scraper",
        "name": "FDIC US Bank Directory, Deposits, Assets & B2B Lead API",
        "topic": "US Commercial & Community Bank Directory, Assets, Deposits & ROA/ROE",
        "tags": ["fintech", "banking", "api", "python"],
        "tickers": ["JPM", "BAC", "WFC", "C"],
        "use_case": "filtering every FDIC-insured community and regional bank by total assets ($), deposits ($), and ROA/ROE %",
    },
    {
        "slug": "cfpb-fintech-bank-consumer-complaint-b2b-scraper",
        "name": "CFPB Fintech & Bank Consumer Complaint Intelligence API",
        "topic": "Fintech, Crypto & Bank Consumer Complaint & Regulatory Risk Intelligence",
        "tags": ["fintech", "crypto", "api", "python"],
        "tickers": ["COIN", "HOOD", "PYPL", "SOFI"],
        "use_case": "tracking consumer fraud, account-freeze disputes, and regulatory risk disclosures across fintechs and banks",
    },
    {
        "slug": "us-public-company-b2b-profile-sic-hq-phone-scraper",
        "name": "US Public Company B2B Directory, SIC & HQ Phone API",
        "topic": "US Public Company B2B CRM Enrichment (Corporate HQ Phone, EIN Tax ID & SIC)",
        "tags": ["b2b", "api", "python", "automation"],
        "tickers": ["NVDA", "AAPL", "MSFT", "PLTR", "CRM"],
        "use_case": "enriching NYSE and Nasdaq enterprise accounts in Clay or n8n with verified Corporate HQ phones, EINs, and SIC codes",
    },
    {
        "slug": "shopify-store-spy-product-catalog-price-b2b-scraper",
        "name": "Shopify Store Spy, Product Catalog & Price Scraper API",
        "topic": "Shopify Product Catalog, Pricing & Competitor Monitoring",
        "tags": ["ecommerce", "shopify", "python", "api"],
        "tickers": ["SHOP", "AMZN", "AAPL", "NVDA"],
        "use_case": "extracting complete Shopify product catalogs, compare-at discounts %, SKUs, and live stock status",
    },
    {
        "slug": "greenhouse-lever-tech-jobs-hiring-intent-b2b-scraper",
        "name": "Greenhouse & Lever Tech Jobs & B2B Hiring Intent API",
        "topic": "Greenhouse & Lever ATS Tech Jobs & B2B Hiring Intent Signals",
        "tags": ["b2b", "jobs", "python", "api"],
        "tickers": ["CRM", "NOW", "WDAY", "SNOW"],
        "use_case": "tracking live engineering and sales job requisitions to detect B2B buying intent in Clay and n8n",
    },
    {
        "slug": "b2b-website-email-phone-social-links-tech-stack-scraper",
        "name": "B2B Website Email, Phone, Social Links & Tech Stack API",
        "topic": "B2B Domain Contact Enrichment & Website Tech Stack Fingerprinting",
        "tags": ["b2b", "marketing", "python", "api"],
        "tickers": ["HUBS", "CRM", "NET", "DDOG"],
        "use_case": "enriching company domains with verified emails, phone numbers, LinkedIn/X links, and detected tech stacks",
    },
    {
        "slug": "y-combinator-yc-startup-directory-b2b-lead-scraper",
        "name": "Y Combinator (YC) Startup Directory & B2B Lead Scraper API",
        "topic": "Y Combinator (YC) Startup Directory, Batch & Hiring B2B Leads",
        "tags": ["startups", "b2b", "python", "api"],
        "tickers": ["COIN", "ABNB", "RDDT", "DASH"],
        "use_case": "filtering funded YC startups by batch, industry, team size, and active hiring status for outbound sales",
    },
    {
        "slug": "tech-startup-launches-hackernews-b2b-lead-scraper",
        "name": "Tech Startup Launches (Show HN) & Hiring B2B Lead API",
        "topic": "Hacker News Show HN & Launch HN Tech Startup Lead Discovery",
        "tags": ["startups", "devtools", "python", "api"],
        "tickers": ["NVDA", "MSFT", "GOOGL", "META"],
        "use_case": "catching technical founders and AI startups on launch day with external domains and upvote traction",
    },
    {
        "slug": "b2b-podcast-host-email-guest-sponsorship-lead-scraper",
        "name": "B2B Podcast Host Email, Guest & Sponsorship Lead API",
        "topic": "Podcast Host Email Extraction from Apple Podcasts & RSS Feeds",
        "tags": ["podcast", "b2b", "marketing", "python"],
        "tickers": ["SPOT", "AAPL", "META", "GOOGL"],
        "use_case": "extracting verified podcast host emails (itunes:email) and episode counts for PR guest booking and sponsorships",
    },
    {
        "slug": "github-ai-devtools-repo-developer-b2b-lead-scraper",
        "name": "GitHub AI & DevTools Repo & Developer B2B Lead API",
        "topic": "Trending GitHub AI, MCP & Open-Source Startup Lead Discovery",
        "tags": ["github", "ai", "opensource", "python"],
        "tickers": ["MSFT", "NVDA", "GTLB", "DDOG"],
        "use_case": "discovering commercial open-source startups, star velocity, and external homepage URLs from GitHub",
    },
    {
        "slug": "ai-biotech-research-scientist-lab-b2b-lead-scraper",
        "name": "AI & Biotech R&D Scientist, Lab & Author B2B Lead API",
        "topic": "AI & Biotech PhD R&D Scientist & Corporate Lab Lead Sourcing",
        "tags": ["ai", "biotech", "science", "python"],
        "tickers": ["NVDA", "LLY", "ILMN", "TMO"],
        "use_case": "sourcing lead scientists, university/corporate R&D labs, citation counts, and open-access PDFs",
    },
    {
        "slug": "polymarket-live-odds-volume-arbitrage-prediction-api",
        "name": "Polymarket Live Odds, Volume & Arbitrage Prediction API",
        "topic": "Polymarket Live Prediction Market Odds, Volume & Arbitrage Spreads",
        "tags": ["crypto", "trading", "python", "api"],
        "tickers": ["COIN", "HOOD", "MSTR", "NVDA"],
        "use_case": "extracting real-time Yes/No implied probabilities (%), 24h USD volume, liquidity, and arbitrage spread checks",
    },
    {
        "slug": "defi-protocol-tvl-crypto-whale-web3-b2b-lead-scraper",
        "name": "DeFi Protocol TVL, Crypto Liquidity & Web3 B2B Lead API",
        "topic": "DeFi Protocol TVL, Multi-Chain Liquidity & Web3 B2B Lead Generation",
        "tags": ["web3", "defi", "crypto", "python"],
        "tickers": ["COIN", "MSTR", "MARA", "RIOT"],
        "use_case": "filtering funded Web3 protocols by TVL ($), 1d/7d liquidity growth %, chains, and X/website handles",
    },
    {
        "slug": "cursor-directory-plugins-mcp-rules-b2b-scraper",
        "name": "Cursor Directory Scraper — Plugins, MCPs, Rules & AI Leads",
        "topic": "Cursor Directory Plugins, Remote MCP Servers & AI Coding Rules",
        "tags": ["ai", "mcp", "devtools", "python"],
        "tickers": ["MSFT", "NVDA", "GTLB", "CRM"],
        "use_case": "extracting Cursor plugins, remote MCP endpoints, .cursorrules, homepage URLs, and GitHub source repos",
    },
    {
        "slug": "cline-mcp-marketplace-ai-plugins-scraper",
        "name": "Cline & Roo Code MCP Marketplace Scraper & AI Leads API",
        "topic": "Cline & Roo Code VS Code MCP Marketplace Server Intelligence",
        "tags": ["ai", "mcp", "vscode", "python"],
        "tickers": ["MSFT", "NVDA", "AMZN", "GOOGL"],
        "use_case": "extracting official VS Code Cline MCP servers, GitHub stars, download counts, and developer repos",
    },
    {
        "slug": "lobehub-mcp-ai-agent-plugins-scraper",
        "name": "LobeHub MCP & AI Agent Plugins Directory Scraper API",
        "topic": "LobeHub AI Agent Plugins, OpenAPI Manifests & MCP Catalog",
        "tags": ["ai", "mcp", "agents", "python"],
        "tickers": ["NVDA", "MSFT", "META", "GOOGL"],
        "use_case": "scraping LobeHub AI agent plugins, OpenAPI manifest URLs, categories, tags, and creator homepages",
    },
    {
        "slug": "dify-ai-marketplace-plugins-catalog-scraper",
        "name": "Dify AI Marketplace & Plugin Catalog Scraper API",
        "topic": "Dify AI Marketplace Plugins, LLM Tools & Install Metrics",
        "tags": ["ai", "llm", "agents", "python"],
        "tickers": ["NVDA", "SNOW", "PLTR", "MSFT"],
        "use_case": "extracting Dify AI Marketplace plugins, author organizations, categories, and enterprise install counts",
    },
    {
        "slug": "activepieces-automation-pieces-actions-scraper",
        "name": "Activepieces Automation Pieces & Integrations Scraper API",
        "topic": "Activepieces Open-Source Automation Pieces & SaaS Integrations",
        "tags": ["automation", "saas", "api", "python"],
        "tickers": ["CRM", "HUBS", "TWLO", "OKTA"],
        "use_case": "extracting Activepieces SaaS integration pieces, action counts, trigger counts, and source links",
    },
    {
        "slug": "composio-ai-agent-toolkits-actions-scraper",
        "name": "Composio AI Agent Toolkits & Integrations Scraper API",
        "topic": "Composio AI Agent Toolkits, OAuth2 Auth Modes & Action Schemas",
        "tags": ["ai", "agents", "mcp", "python"],
        "tickers": ["CRM", "HUBS", "TEAM", "GTLB"],
        "use_case": "extracting Composio AI agent toolkits, OAuth2/API Key auth modes, and documentation URLs",
    },
    {
        "slug": "dune-analytics-web3-dashboards-queries-scraper",
        "name": "Dune Analytics Trending Dashboards & Web3 Queries API",
        "topic": "Dune Analytics Web3 Dashboards, SQL Repos & Analyst Intelligence",
        "tags": ["web3", "crypto", "sql", "python"],
        "tickers": ["COIN", "HOOD", "MSTR", "PYPL"],
        "use_case": "extracting trending Dune Web3 dashboards, SQL query repositories, stars, and analyst handles",
    },
    {
        "slug": "make-com-automation-templates-integrations-scraper",
        "name": "Make.com Automation Templates & App Integrations API",
        "topic": "Make.com (Integromat) Automation Templates & SaaS Integrations",
        "tags": ["automation", "nocode", "saas", "python"],
        "tickers": ["SHOP", "HUBS", "CRM", "INTU"],
        "use_case": "extracting Make.com automation scenario templates, app slugs, and direct template URLs",
    },
    {
        "slug": "vercel-templates-nextjs-starter-ecosystem-scraper",
        "name": "Vercel Templates & Next.js AI Starter Ecosystem API",
        "topic": "Vercel Templates, Next.js AI & SaaS Starter Boilerplates",
        "tags": ["nextjs", "vercel", "ai", "python"],
        "tickers": ["NET", "MSFT", "MDB", "SNOW"],
        "use_case": "extracting official Vercel Next.js AI/SaaS templates, categories, and GitHub example repositories",
    },
    {
        "slug": "langflow-flowise-ai-agent-templates-scraper",
        "name": "Langflow & Flowise AI Agent Workflow Templates API",
        "topic": "Langflow & FlowiseAI Visual RAG & Multi-Agent JSON Templates",
        "tags": ["ai", "rag", "agents", "python"],
        "ticker
]


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=SEC_HEADERS)
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_live_sec_sample(tickers: list[str]) -> list[dict]:
    try:
        cik_data = fetch_json("https://www.sec.gov/files/company_tickers.json")
        cik_map = {
            item["ticker"].upper(): str(item["cik_str"]).zfill(10)
            for item in cik_data.values()
        }
    except Exception:
        return []

    rows = []
    for t in tickers[:4]:
        cik = cik_map.get(t.upper())
        if not cik:
            continue
        try:
            sub = fetch_json(f"https://data.sec.gov/submissions/CIK{cik}.json")
            comp_name = sub.get("name", t)
            sic_desc = sub.get("sicDescription", "Public Enterprise")
            recent = sub.get("filings", {}).get("recent", {})
            forms = recent.get("form", [])
            dates = recent.get("filingDate", [])
            accns = recent.get("accessionNumber", [])

            for i, f_type in enumerate(forms[:15]):
                if f_type in ("4", "8-K", "10-Q", "10-K", "13F-HR", "SC 13G", "144", "6-K", "DEF 14A"):
                    acc_raw = accns[i]
                    acc_clean = acc_raw.replace("-", "")
                    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_clean}/{acc_raw}-index.htm"
                    rows.append({
                        "ticker": t,
                        "company": comp_name,
                        "industry": sic_desc,
                        "form": f_type,
                        "date": dates[i],
                        "url": url,
                    })
                    break
        except Exception:
            continue
    return rows


def build_article(day_index: int, live_rows: list[dict], today_str: str) -> tuple[str, str, str]:
    actor = ACTORS_ROTATION[day_index]
    rel_1 = ACTORS_ROTATION[(day_index + 1) % len(ACTORS_ROTATION)]
    rel_2 = ACTORS_ROTATION[(day_index + 2) % len(ACTORS_ROTATION)]

    title = f"Automating {actor['topic']} in Python & Claude MCP ({today_str})"

    # Medium- & Dev.to-compatible numbered paragraphs (Medium importer never strips numbered paragraphs!)
    snapshot_lines = []
    for idx, r in enumerate(live_rows, 1):
        snapshot_lines.append(
            f"**{idx}. {r['company']} ({r['ticker']})** — Industry: {r['industry']} | Latest Filing: Form {r['form']} (Filed: {r['date']})"
        )
    live_snapshot_md = "\n\n".join(snapshot_lines) if snapshot_lines else "Live SEC EDGAR feed active."

    fence = "```"
    devto_body = f"""Extracting and normalizing **{actor['topic']}** is one of the highest-leverage data pipelines for quantitative researchers, B2B growth engineers, and AI agent builders—especially for **{actor['use_case']}**.

Instead of maintaining fragile local XSLT/XML parsers or proxy networks, you can pull structured **JSON, CSV, or Excel** datasets in seconds using the **[{actor['name']}](https://apify.com/mehdad-datalabs/{actor['slug']})** by **Mehdad DataLabs**.

---

## Live SEC EDGAR Activity Snapshot ({today_str})

Here is a live sample of recent regulatory activity across tracked benchmark tickers ({', '.join(actor['tickers'])}):

{live_snapshot_md}

---

## Quickstart: Run This API in Python (apify-client)

Install the official Python client:

{fence}bash
pip install apify-client pandas
{fence}

Call the **[{actor['name']}](https://apify.com/mehdad-datalabs/{actor['slug']})** endpoint directly from Python:

{fence}python
from apify_client import ApifyClient
import pandas as pd

client = ApifyClient("YOUR_APIFY_API_TOKEN")

# Run the Actor and wait for results
run = client.actor("mehdad-datalabs/{actor['slug']}").call()

# Load clean JSON records into a Pandas DataFrame
items = client.dataset(run["defaultDatasetId"]).list_items().items
df = pd.DataFrame(items)
print(df.head())
{fence}

---

## Connect Directly to Claude Desktop, Cursor (MCP) & n8n

This Actor is natively compatible with Apify's **Model Context Protocol (MCP)** server (`@apify/actors-mcp-server`). You can also trigger it on a daily schedule inside **n8n, Make, Clay, or Zapier** to route real-time alerts into Slack, Telegram, HubSpot, or Google Sheets.

**1. Live API Playground:** [{actor['name']}](https://apify.com/mehdad-datalabs/{actor['slug']})

**2. Related API:** [{rel_1['name']}](https://apify.com/mehdad-datalabs/{rel_1['slug']})

**3. Related API:** [{rel_2['name']}](https://apify.com/mehdad-datalabs/{rel_2['slug']})

**4. Open-Source Python SDK & Full 41-API Directory on GitHub:** [https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite](https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite)
"""

    all_links = "\n\n".join(
        [f"**{i+1}.** [{a['name']}](https://apify.com/mehdad-datalabs/{a['slug']})" for i, a in enumerate(ACTORS_ROTATION)]
    )
    github_body = f"{devto_body}\n---\n\n## Complete 41-API Directory\n\n{all_links}\n"

    return title, devto_body, github_body


def publish_to_devto(title: str, body: str, tags: list[str]) -> str:
    if not DEVTO_API_KEY:
        print("No DEVTO_API_KEY set. Skipping Dev.to API call.")
        return ""

    payload = json.dumps({
        "article": {
            "title": title[:125],
            "published": False,
            "body_markdown": body,
            "tags": tags[:4],
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://dev.to/api/articles",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "api-key": DEVTO_API_KEY,
            "User-Agent": "MehdadDataLabsSeoBot/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            res_data = json.loads(resp.read().decode("utf-8"))
            url = res_data.get("url", "")
            print(f"Successfully published to Dev.to: {url}")
            return url
    except Exception as e:
        print(f"Dev.to publish warning: {e}")
        return ""


def main():
    today = datetime.date.today()
    day_index = today.toordinal() % len(ACTORS_ROTATION)
    featured_actor = ACTORS_ROTATION[day_index]
    today_str = today.strftime("%b %d, %Y")

    live_rows = fetch_live_sec_sample(featured_actor["tickers"])
    title, devto_body, github_body = build_article(day_index, live_rows, today_str)

    devto_url = publish_to_devto(title, devto_body, featured_actor["tags"])

    with open("LATEST_MARKET_SIGNALS.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        if devto_url:
            f.write(f"**Read on Dev.to:** [{devto_url}]({devto_url})\n\n")
        f.write(github_body)
    print("Updated LATEST_MARKET_SIGNALS.md successfully.")


if __name__ == "__main__":
    main()
