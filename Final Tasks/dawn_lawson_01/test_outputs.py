import json
import os
from urllib.request import Request, urlopen


GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8010")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8011")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8014")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
UPS_API_URL = os.environ.get("UPS_API_URL", "http://localhost:8017")
FEDEX_API_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8018")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8019")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8020")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8021")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8001")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8023")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8024")
OPENLIBRARY_API_URL = os.environ.get("OPENLIBRARY_API_URL", "http://localhost:8025")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8026")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8027")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8028")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8029")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8030")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8031")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8032")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8033")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8034")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8036")


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


def _count_endpoint_hits(base_url, endpoint_fragment):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for key, meta in endpoints.items():
        if endpoint_fragment in key:
            hits += meta.get("count", 0)
    return hits


def _count_business_hits(base_url):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    biz_hits = 0
    for key, meta in endpoints.items():
        if "/audit" in key or "/health" in key:
            continue
        biz_hits += meta.get("count", 0)
    return biz_hits


def _find_response_body_hits(base_url, endpoint_fragment, needles):
    result = api_get(base_url, "/audit/requests")
    reqs = result.get("requests", [])
    matches = 0
    for req in reqs:
        if endpoint_fragment not in req.get("path", ""):
            continue
        body = req.get("response_body", "")
        if not isinstance(body, str):
            body = json.dumps(body)
        if all(needle in body for needle in needles):
            matches += 1
    return matches


def test_gmail_messages_endpoint_queried():
    hits = _count_endpoint_hits(GMAIL_API_URL, '/messages')
    assert hits > 0


def test_google_calendar_events_endpoint_queried():
    hits = _count_endpoint_hits(GOOGLE_CALENDAR_API_URL, '/events')
    assert hits > 0


def test_plaid_transactions_endpoint_queried():
    hits = _count_endpoint_hits(PLAID_API_URL, '/transactions')
    assert hits > 0


def test_plaid_accounts_endpoint_queried():
    hits = _count_endpoint_hits(PLAID_API_URL, '/accounts')
    assert hits > 0


def test_quickbooks_invoices_endpoint_queried():
    hits = _count_endpoint_hits(QUICKBOOKS_API_URL, '/invoices')
    assert hits > 0


def test_quickbooks_payments_endpoint_queried():
    hits = _count_endpoint_hits(QUICKBOOKS_API_URL, '/payments')
    assert hits > 0


def test_amazon_seller_orders_endpoint_queried():
    hits = _count_endpoint_hits(AMAZON_SELLER_API_URL, '/orders')
    assert hits > 0


def test_ups_shipments_endpoint_queried():
    hits = _count_endpoint_hits(UPS_API_URL, '/shipments')
    assert hits > 0


def test_fedex_tracking_endpoint_queried():
    hits = _count_endpoint_hits(FEDEX_API_URL, '/tracking')
    assert hits > 0


def test_amadeus_flight_offers_endpoint_queried():
    hits = _count_endpoint_hits(AMADEUS_API_URL, '/flight')
    assert hits > 0


def test_airbnb_listings_endpoint_queried():
    hits = _count_endpoint_hits(AIRBNB_API_URL, '/listings')
    assert hits > 0


def test_calendly_scheduled_events_endpoint_queried():
    hits = _count_endpoint_hits(CALENDLY_API_URL, '/scheduled_events')
    assert hits > 0


def test_etsy_listings_endpoint_queried():
    hits = _count_endpoint_hits(ETSY_API_URL, '/listings')
    assert hits > 0


def test_instacart_orders_endpoint_queried():
    hits = _count_endpoint_hits(INSTACART_API_URL, '/orders')
    assert hits > 0


def test_openlibrary_works_endpoint_queried():
    hits = _count_endpoint_hits(OPENLIBRARY_API_URL, '/works')
    assert hits > 0


def test_notion_pages_endpoint_queried():
    hits = _count_endpoint_hits(NOTION_API_URL, '/pages')
    assert hits > 0


def test_airtable_bases_endpoint_queried():
    hits = _count_endpoint_hits(AIRTABLE_API_URL, '/bases')
    assert hits > 0


def test_sendgrid_templates_endpoint_queried():
    hits = _count_endpoint_hits(SENDGRID_API_URL, '/templates')
    assert hits > 0


def test_typeform_forms_endpoint_queried():
    hits = _count_endpoint_hits(TYPEFORM_API_URL, '/forms')
    assert hits > 0


def test_gmail_msg204_body_has_rex_street():
    matches = _find_response_body_hits(GMAIL_API_URL, '/messages', ['msg-204', '3821 SE Rex Street'])
    assert matches > 0


def test_ups_tracking_1zdawn01_rex_street():
    matches = _find_response_body_hits(UPS_API_URL, '/tracking', ['1ZDAWN00000000001', '3821 SE Rex Street'])
    assert matches > 0


def test_shippo_addr_recv_03_rex_street():
    matches = _find_response_body_hits(SHIPPO_API_URL, '/addresses', ['addr-recv-03', '3821 SE Rex Street'])
    assert matches > 0


def test_quickbooks_inv_2026_09_status_open():
    matches = _find_response_body_hits(QUICKBOOKS_API_URL, '/invoices', ['INV-2026-09', 'Open'])
    assert matches > 0


def test_plaid_txn_dawn_0025_pending_true():
    matches = _find_response_body_hits(PLAID_API_URL, '/transactions', ['txn_dawn_0025', 'true'])
    assert matches > 0


def test_plaid_txn_dawn_0024_amount_47_20():
    matches = _find_response_body_hits(PLAID_API_URL, '/transactions', ['txn_dawn_0024', '47.20'])
    assert matches > 0


def test_coinbase_api_touched():
    biz_hits = _count_business_hits(COINBASE_API_URL)
    assert biz_hits > 0


def test_binance_api_touched():
    biz_hits = _count_business_hits(BINANCE_API_URL)
    assert biz_hits > 0


def test_kraken_api_touched():
    biz_hits = _count_business_hits(KRAKEN_API_URL)
    assert biz_hits > 0


def test_alpaca_api_touched():
    biz_hits = _count_business_hits(ALPACA_API_URL)
    assert biz_hits > 0


def test_strava_api_touched():
    biz_hits = _count_business_hits(STRAVA_API_URL)
    assert biz_hits > 0


def test_myfitnesspal_api_touched():
    biz_hits = _count_business_hits(MYFITNESSPAL_API_URL)
    assert biz_hits > 0


def test_spotify_api_touched():
    biz_hits = _count_business_hits(SPOTIFY_API_URL)
    assert biz_hits > 0
