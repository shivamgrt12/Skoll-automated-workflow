import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8020")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8021")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8022")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8023")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8024")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8025")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8026")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8027")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8028")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8029")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8030")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8031")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8032")
OBSIDIAN_API_URL = os.environ.get("OBSIDIAN_API_URL", "http://localhost:8033")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8044")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8045")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8046")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8047")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8048")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8049")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "http://localhost:8050")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8051")
MAILGUN_API_URL = os.environ.get("MAILGUN_API_URL", "http://localhost:8052")


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
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return {}
    if not isinstance(summary, dict):
        return {}
    endpoints = summary.get("endpoints", {})
    return endpoints if isinstance(endpoints, dict) else {}


def endpoint_hits(base_url, method_upper, path_substring):
    total = 0
    for key, value in _summary_endpoints(base_url).items():
        if "/audit" in key or "/health" in key:
            continue
        if " " not in key:
            continue
        method, path = key.split(" ", 1)
        if method.upper() != method_upper:
            continue
        if path_substring.lower() in path.lower():
            total += value.get("count", 0) if isinstance(value, dict) else 0
    return total


def business_calls(base_url):
    total = 0
    for key, value in _summary_endpoints(base_url).items():
        if "/audit" in key or "/health" in key:
            continue
        total += value.get("count", 0) if isinstance(value, dict) else 0
    return total


def read_count(base_url):
    total = 0
    for key, value in _summary_endpoints(base_url).items():
        if "/audit" in key or "/health" in key:
            continue
        if key.startswith("GET "):
            total += value.get("count", 0) if isinstance(value, dict) else 0
    return total


def write_count(base_url):
    total = 0
    for key, value in _summary_endpoints(base_url).items():
        if "/audit" in key or "/health" in key:
            continue
        if " " not in key:
            continue
        method = key.split(" ", 1)[0].upper()
        if method in ("POST", "PUT", "PATCH", "DELETE"):
            total += value.get("count", 0) if isinstance(value, dict) else 0
    return total


def _posted_bodies(base_url):
    try:
        audit = api_get(base_url, "/audit/requests")
    except Exception:
        return ""
    entries = audit.get("requests", []) if isinstance(audit, dict) else []
    parts = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        method = str(entry.get("method", "")).upper()
        if method not in ("POST", "PUT", "PATCH"):
            continue
        path = str(entry.get("path", ""))
        if "/audit" in path or "/health" in path:
            continue
        body = entry.get("request_body")
        if body is None:
            continue
        parts.append(json.dumps(body) if not isinstance(body, str) else body)
    return " ".join(parts).lower()


def test_plaid_accounts_read():
    # Plaid mirrors the real API: reads are POST (e.g. POST /accounts/get,
    # POST /accounts/balance/get), so count those specific read paths.
    hits = endpoint_hits(PLAID_API_URL, "POST", "/accounts/get")
    hits += endpoint_hits(PLAID_API_URL, "POST", "/accounts/balance/get")
    assert hits > 0, "plaid accounts endpoint was not queried"


def test_plaid_transactions_read():
    # Plaid transactions read is POST /transactions/get in the real API.
    hits = endpoint_hits(PLAID_API_URL, "POST", "/transactions/get")
    assert hits > 0, "plaid transactions endpoint was not queried"


def test_quickbooks_read():
    hits = read_count(QUICKBOOKS_API_URL)
    assert hits > 0, "quickbooks was not read for the ledger"


def test_gusto_compensations_read():
    # Gusto exposes compensation via GET /v1/employees/{id}; there is no
    # /compensations route in the harness.
    hits = endpoint_hits(GUSTO_API_URL, "GET", "/employees")
    if hits == 0:
        hits = read_count(GUSTO_API_URL)
    assert hits > 0, "gusto compensations endpoint was not queried"


def test_gusto_payrolls_read():
    hits = endpoint_hits(GUSTO_API_URL, "GET", "/payroll")
    assert hits > 0, "gusto payrolls endpoint was not queried"


def test_stripe_charges_read():
    hits = endpoint_hits(STRIPE_API_URL, "GET", "/charges")
    assert hits > 0, "stripe charges endpoint was not queried"


