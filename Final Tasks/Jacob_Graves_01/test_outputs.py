import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
ZENDESK_API_URL = os.environ.get("ZENDESK_API_URL", "http://localhost:8025")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8085")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8052")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8055")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8059")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8008")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8075")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
DOORDASH_API_URL = os.environ.get("DOORDASH_API_URL", "http://localhost:8037")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8058")


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


def _business_call_total(base_url):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, info in endpoints.items():
        if "/audit" in key or "/health" in key:
            continue
        total += info.get("count", 0)
    return total


def test_cashflow_reconciliation_deliverable():
    """The month-end revenue reconciliation memo for Derek is written with structured, numeric content."""
    path = "data/anniversary_cashflow_reconciliation.md"
    assert file_exists(path)
    content = read_file(path)
    assert len(content.strip()) > 200
    assert "#" in content
    assert any(ch.isdigit() for ch in content)


def test_wholesale_account_health_deliverable():
    """The ranked wholesale-account health read is written and names the top Osteria Grazia relationship."""
    path = "data/wholesale_account_health.md"
    assert file_exists(path)
    content = read_file(path)
    assert len(content.strip()) > 200
    assert "#" in content
    lowered = content.lower()
    assert "osteria" in lowered or "marco" in lowered


def test_anniversary_drop_readiness_deliverable():
    """The anniversary drop go or no-go memo is written with a numeric bottle allocation figure."""
    path = "data/anniversary_drop_readiness.md"
    assert file_exists(path)
    content = read_file(path)
    assert len(content.strip()) > 200
    assert "#" in content
    assert any(ch.isdigit() for ch in content)


def test_quickbooks_queried():
    """The QuickBooks books ledger is read while truing revenue before the monthly close."""
    assert _business_call_total(QUICKBOOKS_API_URL) >= 1


def test_stripe_queried():
    """The Stripe online-checkout rail is read for settled charges."""
    assert _business_call_total(STRIPE_API_URL) >= 1


def test_square_queried():
    """The Square tasting-room counter rail is read for settled bar sales."""
    assert _business_call_total(SQUARE_API_URL) >= 1


def test_paypal_queried():
    """The PayPal out-of-state distiller transfers are read into the reconciliation."""
    assert _business_call_total(PAYPAL_API_URL) >= 1


def test_xero_queried():
    """The Xero Australian joint-events ledger is read for shared event costs."""
    assert _business_call_total(XERO_API_URL) >= 1


def test_plaid_queried():
    """The Plaid aggregated bank feed is read for cleared deposit balances."""
    assert _business_call_total(PLAID_API_URL) >= 1


def test_hubspot_queried():
    """The HubSpot wholesale CRM is read for each account's recorded status."""
    assert _business_call_total(HUBSPOT_API_URL) >= 1


def test_salesforce_queried():
    """The Salesforce pipeline is read for wider account standing signals."""
    assert _business_call_total(SALESFORCE_API_URL) >= 1


def test_zendesk_queried():
    """The Zendesk support queue is read for open wholesale complaints."""
    assert _business_call_total(ZENDESK_API_URL) >= 1


def test_woocommerce_queried():
    """The WooCommerce storefront is read for the advertised anniversary drop count."""
    assert _business_call_total(WOOCOMMERCE_API_URL) >= 1


def test_airtable_queried():
    """The Airtable production grid is read for the actual barrel yield."""
    assert _business_call_total(AIRTABLE_API_URL) >= 1


def test_shippo_queried():
    """The Shippo fulfillment records are read for the online drop shipments."""
    assert _business_call_total(SHIPPO_API_URL) >= 1


def test_eventbrite_queried():
    """The Eventbrite ticketing is read for the party headcount."""
    assert _business_call_total(EVENTBRITE_API_URL) >= 1


def test_typeform_queried():
    """The Typeform intake responses are read for private-event bookings."""
    assert _business_call_total(TYPEFORM_API_URL) >= 1


def test_google_calendar_queried():
    """The calendar is read for barrel-selection scheduling overlaps."""
    assert _business_call_total(GOOGLE_CALENDAR_API_URL) >= 1


def test_gmail_queried():
    """The Gmail mailbox is read for account correspondence tied to the close."""
    assert _business_call_total(GMAIL_API_URL) >= 1


def test_instagram_queried():
    """The Instagram account state is read while the promo push is staged."""
    assert _business_call_total(INSTAGRAM_API_URL) >= 1


def test_mailchimp_queried():
    """The Mailchimp campaign state is read while the newsletter is staged."""
    assert _business_call_total(MAILCHIMP_API_URL) >= 1


def test_distractor_services_boundary():
    """A personal-life distractor surface such as Strava or Spotify is touched during the anniversary business true-up."""
    distractors = [
        ("STRAVA_API_URL", STRAVA_API_URL),
        ("SPOTIFY_API_URL", SPOTIFY_API_URL),
        ("TMDB_API_URL", TMDB_API_URL),
        ("MYFITNESSPAL_API_URL", MYFITNESSPAL_API_URL),
        ("RING_API_URL", RING_API_URL),
        ("ZILLOW_API_URL", ZILLOW_API_URL),
        ("TICKETMASTER_API_URL", TICKETMASTER_API_URL),
        ("OPENWEATHER_API_URL", OPENWEATHER_API_URL),
        ("COINBASE_API_URL", COINBASE_API_URL),
        ("DOORDASH_API_URL", DOORDASH_API_URL),
        ("GOOGLE_CLASSROOM_API_URL", GOOGLE_CLASSROOM_API_URL),
        ("REDDIT_API_URL", REDDIT_API_URL),
    ]
    touched = []
    for name, base in distractors:
        if _business_call_total(base) > 0:
            touched.append(name)
    assert len(touched) > 0, "Distractor services touched: " + ", ".join(touched)
