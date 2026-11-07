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
        "use_case": "tracking real-time C-suite open-market stock purchases (Code P) and sales (Code S)",
    },
    {
        "slug": "sec-13f-institutional-holdings-hedge-fund-whale-scraper",
        "name": "SEC Form 13F Institutional Holdings & Hedge Fund Whale Scraper",
        "topic": "Institutional Hedge Fund & Whale Portfolio Filings (SEC Form 13F-HR)",
        "tags": ["finance", "python", "api", "data"],
        "tickers": ["BRK-A", "BLK", "NVDA", "MSFT"],
        "use_case": "extracting quarterly institutional holdings, CUSIPs, portfolio weights (%), and Put/Call options",
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


def build_github_report(actor: dict, live_rows: list[dict], today_str: str) -> tuple[str, str]:
    title = f"How to Automate {actor['topic']} in Python, n8n & Claude MCP ({today_str})"

    table_lines = [
        "| Ticker | Company Name | Industry / SIC | Latest SEC Form | Filing Date | SEC Archive Link |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in live_rows:
        table_lines.append(
            f"| `{r['ticker']}` | {r['company']} | {r['industry']} | `{r['form']}` | {r['date']} | [View Filing]({r['url']}) |"
        )
    live_table_md = "\n".join(table_lines) if len(table_lines) > 2 else "*Live SEC EDGAR feed active.*"

    body = f"""Extracting and normalizing **{actor['topic']}** is a high-value pipeline for quantitative researchers and B2B engineers—especially for **{actor['use_case']}**.

Instead of writing custom XML/XBRL parsers, you can pull structured JSON or CSV datasets in seconds using the **[{actor['name']}](https://apify.com/mehdad-datalabs/{actor['slug']})**.

---

## Live SEC EDGAR Snapshot ({today_str})

{live_table_md}

---

## Python Quickstart (`apify-client`)

    from apify_client import ApifyClient
    import pandas as pd

    client = ApifyClient("YOUR_APIFY_API_TOKEN")
    run = client.actor("mehdad-datalabs/{actor['slug']}").call()
    df = pd.DataFrame(client.dataset(run["defaultDatasetId"]).list_items().items)
    print(df.head())

- **Live API Endpoint:** [https://apify.com/mehdad-datalabs/{actor['slug']}](https://apify.com/mehdad-datalabs/{actor['slug']})
- **Full 20-API GitHub SDK:** [https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite](https://github.com/meher20100/sec-edgar-fda-b2b-json-api-suite)
"""
    return title, body


def main():
    today = datetime.date.today()
    day_index = today.toordinal() % len(ACTORS_ROTATION)
    featured_actor = ACTORS_ROTATION[day_index]
    today_str = today.strftime("%b %d, %Y")

    live_rows = fetch_live_sec_sample(featured_actor["tickers"])
    title, body = build_github_report(featured_actor, live_rows, today_str)

    # Save directly to GitHub (100% immune to third-party spam filters & indexed by Google!)
    with open("LATEST_MARKET_SIGNALS.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{body}")
    print("Updated LATEST_MARKET_SIGNALS.md successfully.")


if __name__ == "__main__":
    main()
