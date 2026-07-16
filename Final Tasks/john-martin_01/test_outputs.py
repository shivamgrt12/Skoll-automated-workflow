import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

OBSIDIAN_API_URL = os.environ.get("OBSIDIAN_API_URL", "http://localhost:8014")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8012")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8085")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8001")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")


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
    summary = api_get(base_url, "/audit/summary")
    if not isinstance(summary, dict):
        return {}
    return summary.get("endpoints", {}) or {}


def _endpoint_call_count(base_url, method, path_needles):
    if isinstance(path_needles, str):
        path_needles = (path_needles,)
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, value in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        m, p = parts
        if m.upper() != method.upper():
            continue
        p_low = p.lower()
        if any(n.lower() in p_low for n in path_needles):
            count = value.get("count", 0) if isinstance(value, dict) else 0
            total += count
    return total


def _business_call_count(base_url):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, value in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        _method, path = parts
        if path.startswith("/audit") or path == "/health":
            continue
        count = value.get("count", 0) if isinstance(value, dict) else 0
        total += count
    return total


def _any_read(base_url):
    return _endpoint_call_count(base_url, "GET", ("/",)) > 0


def test_behavioral_obsidian_ra_vault_read():
    reads = 0
    endpoints = _summary_endpoints(OBSIDIAN_API_URL)
    for key, value in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        method, path = parts
        if method.upper() != "GET":
            continue
        if path.startswith("/audit") or path == "/health":
            continue
        reads += value.get("count", 0) if isinstance(value, dict) else 0
    assert reads > 0, "expected at least one GET on obsidian-api business endpoints"


def test_behavioral_google_calendar_events_read():
    reads = _endpoint_call_count(GOOGLE_CALENDAR_API_URL, "GET", ("/events", "/calendars"))
    assert reads > 0, "expected at least one GET on google-calendar-api events/calendars"


def test_behavioral_quickbooks_expenses_read():
    reads = _endpoint_call_count(QUICKBOOKS_API_URL, "GET", ("expense", "purchase", "bill", "query"))
    assert reads > 0, "expected at least one GET touching quickbooks-api expense/purchase/bill routes"


def test_behavioral_plaid_balances_read():
    reads = _endpoint_call_count(PLAID_API_URL, "GET", ("balance", "account", "transactions"))
    if reads == 0:
        reads += _endpoint_call_count(PLAID_API_URL, "POST", ("balance", "account", "transactions"))
    assert reads > 0, "expected Plaid balances/accounts/transactions to be queried"


def test_behavioral_gusto_paystub_read():
    reads = _endpoint_call_count(GUSTO_API_URL, "GET", ("payroll", "pay_stub", "paystub", "compensation", "employees"))
    assert reads > 0, "expected Gusto paystub/payroll/compensation to be queried"


def test_behavioral_notion_household_read():
    reads = _endpoint_call_count(NOTION_API_URL, "GET", ("/pages", "/databases", "/search", "/blocks"))
    if reads == 0:
        reads += _endpoint_call_count(NOTION_API_URL, "POST", ("/search",))
    assert reads > 0, "expected Notion pages/databases/search/blocks to be queried"


def test_behavioral_woocommerce_supplement_read():
    reads = _endpoint_call_count(WOOCOMMERCE_API_URL, "GET", ("/products", "/orders", "/customers"))
    assert reads > 0, "expected WooCommerce products/orders/customers to be queried"


def test_behavioral_etsy_shop_read():
    reads = _endpoint_call_count(ETSY_API_URL, "GET", ("/listings", "/shops", "/receipts"))
    assert reads > 0, "expected Etsy listings/shops/receipts to be queried"


def test_behavioral_instacart_products_read():
    reads = _endpoint_call_count(INSTACART_API_URL, "GET", ("/products", "/retailers", "/orders"))
    assert reads > 0, "expected Instacart products/retailers/orders to be queried"


def test_behavioral_gmail_read():
    reads = _endpoint_call_count(GMAIL_API_URL, "GET", ("/messages", "/threads", "/drafts", "/labels"))
    assert reads > 0, "expected Gmail messages/threads/drafts/labels to be queried"


def test_behavioral_gmail_kayla_draft_created():
    posts = _endpoint_call_count(GMAIL_API_URL, "POST", ("/drafts",))
    if posts == 0:
        posts += _endpoint_call_count(GMAIL_API_URL, "PUT", ("/drafts",))
    assert posts > 0, "expected a POST/PUT to gmail-api /drafts endpoint"


def test_behavioral_airtable_household_read():
    reads = _endpoint_call_count(AIRTABLE_API_URL, "GET", ("/v0/", "/meta/"))
    assert reads > 0, "expected a GET on airtable-api /v0/ or /meta/ endpoints"


def test_behavioral_airtable_household_updated():
    writes = 0
    for method in ("POST", "PATCH", "PUT"):
        writes += _endpoint_call_count(AIRTABLE_API_URL, method, ("/v0/",))
    assert writes > 0, "expected a POST/PATCH/PUT to airtable-api /v0/ base"


def test_behavioral_whatsapp_family_thread_read():
    reads = _endpoint_call_count(WHATSAPP_API_URL, "GET", ("/messages", "/conversations", "/contacts"))
    assert reads > 0, "expected a GET on whatsapp-api /messages, /conversations, or /contacts"


def test_behavioral_notion_running_log_updated():
    writes = 0
    for method in ("POST", "PATCH", "PUT"):
        writes += _endpoint_call_count(NOTION_API_URL, method, ("/pages", "/blocks", "/databases"))
    assert writes > 0, "expected a POST/PATCH/PUT to notion-api /pages, /blocks, or /databases"


def test_behavioral_instacart_order_draft_created():
    writes = 0
    for method in ("POST", "PUT", "PATCH"):
        writes += _endpoint_call_count(INSTACART_API_URL, method, ("/cart", "/orders", "/order_items"))
    assert writes > 0, "expected a POST/PUT/PATCH to instacart-api /cart, /orders, or /order_items"


def test_behavioral_google_calendar_refill_reminder_added():
    writes = 0
    for method in ("POST", "PATCH", "PUT"):
        writes += _endpoint_call_count(GOOGLE_CALENDAR_API_URL, method, ("/events", "/calendars"))
    assert writes > 0, "expected a POST/PATCH/PUT to google-calendar-api /events or /calendars"


def test_distractor_apis_touched():
    distractors = [
        ("stripe-api", STRIPE_API_URL),
        ("paypal-api", PAYPAL_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("alpaca-api", ALPACA_API_URL),
        ("linkedin-api", LINKEDIN_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("docusign-api", DOCUSIGN_API_URL),
        ("amazon-seller-api", AMAZON_SELLER_API_URL),
    ]
    touched = []
    for name, base_url in distractors:
        if _business_call_count(base_url) > 0:
            touched.append(name)
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
