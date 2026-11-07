import os
import json
import datetime
import urllib.request

DEVTO_API_KEY = os.getenv("DEVTO_API_KEY", "").strip()

SEC_HEADERS = {
    "User-Agent": "MehdadDataLabsBot support@mehdaddatalabs.io",
    "Accept": "application/json",
}

# All 20 Actors in your Mehdad DataLabs Suite (Rotates automatically every day!)
ACTORS_ROTATION = [
    {
        "slug": "sec-form-4-insider-trading-scraper-xml-parser-api",
        "name": "SEC Form 4 Insider Trading Scraper & XML Parser API",
        "topic": "CEO & CFO Insider Stock Trading (SEC Form 4 XML)",
        "tags": ["python", "finance", "api", "ai"],
        "tickers": ["NVDA", "AAPL", "MSFT", "PLTR", "TSLA"],
        "form_filter": "4",
        "use_case": "tracking real-time C-suite open-market stock purchases (Code P) and sales (Code S) before retail news coverage",
    },
    {
        "slug": "sec-13f-institutional-holdings-hedge-fund-whale-scraper",
        "name": "SEC Form 13F Institutional Holdings & Hedge Fund Whale Scraper",
        "topic": "Institutional Hedge Fund & Whale Portfolio Filings (SEC Form 13F-HR)",
        "tags": ["finance", "python", "api", "data"],
        "tickers": ["BRK-A", "BLK", "NVDA", "MSFT"],
        "form_filter": "13F-HR",
        "use_case": "extracting quarterly institutional holdings, CUSIPs, portfolio weights (%), and Put/Call option positions",
    },
    {
        "slug": "sec-8k-corporate-events-ma-executive-change-scraper",
        "name": "SEC Form 8-K Corporate Events, M&A & Executive Change Scraper",
        "topic": "Breaking Corporate Catalysts, M&A & CEO Changes (SEC Form 8-K)",
        "tags": ["api", "python", "finance", "automation"],
        "tickers": ["AAPL", "NVDA", "META", "AMZN", "CRM"],
        "form_filter": "8-K",
        "use_case": "decoding Item 5.02 executive appointments, Item 2.02 earnings releases, and Item 1.01 M&A agreements for B2B outreach and event-driven trading",
    },
    {
        "slug": "sec-10k-10q-xbrl-financial-statements-earnings-api",
        "name": "SEC 10-K & 10-Q XBRL Financial Statements & Earnings API",
        "topic": "Audited US-GAAP XBRL Financial Statements (SEC Form 10-K & 10-Q)",
        "tags": ["python", "finance", "ai", "api"],
        "tickers": ["MSFT", "NVDA", "GOOGL", "AAPL"],
        "form_filter": "10-Q",
        "use_case": "normalizing quarterly and annual Revenue, Net Income, Diluted EPS, Cash Flow, and Balance Sheet metrics for AI agents (MCP) and DCF valuation models",
    },
    {
        "slug": "sec-schedule-13d-13g-activist-investor-ownership-api",
        "name": "SEC Schedule 13D & 13G Activist Investor & 5%+ Ownership API",
        "topic": "Activist Hedge Fund Takeovers & 5%+ Whale Stakes (Schedule 13D & 13G)",
        "tags": ["finance", "python", "api", "trading"],
        "tickers": ["DIS", "INTC", "PYPL", "CRM"],
        "form_filter": "SC 13G",
        "use_case": "monitoring hostile takeover campaigns (Schedule 13D) and 5%+ institutional block accumulations (Schedule 13G)",
    },
    {
        "slug": "sec-ipo-s1-form144-insider-sale-scraper",
        "name": "SEC Form S-1 IPO Pipeline & Form 144 Insider Sale Notice API",
        "topic": "Pre-IPO Tech Registrations & Rule 144 Restricted Stock Sales (Form S-1 & 144)",
        "tags": ["finance", "python", "api", "startups"],
        "tickers": ["PLTR", "RDDT", "ARM", "NVDA"],
        "form_filter": "144",
        "use_case": "catching Rule 144 founder/VC proposed restricted stock sales and Form S-1/S-3 dilution filings early",
    },
    {
        "slug": "sec-form-d-startup-funding-vc-b2b-lead-scraper",
        "name": "SEC Form D Startup Funding, VC Raise & Founder B2B Lead API",
        "topic": "Newly Funded Startups & Venture Capital Raises (SEC Form D XML)",
        "tags": ["startups", "b2b", "api", "python"],
        "tickers": ["NVDA", "PLTR", "CRM", "SNOW"],
        "form_filter": "D",
        "use_case": "extracting newly funded private startups, exact dollar amounts raised, and Founder/CEO contact names within 15 days of their VC check",
    },
    {
        "slug": "sec-nport-etf-mutual-fund-holdings-xml-scraper",
        "name": "SEC Form N-PORT Mutual Fund & ETF Portfolio Holdings API",
        "topic": "Monthly ETF & Mutual Fund Portfolio Holdings (SEC Form N-PORT)",
        "tags": ["finance", "python", "api", "etf"],
        "tickers": ["NVDA", "AAPL", "MSFT", "AMZN"],
        "form_filter": "NPORT-P",
        "use_case": "parsing Vanguard, BlackRock iShares, and Fidelity ETF holdings XML tables with ISINs, CUSIPs, and exact net asset weights",
    },
    {
        "slug": "sec-def14a-ceo-executive-compensation-proxy-scraper",
        "name": "SEC DEF 14A Executive Compensation & Proxy Statement API",
        "topic": "CEO Compensation, Board Elections & Merger Proxies (SEC Form DEF 14A)",
        "tags": ["finance", "api", "python", "governance"],
        "tickers": ["NVDA", "AAPL", "TSLA", "MSFT"],
        "form_filter": "DEF 14A",
        "use_case": "benchmarking C-suite executive compensation, golden parachutes (DEFM14A), and activist proxy fights (DFAN14A)",
    },
    {
        "slug": "sec-20f-6k-foreign-adr-international-stock-scraper",
        "name": "SEC Form 20-F & 6-K Global ADR & Foreign Stock Filings API",
        "topic": "International ADR Stocks & Semiconductor Monthly Revenue (SEC Form 20-F & 6-K)",
        "tags": ["finance", "python", "api", "global"],
        "tickers": ["TSM", "ASML", "NVO", "BABA"],
        "form_filter": "6-K",
        "use_case": "tracking TSMC monthly wafer revenue, ASML earnings, and Novo Nordisk clinical updates filed on Foreign Private Issuer Forms 20-F and 6-K",
    },
    {
        "slug": "us-federal-government-contract-awards-dod-b2b-scraper",
        "name": "US Federal Government Contract Awards & DoD B2B Lead Scraper",
        "topic": "Pentagon (DoD) & US Federal Government Contract Winners (GovCon API)",
        "tags": ["govtech", "b2b", "api", "python"],
        "tickers": ["PLTR", "LMT", "BAH", "LDOS"],
        "form_filter": "8-K",
        "use_case": "identifying newly funded defense, AI, and cybersecurity federal contractors for B2B subcontracting outreach and stock catalyst tracking",
    },
    {
        "slug": "fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper",
        "name": "FDA Drug Approvals, NDA/BLA Biotech Catalyst & Pharma API",
        "topic": "US FDA New Drug (NDA) & Biologics (BLA) Biotech Catalysts",
        "tags": ["biotech", "healthcare", "api", "python"],
        "tickers": ["LLY", "NVO", "PFE", "VRTX"],
        "form_filter": "8-K",
        "use_case": "tracking FDA NDA, BLA, and ANDA drug approvals, Priority Review designations, and pharmaceutical sponsor leads",
    },
    {
        "slug": "clinical-trials-biotech-catalyst-cro-b2b-lead-scraper",
        "name": "ClinicalTrials.gov Phase 1-3 Biotech Catalyst & B2B Lead API",
        "topic": "Phase 1, 2 & 3 Clinical Trial Readout Catalysts & CRO B2B Leads",
        "tags": ["biotech", "healthcare", "python", "api"],
        "tickers": ["LLY", "MRNA", "VRTX", "REGN"],
        "form_filter": "8-K",
        "use_case": "extracting active recruiting clinical trials, primary completion readout dates, and Principal Investigator contact emails and phones",
    },
    {
        "slug": "fda-510k-medical-device-clearances-medtech-b2b-scraper",
        "name": "FDA 510(k) Medical Device Clearances & MedTech B2B Lead API",
        "topic": "US FDA 510(k) Medical Device Clearances & MedTech B2B Contacts",
        "tags": ["medtech", "healthcare", "api", "python"],
        "tickers": ["ISRG", "MDT", "ABT", "SYK"],
        "form_filter": "8-K",
        "use_case": "capturing newly cleared medical devices along with the MedTech Applicant Company Name, Named Contact Person, and HQ Address",
    },
    {
        "slug": "fda-product-recalls-safety-enforcement-b2b-scraper",
        "name": "FDA Drug, Device & Food Recall Enforcement & Legal Lead API",
        "topic": "FDA Class I, II & III Product Recalls & Mass-Tort Litigation Leads",
        "tags": ["healthcare", "legaltech", "api", "python"],
        "tickers": ["ABT", "BAX", "MDT", "PFE"],
        "form_filter": "8-K",
        "use_case": "monitoring critical Class I medical device, pharmaceutical, and food safety recalls for mass-tort law firms and QA compliance teams",
    },
    {
        "slug": "us-doctor-dentist-clinic-healthcare-b2b-lead-scraper",
        "name": "US Doctor, Dentist & Medical Clinic B2B Lead Scraper API",
        "topic": "Verified US Doctors, Dentists & Medical Clinics B2B Lead Generation (CMS NPI)",
        "tags": ["b2b", "healthcare", "api", "python"],
        "tickers": ["UNH", "HCA", "CVS", "ELV"],
        "form_filter": "10-Q",
        "use_case": "extracting NPI-2 dental and medical clinics with Clinic Owner / Authorized Official names, direct phone numbers, and state license numbers",
    },
    {
        "slug": "us-pharmacy-medical-lab-dme-b2b-lead-scraper",
        "name": "US Pharmacy, Clinical Lab & Medical Supply B2B Lead API",
        "topic": "Independent US Pharmacies, Diagnostic Labs & DME Suppliers B2B Leads",
        "tags": ["b2b", "healthcare", "python", "api"],
        "tickers": ["MCK", "COR", "CAH", "LH"],
        "form_filter": "10-Q",
        "use_case": "building verified outbound lists of independent pharmacies, compounding pharmacies, and clinical labs with Chief Pharmacist/Owner direct phones",
    },
    {
        "slug": "fdic-us-bank-directory-deposits-assets-b2b-scraper",
        "name": "FDIC US Bank Directory, Deposits, Assets & B2B Lead API",
        "topic": "US Commercial & Community Bank Directory, Assets, Deposits & ROA/ROE",
        "tags": ["fintech", "banking", "api", "python"],
        "tickers": ["JPM", "BAC", "WFC", "C"],
        "form_filter": "10-Q",
        "use_case": "filtering every FDIC-insured community and regional bank by total assets ($), deposits ($), ROA/ROE %, branch count, and website for fintech B2B sales",
    },
    {
        "slug": "cfpb-fintech-bank-consumer-complaint-b2b-scraper",
        "name": "CFPB Fintech & Bank Consumer Complaint Intelligence API",
        "topic": "Fintech, Crypto & Bank Consumer Complaint & Regulatory Risk Intelligence",
        "tags": ["fintech", "crypto", "api", "python"],
        "tickers": ["COIN", "HOOD", "PYPL", "SOFI"],
        "form_filter": "10-Q",
        "use_case": "tracking consumer fraud, account-freeze disputes, and regulatory risk disclosures across Coinbase, Robinhood, PayPal, and national banks",
    },
    {
        "slug": "us-public-company-b2b-profile-sic-hq-phone-scraper",
        "name": "US Public Company B2B Directory, SIC & HQ Phone API",
        "topic": "US Public Company B2B CRM Enrichment (Corporate HQ Phone, EIN Tax ID & SIC)",
        "tags": ["b2b", "api", "python", "automation"],
        "tickers": ["NVDA", "AAPL", "MSFT", "PLTR", "CRM"],
        "form_filter": "10-K",
        "use_case": "enriching NYSE and Nasdaq enterprise accounts in Clay, n8n, or HubSpot with verified Corporate HQ switchboard phones, street addresses, EINs, and SIC codes",
    },
]


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=SEC_HEADERS)
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_live_sec_sample(tickers: list[str]) -> list[dict]:
    """Pulls live recent SEC filings for the featured tickers so every daily post has real, fresh data."""
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
            phone = sub.get("phone", "Verified HQ")
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
                        "phone": phone,
                        "form": f_type,
                        "date": dates[i],
                        "url": url,
                    })
                    break
        except Exception:
            continue
    return rows


