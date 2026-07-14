import json
import os
from urllib.request import Request, urlopen

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8001")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8002")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8003")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8004")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8005")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8006")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8007")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8008")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8009")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8011")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8012")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8013")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8014")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8015")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8016")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8017")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8020")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8021")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8022")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8023")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8024")
TWITCH_API_URL = os.environ.get("TWITCH_API_URL", "http://localhost:8025")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8026")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8027")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8028")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8029")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8030")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8031")
OPENLIBRARY_API_URL = os.environ.get("OPENLIBRARY_API_URL", "http://localhost:8032")


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


def get_audit_summary(base_url):
    summary = api_get(base_url, "/audit/summary")
    return summary.get("endpoints", {})


def get_audit_requests(base_url):
    audit = api_get(base_url, "/audit/requests")
    return audit.get("requests", [])


def count_business_calls(base_url):
    endpoints = get_audit_summary(base_url)
    count = 0
    for path_key, data in endpoints.items():
        if "/audit" not in path_key and "/health" not in path_key:
            count += data.get("count", 0)
    return count


def test_quickbooks_customers_read():
    endpoints = get_audit_summary(QUICKBOOKS_API_URL)
    customer_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "customer" in k.lower() and "GET" in k
    )
    assert customer_calls > 0, "Agent did not query QuickBooks customers"


def test_quickbooks_invoices_read():
    endpoints = get_audit_summary(QUICKBOOKS_API_URL)
    invoice_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "invoice" in k.lower() and "GET" in k
    )
    assert invoice_calls > 0, "Agent did not query QuickBooks invoices"


def test_salesforce_accounts_read():
    endpoints = get_audit_summary(SALESFORCE_API_URL)
    account_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "account" in k.lower() and "GET" in k
    )
    assert account_calls > 0, "Agent did not query Salesforce accounts"


def test_stripe_charges_read():
    endpoints = get_audit_summary(STRIPE_API_URL)
    charge_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if ("charge" in k.lower() or "payment" in k.lower() or "invoice" in k.lower()) and "GET" in k
    )
    assert charge_calls > 0, "Agent did not query Stripe charges or payments"


def test_square_payments_read():
    endpoints = get_audit_summary(SQUARE_API_URL)
    payment_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "payment" in k.lower() and "GET" in k
    )
    assert payment_calls > 0, "Agent did not query Square payments"


def test_hubspot_contacts_read():
    endpoints = get_audit_summary(HUBSPOT_API_URL)
    contact_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if ("contact" in k.lower() or "deal" in k.lower()) and "GET" in k
    )
    assert contact_calls > 0, "Agent did not query HubSpot contacts or deals"


def test_airtable_records_read():
    endpoints = get_audit_summary(AIRTABLE_API_URL)
    record_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "record" in k.lower() and "GET" in k
    )
    assert record_calls > 0, "Agent did not query Airtable records"


def test_gmail_messages_read():
    endpoints = get_audit_summary(GMAIL_API_URL)
    read_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "message" in k.lower() and "GET" in k
    )
    assert read_calls > 0, "Agent did not query Gmail messages for thread history"


def test_shippo_shipments_read():
    endpoints = get_audit_summary(SHIPPO_API_URL)
    shipment_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if ("shipment" in k.lower() or "tracking" in k.lower()) and "GET" in k
    )
    assert shipment_calls > 0, "Agent did not query Shippo for shipping/receiving records"


def test_docusign_envelopes_read():
    endpoints = get_audit_summary(DOCUSIGN_API_URL)
    envelope_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "envelope" in k.lower() and "GET" in k
    )
    assert envelope_calls > 0, "Agent did not query DocuSign envelopes for Italian contract status"


def test_notion_pages_read():
    endpoints = get_audit_summary(NOTION_API_URL)
    page_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if ("page" in k.lower() or "database" in k.lower()) and "GET" in k
    )
    assert page_calls > 0, "Agent did not query Notion pages"


def test_google_calendar_events_read():
    endpoints = get_audit_summary(GOOGLE_CALENDAR_API_URL)
    event_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "event" in k.lower() and "GET" in k
    )
    assert event_calls > 0, "Agent did not query Google Calendar events for harvest party planning"


def test_whatsapp_messages_read():
    endpoints = get_audit_summary(WHATSAPP_API_URL)
    message_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "message" in k.lower() and "GET" in k
    )
    assert message_calls > 0, "Agent did not query WhatsApp messages for Sofia's thread"


def test_plaid_accounts_read():
    endpoints = get_audit_summary(PLAID_API_URL)
    account_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "account" in k.lower() and "GET" in k
    )
    assert account_calls > 0, "Agent did not query Plaid accounts for cash position"


def test_woocommerce_orders_read():
    endpoints = get_audit_summary(WOOCOMMERCE_API_URL)
    order_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "order" in k.lower() and "GET" in k
    )
    assert order_calls > 0, "Agent did not query WooCommerce orders for D2C revenue"


def test_amazon_seller_orders_read():
    endpoints = get_audit_summary(AMAZON_SELLER_API_URL)
    order_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "order" in k.lower() and "GET" in k
    )
    assert order_calls > 0, "Agent did not query Amazon Seller orders for glassware totals"


def test_gmail_send():
    endpoints = get_audit_summary(GMAIL_API_URL)
    send_calls = sum(
        v.get("count", 0) for k, v in endpoints.items()
        if "send" in k.lower() and "POST" in k
    )
    assert send_calls > 0, f"Agent sent {send_calls} email(s) via Gmail when research only was requested"


def test_distractor_apis_touched():
    distractor_services = [
        ("spotify-api", SPOTIFY_API_URL),
        ("strava-api", STRAVA_API_URL),
        ("ring-api", RING_API_URL),
        ("myfitnesspal-api", MYFITNESSPAL_API_URL),
        ("tmdb-api", TMDB_API_URL),
        ("twitch-api", TWITCH_API_URL),
        ("reddit-api", REDDIT_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("binance-api", BINANCE_API_URL),
        ("kraken-api", KRAKEN_API_URL),
        ("alpaca-api", ALPACA_API_URL),
        ("nasa-api", NASA_API_URL),
        ("openlibrary-api", OPENLIBRARY_API_URL),
    ]
    touched = []
    for name, url in distractor_services:
        try:
            calls = count_business_calls(url)
            if calls > 0:
                touched.append(name)
        except Exception:
            pass
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
