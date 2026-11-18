import os
import json
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mehdad-datalabs-sec-fda-b2b")
BASE_URL = "https://api.apify.com/v2/acts"


async def _run_actor(actor_slug: str, run_input: dict) -> str:
    token = os.getenv("APIFY_TOKEN", "").strip()
    if not token:
        return json.dumps({
            "error": "APIFY_TOKEN environment variable is required. Get a free key ($5/mo credit) at https://console.apify.com/account/integrations"
        })
    url = f"{BASE_URL}/mehdad-datalabs~{actor_slug}/run-sync-get-dataset-items"
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(url, params={"token": token}, json=run_input)
        resp.raise_for_status()
        return json.dumps(resp.json()[:25], ensure_ascii=False)


@mcp.tool()
async def get_sec_form4_insider_trades(tickers: list[str], max_filings_per_ticker: int = 10) -> str:
    """Fetch parsed US SEC Form 4 insider buying and selling filings for stock tickers."""
    return await _run_actor(
        "sec-form-4-insider-trading-scraper-xml-parser-api",
        {"tickers": tickers, "transactionCodes": ["P", "S"], "maxFilingsPerTicker": max_filings_per_ticker},
    )


@mcp.tool()
async def get_sec_13f_hedge_fund_holdings(institutions: list[str], max_holdings: int = 25) -> str:
    """Fetch US SEC Form 13F institutional whale holdings for hedge funds."""
    return await _run_actor(
        "sec-13f-institutional-holdings-hedge-fund-whale-scraper",
        {"institutions": institutions, "maxHoldingsPerInstitution": max_holdings},
    )


@mcp.tool()
async def get_fda_drug_approvals(max_results: int = 20) -> str:
    """Fetch recent US FDA NDA/BLA drug approvals and biotech catalysts."""
    return await _run_actor(
        "fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper",
        {"maxResults": max_results},
    )


@mcp.tool()
async def get_shopify_store_catalog(store_domains: list[str], max_products_per_store: int = 25) -> str:
    """Scrape live Shopify competitor product catalogs, prices, and compare-at discounts."""
    return await _run_actor(
        "shopify-store-spy-product-catalog-price-b2b-scraper",
        {"storeDomains": store_domains, "maxProductsPerStore": max_products_per_store},
    )


@mcp.tool()
async def get_yc_startups(industry_or_keyword: str = "AI", max_results: int = 25) -> str:
    """Extract funded Y Combinator startups by industry, keyword, and hiring status."""
    return await _run_actor(
        "y-combinator-yc-startup-directory-b2b-lead-scraper",
        {"industryOrKeyword": industry_or_keyword, "maxResults": max_results},
    )


@mcp.tool()
async def enrich_b2b_websites(websites: list[str]) -> str:
    """Enrich B2B company websites with contact emails, phone numbers, social links, and tech stack."""
    return await _run_actor(
        "b2b-website-email-phone-social-links-tech-stack-scraper",
        {"websites": websites},
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
