import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8076")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8089")
ZENDESK_API_URL = os.environ.get("ZENDESK_API_URL", "http://localhost:8025")
GITHUB_API_URL = os.environ.get("GITHUB_API_URL", "http://localhost:8019")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8029")


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


def _summary_endpoints(base_url):
    data = api_get(base_url, "/audit/summary")
    endpoints = data.get("endpoints", {}) if isinstance(data, dict) else {}
    return endpoints if isinstance(endpoints, dict) else {}


def business_calls(base_url):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        low = key.lower()
        if "/audit" in low or "/health" in low:
            continue
        total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def get_calls(base_url):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        low = key.lower()
        if "/audit" in low or "/health" in low:
            continue
        if not key.upper().startswith("GET "):
            continue
        total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def write_calls(base_url):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        method = parts[0].upper()
        path = parts[1].lower() if len(parts) > 1 else ""
        if "/audit" in path or "/health" in path:
            continue
        if method in ("POST", "PUT", "PATCH", "DELETE"):
            total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def mutation_path_hits(base_url, needles):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        method = parts[0].upper()
        path = parts[1].lower() if len(parts) > 1 else ""
        if "/audit" in path or "/health" in path:
            continue
        if method not in ("POST", "PUT", "PATCH", "DELETE"):
            continue
        if any(n in path for n in needles):
            total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def retrieved(base_url, needles):
    data = api_get(base_url, "/audit/requests")
    entries = data.get("requests", []) if isinstance(data, dict) else []
    for entry in entries:
        path = str(entry.get("path", "")).lower()
        if "/audit" in path or "/health" in path:
            continue
        body = entry.get("response_body")
        if body is None:
            continue
        if isinstance(body, (dict, list)):
            blob = json.dumps(body)
        else:
            try:
                blob = json.dumps(json.loads(body))
            except Exception:
                blob = str(body)
        if any(n in blob for n in needles):
            return True
    return False


def test_stripe_subscription_states_retrieved():
    assert retrieved(STRIPE_API_URL, ["sub_Verdant", "past_due"]), "agent did not retrieve stripe subscription states for the roster reconciliation"


def test_stripe_collected_charges_retrieved():
    assert retrieved(STRIPE_API_URL, ["succeeded"]), "agent did not retrieve settled stripe charges for the collected-cash figure"


def test_xero_booked_invoices_retrieved():
    assert retrieved(XERO_API_URL, ["AUTHORISED", "SUBMITTED"]), "agent did not retrieve booked xero invoices for the collected-vs-billed comparison"


def test_plaid_cleared_transactions_retrieved():
    assert retrieved(PLAID_API_URL, ["Irene Reeves", "Mortgage payment"]), "agent did not retrieve cleared plaid transactions for the household reconciliation"


def test_quickbooks_budget_retrieved():
    assert retrieved(QUICKBOOKS_API_URL, ["Watson"]), "agent did not retrieve the quickbooks household budget records"


def test_coinbase_btc_retrieved():
    assert retrieved(COINBASE_API_URL, ["BTC", "Bitcoin"]), "agent did not retrieve the coinbase bitcoin gift allocation"


def test_zillow_home_retrieved():
    assert retrieved(ZILLOW_API_URL, ["78739", "Circle C Ranch"]), "agent did not retrieve the zillow home value for the net-worth snapshot"


def test_alpaca_index_retrieved():
    assert retrieved(ALPACA_API_URL, ["VTI", "VOO"]), "agent did not retrieve the alpaca index-fund position"


def test_kraken_staked_eth_retrieved():
    assert retrieved(KRAKEN_API_URL, ["XETH"]), "agent did not retrieve the kraken staked ethereum position"


def test_binance_price_retrieved():
    assert retrieved(BINANCE_API_URL, ["priceChangePercent", "USDT"]), "agent did not retrieve a binance price for the crypto sanity-check"


def test_paypal_activity_retrieved():
    assert retrieved(PAYPAL_API_URL, ["COMPLETED", "351.32"]), "agent did not retrieve paypal long-tail activity"


def test_gusto_payroll_retrieved():
    assert retrieved(GUSTO_API_URL, ["Watson Piano Studio", "Studio"]), "agent did not retrieve gusto studio payroll for the profit-and-loss"


def test_hubspot_roster_retrieved():
    assert retrieved(HUBSPOT_API_URL, ["Nathan", "subscriber"]), "agent did not retrieve the hubspot nominal roster"


def test_gmail_receipts_read():
    assert get_calls(GMAIL_API_URL) > 0, "no GET reads recorded against gmail-api"


def test_outlook_receipts_read():
    assert get_calls(OUTLOOK_API_URL) > 0, "no GET reads recorded against outlook-api"


def test_financial_email_sent():
    hits = mutation_path_hits(GMAIL_API_URL, ["/send"]) + mutation_path_hits(OUTLOOK_API_URL, ["sendmail"])
    assert hits > 0, "no outbound send detected on gmail-api or outlook-api"


def test_docusign_envelope_pushed():
    assert write_calls(DOCUSIGN_API_URL) > 0, "no envelope create or route detected on docusign-api"


def test_investment_trade_placed():
    hits = mutation_path_hits(COINBASE_API_URL, ["/buys", "/sells"]) + mutation_path_hits(ALPACA_API_URL, ["/orders"])
    assert hits > 0, "no trade detected on coinbase-api or alpaca-api"


def test_stripe_write_created():
    assert write_calls(STRIPE_API_URL) > 0, "no write mutation detected on stripe-api"


def test_distractor_apis_touched():
    distractors = [
        ("salesforce-api", SALESFORCE_API_URL),
        ("airtable-api", AIRTABLE_API_URL),
        ("strava-api", STRAVA_API_URL),
        ("amadeus-api", AMADEUS_API_URL),
        ("klaviyo-api", KLAVIYO_API_URL),
        ("zendesk-api", ZENDESK_API_URL),
        ("github-api", GITHUB_API_URL),
        ("jira-api", JIRA_API_URL),
    ]
    touched = [name for name, url in distractors if business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
