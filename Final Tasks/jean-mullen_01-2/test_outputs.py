import json
import os
from urllib.request import Request, urlopen

# URL constants - Required APIs
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
FIGMA_API_URL = os.environ.get("FIGMA_API_URL", "http://localhost:8079")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8028")

# Distractor APIs
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8076")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
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


def business_calls(base_url):
    try:
        summary = api_get(base_url, "/audit/summary")
        endpoints = summary.get("endpoints", {})
        count = 0
        for endpoint_key, stats in endpoints.items():
            if "/audit" not in endpoint_key and "/health" not in endpoint_key:
                count += stats.get("count", 0)
        return count
    except Exception:
        return 0


def test_quickbooks_customers_read():
    audit = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    customer_calls = 0
    for key in endpoints:
        if "customer" in key.lower() or "Customer" in key:
            customer_calls += endpoints[key].get("count", 0)
    assert customer_calls > 0, "QuickBooks customers endpoint was not queried"


def test_quickbooks_invoices_read():
    audit = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    invoice_calls = 0
    for key in endpoints:
        if "invoice" in key.lower() or "Invoice" in key:
            invoice_calls += endpoints[key].get("count", 0)
    assert invoice_calls > 0, "QuickBooks invoices endpoint was not queried"


def test_stripe_customers_read():
    audit = api_get(STRIPE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    customer_calls = 0
    for key in endpoints:
        if "customer" in key.lower():
            customer_calls += endpoints[key].get("count", 0)
    assert customer_calls > 0, "Stripe customers endpoint was not queried"


def test_stripe_invoices_read():
    audit = api_get(STRIPE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    invoice_calls = 0
    for key in endpoints:
        if "invoice" in key.lower():
            invoice_calls += endpoints[key].get("count", 0)
    assert invoice_calls > 0, "Stripe invoices endpoint was not queried"


def test_docusign_envelopes_read():
    audit = api_get(DOCUSIGN_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    envelope_calls = 0
    for key in endpoints:
        if "envelope" in key.lower():
            envelope_calls += endpoints[key].get("count", 0)
    assert envelope_calls > 0, "DocuSign envelopes endpoint was not queried"


def test_eventbrite_events_read():
    audit = api_get(EVENTBRITE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    event_calls = 0
    for key in endpoints:
        if "event" in key.lower():
            event_calls += endpoints[key].get("count", 0)
    assert event_calls > 0, "Eventbrite events endpoint was not queried"


def test_eventbrite_attendees_read():
    audit = api_get(EVENTBRITE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    attendee_calls = 0
    for key in endpoints:
        if "attendee" in key.lower():
            attendee_calls += endpoints[key].get("count", 0)
    assert attendee_calls > 0, "Eventbrite attendees endpoint was not queried"


def test_google_calendar_events_read():
    audit = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    event_calls = 0
    for key in endpoints:
        if "event" in key.lower() or "calendar" in key.lower():
            event_calls += endpoints[key].get("count", 0)
    assert event_calls > 0, "Google Calendar events endpoint was not queried"



def test_deliverable_financial_brief_exists():
    path = os.path.join(os.environ.get("WORKSPACE", "/workspace"), "financial_reconciliation_brief.md")
    assert file_exists(path), f"Deliverable not found: {path}"


def test_deliverable_contract_summary_exists():
    path = os.path.join(os.environ.get("WORKSPACE", "/workspace"), "contract_commitment_summary.md")
    assert file_exists(path), f"Deliverable not found: {path}"


def test_distractor_apis_touched():
    distractors = [
        ("spotify-api", SPOTIFY_API_URL),
        ("openweather-api", OPENWEATHER_API_URL),
        ("amadeus-api", AMADEUS_API_URL),
        ("strava-api", STRAVA_API_URL),
        ("myfitnesspal-api", MYFITNESSPAL_API_URL),
        ("youtube-api", YOUTUBE_API_URL),
        ("wordpress-api", WORDPRESS_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
    ]
    touched = []
    for name, url in distractors:
        if business_calls(url) > 0:
            touched.append(name)
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
