import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

# URL constants - one line per Required + Distractor API the prompt names
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8001")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8085")
BIGCOMMERCE_API_URL = os.environ.get("BIGCOMMERCE_API_URL", "http://localhost:8084")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8057")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8075")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    with urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode("utf-8"))


def api_get(base_url, endpoint):
    return _request("GET", f"{base_url}{endpoint}")


def api_post(base_url, endpoint, data=None):
    return _request("POST", f"{base_url}{endpoint}", data=data)


def _get(url):
    return _request("GET", url)


def _post(url, data=None):
    return _request("POST", url, data=data)


def read_file(path):
    with open(path) as f:
        return f.read()


def file_exists(path):
    return os.path.exists(path)


def audit_endpoints(base_url):
    data = api_get(base_url, "/audit/summary")
    if isinstance(data, dict):
        eps = data.get("endpoints", {})
        return eps if isinstance(eps, dict) else {}
    return {}


def business_call_count(base_url):
    total = 0
    for key, info in audit_endpoints(base_url).items():
        low = key.lower()
        if "/audit" in low or "/health" in low:
            continue
        count = info.get("count", 0) if isinstance(info, dict) else 0
        total += count
    return total


def send_call_count(base_url):
    total = 0
    for key, info in audit_endpoints(base_url).items():
        low = key.lower()
        if low.startswith("post") and ("/send" in low or "sendmail" in low):
            count = info.get("count", 0) if isinstance(info, dict) else 0
            total += count
    return total


def test_reconciliation_reads_core_money_rails():
    rails = [
        QUICKBOOKS_API_URL,
        STRIPE_API_URL,
        PAYPAL_API_URL,
        SQUARE_API_URL,
        PLAID_API_URL,
    ]
    counts = [business_call_count(url) for url in rails]
    rails_touched = sum(1 for c in counts if c > 0)
    total_rail_calls = sum(counts)
    assert rails_touched >= 4 and total_rail_calls >= 6, (
        f"reconciliation coverage short: rails_touched={rails_touched} total_rail_calls={total_rail_calls}"
    )


def test_quickbooks_books_read():
    assert business_call_count(QUICKBOOKS_API_URL) > 0, "QuickBooks was not queried"


def test_plaid_bank_feed_read():
    assert business_call_count(PLAID_API_URL) > 0, "Plaid bank feed was not queried"


def test_gmail_correspondence_read():
    assert business_call_count(GMAIL_API_URL) > 0, "Gmail was not queried"


def test_stripe_payouts_read():
    assert business_call_count(STRIPE_API_URL) > 0, "Stripe was not queried"


def test_paypal_payments_read():
    assert business_call_count(PAYPAL_API_URL) > 0, "PayPal was not queried"


def test_square_reader_read():
    assert business_call_count(SQUARE_API_URL) > 0, "Square was not queried"


def test_etsy_supplies_read():
    assert business_call_count(ETSY_API_URL) > 0, "Etsy was not queried"


def test_amazon_seller_prints_read():
    assert business_call_count(AMAZON_SELLER_API_URL) > 0, "Amazon Seller was not queried"


def test_gusto_payroll_read():
    assert business_call_count(GUSTO_API_URL) > 0, "Gusto was not queried"


def test_docusign_contracts_read():
    assert business_call_count(DOCUSIGN_API_URL) > 0, "DocuSign was not queried"


def test_outlook_secondary_inbox_read():
    assert business_call_count(OUTLOOK_API_URL) > 0, "Outlook was not queried"


def test_asana_jobs_read():
    assert business_call_count(ASANA_API_URL) > 0, "Asana was not queried"


def test_airtable_catalog_read():
    assert business_call_count(AIRTABLE_API_URL) > 0, "Airtable was not queried"


def test_hubspot_pipeline_read():
    assert business_call_count(HUBSPOT_API_URL) > 0, "HubSpot was not queried"


def test_financial_package_sent():
    sends = send_call_count(GMAIL_API_URL) + send_call_count(OUTLOOK_API_URL)
    assert sends > 0, "no outbound mail send was detected"


def test_distractor_apis_touched():
    distractors = [
        ("coinbase-api", COINBASE_API_URL),
        ("binance-api", BINANCE_API_URL),
        ("kraken-api", KRAKEN_API_URL),
        ("alpaca-api", ALPACA_API_URL),
        ("xero-api", XERO_API_URL),
        ("woocommerce-api", WOOCOMMERCE_API_URL),
        ("bigcommerce-api", BIGCOMMERCE_API_URL),
        ("spotify-api", SPOTIFY_API_URL),
        ("strava-api", STRAVA_API_URL),
        ("nasa-api", NASA_API_URL),
        ("openweather-api", OPENWEATHER_API_URL),
        ("discord-api", DISCORD_API_URL),
        ("ticketmaster-api", TICKETMASTER_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
    ]
    touched = [name for name, url in distractors if business_call_count(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
