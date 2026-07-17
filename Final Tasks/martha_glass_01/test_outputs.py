import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8076")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8038")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8030")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")


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


def endpoint_counts(base_url):
    summary = api_get(base_url, "/audit/summary")
    if isinstance(summary, dict):
        return summary.get("endpoints", {})
    return {}


def business_calls(base_url):
    total = 0
    for key, info in endpoint_counts(base_url).items():
        low = key.lower()
        if "/audit" in low or "/health" in low:
            continue
        if isinstance(info, dict):
            total += info.get("count", 0)
    return total


def count_endpoint(base_url, method, fragment):
    total = 0
    want = method.upper()
    for key, info in endpoint_counts(base_url).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        kmethod, kpath = parts[0].upper(), parts[1]
        if kmethod == want and fragment in kpath and isinstance(info, dict):
            total += info.get("count", 0)
    return total


def test_plaid_consulted():
    assert business_calls(PLAID_API_URL) > 0, "no Plaid business calls recorded"


def test_quickbooks_consulted():
    assert business_calls(QUICKBOOKS_API_URL) > 0, "no QuickBooks business calls recorded"


def test_xero_consulted():
    assert business_calls(XERO_API_URL) > 0, "no Xero business calls recorded"


def test_stripe_consulted():
    assert business_calls(STRIPE_API_URL) > 0, "no Stripe business calls recorded"


def test_paypal_consulted():
    assert business_calls(PAYPAL_API_URL) > 0, "no PayPal business calls recorded"


def test_square_consulted():
    assert business_calls(SQUARE_API_URL) > 0, "no Square business calls recorded"


def test_gusto_consulted():
    assert business_calls(GUSTO_API_URL) > 0, "no Gusto business calls recorded"


def test_amazon_seller_consulted():
    assert business_calls(AMAZON_SELLER_API_URL) > 0, "no Amazon Seller business calls recorded"


def test_coinbase_consulted():
    assert business_calls(COINBASE_API_URL) > 0, "no Coinbase business calls recorded"


def test_binance_consulted():
    assert business_calls(BINANCE_API_URL) > 0, "no Binance business calls recorded"


def test_kraken_consulted():
    assert business_calls(KRAKEN_API_URL) > 0, "no Kraken business calls recorded"


def test_alpaca_consulted():
    assert business_calls(ALPACA_API_URL) > 0, "no Alpaca business calls recorded"


def test_gmail_consulted():
    assert business_calls(GMAIL_API_URL) > 0, "no Gmail business calls recorded"


def test_gmail_message_sent():
    assert count_endpoint(GMAIL_API_URL, "POST", "/messages/send") > 0, "gmail send endpoint was invoked"


def test_alpaca_order_placed():
    assert count_endpoint(ALPACA_API_URL, "POST", "/v2/orders") > 0, "alpaca order endpoint was invoked"


def test_coinbase_trade_placed():
    assert count_endpoint(COINBASE_API_URL, "POST", "/buys") + count_endpoint(COINBASE_API_URL, "POST", "/sells") > 0, "coinbase buy or sell endpoint was invoked"


def test_distractor_apis_touched():
    candidates = [
        ("docusign-api", DOCUSIGN_API_URL),
        ("whatsapp-api", WHATSAPP_API_URL),
        ("amadeus-api", AMADEUS_API_URL),
        ("airbnb-api", AIRBNB_API_URL),
        ("zillow-api", ZILLOW_API_URL),
        ("trello-api", TRELLO_API_URL),
        ("mailchimp-api", MAILCHIMP_API_URL),
    ]
    touched = [name for name, url in candidates if business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
