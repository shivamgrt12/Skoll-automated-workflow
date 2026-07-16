import json
import os
from urllib.request import Request, urlopen

GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8046")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8047")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8049")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8004")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8050")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8052")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8008")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8057")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "http://localhost:8063")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8026")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8034")
DOORDASH_API_URL = os.environ.get("DOORDASH_API_URL", "http://localhost:8037")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8029")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8048")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8044")
VIMEO_API_URL = os.environ.get("VIMEO_API_URL", "http://localhost:8051")


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
        for key, val in endpoints.items():
            if "/audit" not in key and "/health" not in key:
                count += val.get("count", 0)
        return count
    except Exception:
        return 0


def test_behavioral_gmail_messages_read():
    audit = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "messages" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Gmail messages were not queried"


def test_behavioral_plaid_accounts_read():
    audit = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "accounts" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Plaid accounts were not queried"


def test_behavioral_plaid_transactions_read():
    audit = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "transactions" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Plaid transactions were not queried"


def test_behavioral_paypal_payouts_read():
    audit = api_get(PAYPAL_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "payout" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "PayPal payouts were not queried"


def test_behavioral_eventbrite_events_read():
    audit = api_get(EVENTBRITE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "event" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Eventbrite events were not queried"


def test_behavioral_airtable_records_read():
    audit = api_get(AIRTABLE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "record" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Airtable records were not queried"


def test_behavioral_google_calendar_events_read():
    audit = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "event" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Google Calendar events were not queried"


def test_behavioral_stripe_charges_read():
    audit = api_get(STRIPE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and ("charge" in key.lower() or "payment" in key.lower()):
            read_count += val.get("count", 0)
    assert read_count > 0, "Stripe charges/payments were not queried"


def test_behavioral_xero_invoices_read():
    audit = api_get(XERO_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "invoice" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Xero invoices were not queried"


def test_behavioral_asana_tasks_read():
    audit = api_get(ASANA_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "task" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Asana tasks were not queried"


def test_behavioral_vimeo_videos_read():
    audit = api_get(VIMEO_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and "video" in key.lower():
            read_count += val.get("count", 0)
    assert read_count > 0, "Vimeo videos were not queried"


def test_behavioral_notion_pages_read():
    audit = api_get(NOTION_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_count = 0
    for key, val in endpoints.items():
        if "GET" in key and ("page" in key.lower() or "database" in key.lower() or "block" in key.lower()):
            read_count += val.get("count", 0)
    assert read_count > 0, "Notion pages/databases were not queried"


def test_distractor_apis_touched():
    distractor_services = [
        ("ring-api", RING_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("discord-api", DISCORD_API_URL),
        ("telegram-api", TELEGRAM_API_URL),
        ("whatsapp-api", WHATSAPP_API_URL),
        ("twilio-api", TWILIO_API_URL),
        ("yelp-api", YELP_API_URL),
        ("doordash-api", DOORDASH_API_URL),
    ]
    touched = []
    for name, url in distractor_services:
        calls = business_calls(url)
        if calls > 0:
            touched.append(name)
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
