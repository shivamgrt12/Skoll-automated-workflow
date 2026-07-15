import json
import os
import re
import subprocess
import sqlite3
from urllib.request import Request, urlopen

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")

OUTPUT_DIR = os.environ.get("AGENT_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "output"))


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


def business_calls(base_url):
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return 0
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    total = 0
    for key, info in endpoints.items():
        parts = key.split(" ", 1)
        path = parts[1] if len(parts) == 2 else key
        if path.startswith("/audit") or path == "/health":
            continue
        count = info.get("count", 0) if isinstance(info, dict) else 0
        total += count
    return total


def find_deliverable(*name_fragments):
    frags = [f.lower() for f in name_fragments]
    if not os.path.isdir(OUTPUT_DIR):
        return None
    for root, _dirs, files in os.walk(OUTPUT_DIR):
        for fn in files:
            low = fn.lower()
            if all(f in low for f in frags):
                return os.path.join(root, fn)
    return None


def all_output_text():
    chunks = []
    if not os.path.isdir(OUTPUT_DIR):
        return ""
    for root, _dirs, files in os.walk(OUTPUT_DIR):
        for fn in files:
            try:
                with open(os.path.join(root, fn), encoding="utf-8", errors="ignore") as f:
                    chunks.append(f.read())
            except Exception:
                continue
    return "\n".join(chunks)


def _cash_position_file():
    return (
        find_deliverable("cash", "position")
        or find_deliverable("household", "cash")
        or find_deliverable("reconcil")
    )


def _tax_summary_file():
    return (
        find_deliverable("tax")
        or find_deliverable("side", "business")
        or find_deliverable("earnings")
    )


def test_quickbooks_records_read():
    assert business_calls(QUICKBOOKS_API_URL) > 0, "no QuickBooks business calls recorded"


def test_plaid_feed_read():
    assert business_calls(PLAID_API_URL) > 0, "no Plaid business calls recorded"


def test_zillow_comps_read():
    assert business_calls(ZILLOW_API_URL) > 0, "no Zillow business calls recorded"


def test_second_book_or_rail_read():
    total = (
        business_calls(XERO_API_URL)
        + business_calls(STRIPE_API_URL)
        + business_calls(SQUARE_API_URL)
        + business_calls(PAYPAL_API_URL)
    )
    assert total > 0, "no cross-source rail (xero/stripe/square/paypal) calls recorded"


def test_gmail_receipts_read():
    assert business_calls(GMAIL_API_URL) > 0, "no Gmail business calls recorded"


def test_calendar_jobs_read():
    assert business_calls(GOOGLE_CALENDAR_API_URL) > 0, "no Google Calendar business calls recorded"


def test_notion_playbook_read():
    assert business_calls(NOTION_API_URL) > 0, "no Notion business calls recorded"


def test_airtable_vendors_read():
    assert business_calls(AIRTABLE_API_URL) > 0, "no Airtable business calls recorded"


def test_docusign_contracts_read():
    assert business_calls(DOCUSIGN_API_URL) > 0, "no DocuSign business calls recorded"


def test_cash_position_deliverable_exists():
    assert _cash_position_file() is not None, "household cash-position deliverable not found in output dir"


def test_cash_position_has_client_lines():
    path = _cash_position_file()
    assert path is not None, "household cash-position deliverable not found"
    text = read_file(path).lower()
    named = [n for n in ["tony", "keisha", "sandra", "carla", "miguel"] if n in text]
    assert len(named) >= 3, f"reconciliation names too few clients: {named}"


def test_cash_position_reports_totals():
    path = _cash_position_file()
    assert path is not None, "household cash-position deliverable not found"
    text = read_file(path).lower()
    assert "collect" in text, "no collected total present"
    assert "outstand" in text or "owed" in text or "balance" in text, "no outstanding total present"


def test_cash_position_tony_balance():
    path = _cash_position_file()
    assert path is not None, "household cash-position deliverable not found"
    text = read_file(path)
    assert "1664.29" in text or "1,664.29" in text, "Tony Rizzi 1664.29 outstanding figure missing"


def test_cash_position_keisha_balance():
    path = _cash_position_file()
    assert path is not None, "household cash-position deliverable not found"
    text = read_file(path)
    assert re.search(r"(?<![\d,.])985\.00(?![\d])", text) or re.search(r"(?<![\d,.])985(?![\d,.])", text), \
        "Keisha Washington 985.00 outstanding figure missing"


def test_cash_position_shows_profit_line():
    path = _cash_position_file()
    assert path is not None, "household cash-position deliverable not found"
    text = read_file(path).lower()
    assert "profit" in text or "net" in text, "no profit/net line present in reconciliation"


def test_tax_summary_deliverable_exists():
    assert _tax_summary_file() is not None, "side-business tax summary deliverable not found in output dir"


def test_tax_summary_has_costs_section():
    path = _tax_summary_file()
    assert path is not None, "side-business tax summary deliverable not found"
    text = read_file(path).lower()
    assert "cost" in text or "expense" in text, "tax summary lacks a costs/expenses section"
    assert "earn" in text or "income" in text or "revenue" in text or "collect" in text, "tax summary lacks an earnings section"


def test_equity_read_present():
    text = all_output_text().lower()
    assert "equity" in text or "mortgage" in text, "no row-house equity read present in output"


def test_distractor_apis_touched():
    distractors = [
        ("alpaca-api", ALPACA_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("gusto-api", GUSTO_API_URL),
        ("hubspot-api", HUBSPOT_API_URL),
        ("wordpress-api", WORDPRESS_API_URL),
        ("binance-api", BINANCE_API_URL),
    ]
    touched = [name for name, url in distractors if business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