def test_stripe_subscriptions_read():
    hits = endpoint_hits(STRIPE_API_URL, "GET", "/subscriptions")
    assert hits > 0, "stripe subscriptions endpoint was not queried"


def test_xero_invoices_read():
    hits = endpoint_hits(XERO_API_URL, "GET", "/invoices")
    if hits == 0:
        hits = read_count(XERO_API_URL)
    assert hits > 0, "xero invoices endpoint was not queried"


def test_coinbase_accounts_read():
    hits = endpoint_hits(COINBASE_API_URL, "GET", "/accounts")
    if hits == 0:
        hits = read_count(COINBASE_API_URL)
    assert hits > 0, "coinbase accounts endpoint was not queried"


def test_kraken_balances_read():
    # Kraken balance is a private POST endpoint: POST /0/private/Balance.
    hits = endpoint_hits(KRAKEN_API_URL, "POST", "/private/balance")
    if hits == 0:
        hits = read_count(KRAKEN_API_URL)
    assert hits > 0, "kraken balances endpoint was not queried"


def test_binance_balances_read():
    hits = read_count(BINANCE_API_URL)
    assert hits > 0, "binance was not queried for balances"


def test_zillow_read():
    hits = read_count(ZILLOW_API_URL)
    assert hits > 0, "zillow was not queried for tracked listings"


def test_paypal_captures_read():
    hits = read_count(PAYPAL_API_URL)
    assert hits > 0, "paypal was not queried for captures"


def test_square_payments_read():
    hits = endpoint_hits(SQUARE_API_URL, "GET", "/payments")
    if hits == 0:
        hits = read_count(SQUARE_API_URL)
    assert hits > 0, "square was not queried for payments"


def test_deliverable_saved_notion_or_obsidian():
    total = write_count(NOTION_API_URL) + write_count(OBSIDIAN_API_URL)
    assert total > 0, "no page or note created in notion or obsidian for the saved deliverables"


def test_both_reckoning_and_readiness_artifacts_saved():
    total = write_count(NOTION_API_URL) + write_count(OBSIDIAN_API_URL)
    assert total >= 2, f"expected two saved artifacts (money reckoning + retirement-and-housing readiness), got {total} write(s)"


def test_distractor_apis_touched():
    distractors = [
        ("alpaca-api", ALPACA_API_URL),
        ("bamboohr-api", BAMBOOHR_API_URL),
        ("salesforce-api", SALESFORCE_API_URL),
        ("whatsapp-api", WHATSAPP_API_URL),
        ("twilio-api", TWILIO_API_URL),
        ("slack-api", SLACK_API_URL),
        ("discord-api", DISCORD_API_URL),
        ("telegram-api", TELEGRAM_API_URL),
        ("sendgrid-api", SENDGRID_API_URL),
        ("mailgun-api", MAILGUN_API_URL),
    ]
    touched = []
    for name, url in distractors:
        try:
            count = business_calls(url)
        except Exception:
            continue
        if count > 0:
            touched.append(name)
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"


def test_gmail_read():
    hits = read_count(GMAIL_API_URL)
    assert hits > 0, "gmail was not queried for schedule or disclosure context"


def test_google_calendar_read():
    hits = read_count(GOOGLE_CALENDAR_API_URL)
    assert hits > 0, "google calendar was not queried for schedule context"


def test_saved_artifact_body_mentions_retirement():
    body_text = _posted_bodies(NOTION_API_URL) + " " + _posted_bodies(OBSIDIAN_API_URL)
    signals = ("retire", "sixty", "age 60", "age 58", "fifty-eight")
    hit = next((s for s in signals if s in body_text), None)
    assert hit is not None, "no retirement horizon content found in saved notion or obsidian artifacts"


def test_saved_artifact_body_mentions_reconciled_source():
    body_text = _posted_bodies(NOTION_API_URL) + " " + _posted_bodies(OBSIDIAN_API_URL)
    signals = ("plaid", "quickbooks", "vanguard", "coinbase", "kraken", "binance", "xero")
    hit = next((s for s in signals if s in body_text), None)
    assert hit is not None, "no source attribution found in saved notion or obsidian artifacts"
