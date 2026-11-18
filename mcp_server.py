import os
import json
from typing import Annotated
import httpx
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

mcp = FastMCP("mehdad-datalabs-sec-fda-b2b")
BASE_URL = "https://api.apify.com/v2/acts"
READ_ONLY = ToolAnnotations(
    readOnlyHint=True,
    destructiveHint=False,
    idempotentHint=True,
    openWorldHint=True,
)


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


@mcp.tool(annotations=READ_ONLY)
async def get_sec_form4_insider_trades(
    tickers: Annotated[
        list[str],
        Field(description="List of US stock ticker symbols to query (e.g., ['NVDA', 'AAPL', 'TSLA'])."),
    ],
    max_filings_per_ticker: Annotated[
        int,
        Field(default=10, ge=1, le=50, description="Maximum number of recent SEC Form 4 filings to return per ticker (1-50)."),
    ] = 10,
) -> str:
    """Fetch parsed US SEC EDGAR Form 4 insider buying (P) and selling (S) transactions.

    Use this tool to track executive (CEO, CFO, Director) open-market stock purchases and sales.
    Returns a JSON array of up to 25 filing records containing ticker, companyName, insiderName,
    insiderRole, transactionCode, shares, pricePerShare, totalValue, filingDate, and filingUrl.
    Requires the APIFY_TOKEN environment variable.
    """
    return await _run_actor(
        "sec-form-4-insider-trading-scraper-xml-parser-api",
        {"tickers": tickers, "transactionCodes": ["P", "S"], "maxFilingsPerTicker": max_filings_per_ticker},
    )


@mcp.tool(annotations=READ_ONLY)
async def get_sec_13f_hedge_fund_holdings(
    institutions: Annotated[
        list[str],
        Field(description="List of institutional investment manager names to query (e.g., ['Berkshire Hathaway', 'Citadel Advisors'])."),
    ],
    max_holdings: Annotated[
        int,
        Field(default=25, ge=1, le=100, description="Maximum number of top portfolio positions to return per institution (1-100)."),
    ] = 25,
) -> str:
    """Fetch quarterly US SEC EDGAR Form 13F institutional hedge fund portfolio holdings.

    Use this tool to inspect major whale equity positions and share counts reported to the SEC.
    Returns a JSON array of up to 25 holdings containing institution, issuerName, cusip,
    valueUsd, shares, and reportDate. Requires the APIFY_TOKEN environment variable.
    """
    return await _run_actor(
        "sec-13f-institutional-holdings-hedge-fund-whale-scraper",
        {"institutions": institutions, "maxHoldingsPerInstitution": max_holdings},
    )


@mcp.tool(annotations=READ_ONLY)
async def get_fda_drug_approvals(
    max_results: Annotated[
        int,
        Field(default=20, ge=1, le=100, description="Maximum number of recent FDA drug approval records to retrieve (1-100)."),
    ] = 20,
) -> str:
    """Fetch recent US FDA New Drug Applications (NDA) and Biologics License Applications (BLA).

    Use this tool to monitor biotech/pharma FDA approval catalysts and newly cleared therapies.
    Returns a JSON array of up to 25 records containing drugName, sponsor, applicationNumber,
    activeIngredient, approvalDate, and submissionStatus. Requires the APIFY_TOKEN environment variable.
    """
    return await _run_actor(
        "fda-drug-approvals-biotech-catalyst-pharma-b2b-scraper",
        {"maxResults": max_results},
    )


@mcp.tool(annotations=READ_ONLY)
async def get_shopify_store_catalog(
    store_domains: Annotated[
        list[str],
        Field(description="List of Shopify store domains without protocol (e.g., ['allbirds.com', 'gymshark.com'])."),
    ],
    max_products_per_store: Annotated[
        int,
        Field(default=25, ge=1, le=200, description="Maximum number of products to extract per Shopify store (1-200)."),
    ] = 25,
) -> str:
    """Extract live product catalogs, prices, discounts, and availability from Shopify stores.

    Use this tool for e-commerce competitor price monitoring and SKU research.
    Returns a JSON array of up to 25 products containing storeDomain, title, vendor, price,
    compareAtPrice, available, and productUrl. Requires the APIFY_TOKEN environment variable.
    """
    return await _run_actor(
        "shopify-store-spy-product-catalog-price-b2b-scraper",
        {"storeDomains": store_domains, "maxProductsPerStore": max_products_per_store},
    )


@mcp.tool(annotations=READ_ONLY)
async def get_yc_startups(
    industry_or_keyword: Annotated[
        str,
        Field(default="AI", description="Industry, vertical, or keyword to filter Y Combinator startups (e.g., 'AI', 'B2B', 'Fintech')."),
    ] = "AI",
    max_results: Annotated[
        int,
        Field(default=25, ge=1, le=100, description="Maximum number of Y Combinator startup profiles to return (1-100)."),
    ] = 25,
) -> str:
    """Search funded Y Combinator startups by industry, keyword, batch, and hiring status.

    Use this tool for B2B lead generation, VC deal sourcing, and startup market research.
    Returns a JSON array of up to 25 companies containing companyName, batch, website,
    oneLiner, teamSize, isHiring, and industries. Requires the APIFY_TOKEN environment variable.
    """
    return await _run_actor(
        "y-combinator-yc-startup-directory-b2b-lead-scraper",
        {"industryOrKeyword": industry_or_keyword, "maxResults": max_results},
    )


@mcp.tool(annotations=READ_ONLY)
async def enrich_b2b_websites(
    websites: Annotated[
        list[str],
        Field(description="List of full B2B company website URLs to enrich (e.g., ['https://linear.app', 'https://supabase.com'])."),
    ],
) -> str:
    """Enrich B2B company websites with verified contact emails, phone numbers, social links, and tech stack.

    Use this tool to turn a list of company domains into actionable B2B sales leads.
    Returns a JSON array of up to 25 enriched profiles containing website, emails, phones,
    socialLinks (LinkedIn, X, GitHub), and detected techStack. Requires the APIFY_TOKEN environment variable.
    """
    return await _run_actor(
        "b2b-website-email-phone-social-links-tech-stack-scraper",
        {"websites": websites},
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
