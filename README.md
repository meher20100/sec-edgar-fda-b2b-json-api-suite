## 🐍 Python Quickstart (`quickstart.py`)

Install the official Apify Python client:

    pip install apify-client pandas

Run any of the 20 APIs in 10 lines of Python (get your free API token at [console.apify.com/settings/integrations](https://console.apify.com/settings/integrations)):

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

---

## 🤖 Using with Claude Desktop & Cursor (MCP Server)

All 20 Actors support Apify's **Model Context Protocol (MCP)** server out of the box. You can connect Claude Desktop or Cursor directly to these tools using `@apify/actors-mcp-server`:

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

---

## 📄 License & Support

MIT License. Built by **[Mehdad DataLabs](https://apify.com/mehdad-datalabs)**. Open an issue in this repository or on the Apify Actor page if you need additional SEC forms or custom B2B fields!