def build_article(actor: dict, live_rows: list[dict], today_str: str) -> tuple[str, str]:
    title = f"How to Automate {actor['topic']} in Python, n8n & Claude MCP ({today_str})"

    table_lines = [
        "| Ticker | Company Name | Industry / SIC | Latest SEC Form | Filing Date | Verified Link |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in live_rows:
        table_lines.append(
            f"| `{r['ticker']}` | {r['company']} | {r['industry']} | `{r['form']}` | {r['date']} | [View Filing]({r['url']}) |"
        )
    live_table_md = "\n".join(table_lines) if len(table_lines) > 2 else "*Live SEC EDGAR feed active.*"

    suite_links = []
    for a in ACTORS_ROTATION:
        suite_links.append(f"- [{a['name']}](https://apify.com/mehdad-datalabs/{a['slug']})")
    suite_md = "\n".join(suite_links)

    body = f"""Extracting and normalizing **{actor['topic']}** is one of the highest-leverage data pipelines for quantitative researchers, B2B growth engineers, and AI agent builders—especially for **{actor['use_case']}**.

Instead of maintaining fragile local scrapers, XSLT parsers, or expensive proxy networks, you can pull clean, structured **JSON, CSV, or Excel** datasets in under 5 seconds using the **[{actor['name']}](https://apify.com/mehdad-datalabs/{actor['slug']})** by **Mehdad DataLabs**.

---

## Live Market & Regulatory Snapshot ({today_str})

Here is a live sample of recent SEC EDGAR activity across tracked benchmark tickers (`{', '.join(actor['tickers'])}`):

{live_table_md}

---

## Quickstart: Run This API in Python (`apify-client`)

Install the official client:

    pip install apify-client pandas

Call the **[{actor['name']}](https://apify.com/mehdad-datalabs/{actor['slug']})** endpoint directly from Python:

    from apify_client import ApifyClient
    import pandas as pd

    client = ApifyClient("YOUR_APIFY_API_TOKEN")

    # Run the Actor and wait for results
    run = client.actor("mehdad-datalabs/{actor['slug']}").call()

    # Load clean JSON records into a Pandas DataFrame
    items = client.dataset(run["defaultDatasetId"]).list_items().items
    df = pd.DataFrame(items)
    print(df.head())

---

## Connect Directly to Claude Desktop, Cursor (MCP) & n8n

This Actor is natively compatible with Apify's **Model Context Protocol (MCP)** server (`@apify/actors-mcp-server`). You can also trigger it on a daily schedule inside **n8n, Make, Clay, or Zapier** to route real-time alerts into Slack, Telegram, HubSpot, or Google Sheets.

- **Try the Live API Playground:** [https://apify.com/mehdad-datalabs/{actor['slug']}](https://apify.com/mehdad-datalabs/{actor['slug']})
- **Open-Source Python SDK & Examples on GitHub:** [https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite](https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite)

---

## Explore the Full 20-API Financial, Biotech & B2B Intelligence Suite

{suite_md}
"""
    return title, body


def publish_to_devto(title: str, body: str, tags: list[str]) -> str:
    if not DEVTO_API_KEY:
        print("No DEVTO_API_KEY set. Skipping Dev.to API call.")
        return ""

    payload = json.dumps({
        "article": {
            "title": title[:125],
            "published": True,
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

    print(f"Featured Actor for {today_str}: {featured_actor['name']}")
    live_rows = fetch_live_sec_sample(featured_actor["tickers"])
    title, body = build_article(featured_actor, live_rows, today_str)

    devto_url = publish_to_devto(title, body, featured_actor["tags"])

    # Also write LATEST_MARKET_SIGNALS.md in the GitHub repo for daily GitHub SEO commits
    with open("LATEST_MARKET_SIGNALS.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        if devto_url:
            f.write(f"**Read on Dev.to:** [{devto_url}]({devto_url})\n\n")
        f.write(body)
    print("Updated LATEST_MARKET_SIGNALS.md successfully.")


if __name__ == "__main__":
    main()
