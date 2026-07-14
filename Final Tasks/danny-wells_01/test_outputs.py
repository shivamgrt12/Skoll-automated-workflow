import json
import os
from urllib.request import Request, urlopen

AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8001")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8002")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8003")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8004")
FRESHDESK_API_URL = os.environ.get("FRESHDESK_API_URL", "http://localhost:8005")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8006")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8007")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8008")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8009")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8010")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8011")
PAGERDUTY_API_URL = os.environ.get("PAGERDUTY_API_URL", "http://localhost:8012")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8013")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8014")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8015")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8016")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8017")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8018")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8019")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8020")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8021")


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


def _summary(base_url):
    try:
        return api_get(base_url, "/audit/summary")
    except Exception:
        return {}


def _endpoints(base_url):
    summary = _summary(base_url)
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    return endpoints or {}


def read_count(base_url):
    endpoints = _endpoints(base_url)
    total = 0
    for key, info in endpoints.items():
        if key.startswith("GET /audit") or key.startswith("GET /health"):
            continue
        if key.startswith("GET "):
            total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def write_count(base_url, method="POST"):
    endpoints = _endpoints(base_url)
    total = 0
    prefix = f"{method} "
    for key, info in endpoints.items():
        if key.startswith(f"{method} /audit"):
            continue
        if key.startswith(prefix):
            total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def endpoint_count(base_url, method, needle):
    endpoints = _endpoints(base_url)
    total = 0
    prefix = f"{method} "
    for key, info in endpoints.items():
        if not key.startswith(prefix):
            continue
        path = key[len(prefix):]
        if needle.lower() in path.lower():
            total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def business_calls(base_url):
    endpoints = _endpoints(base_url)
    total = 0
    for key, info in endpoints.items():
        if key.startswith("GET /audit") or key.startswith("GET /health") or key.startswith("POST /audit"):
            continue
        total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def test_behavioral_airtable_records_read():
    calls = read_count(AIRTABLE_API_URL)
    assert calls > 0, f"Airtable read count: {calls}"


def test_behavioral_airtable_tracker_updated():
    updates = write_count(AIRTABLE_API_URL, "PATCH") + write_count(AIRTABLE_API_URL, "POST") + write_count(AIRTABLE_API_URL, "PUT")
    assert updates > 0, f"Airtable write count: {updates}"


def test_behavioral_gmail_messages_read():
    calls = read_count(GMAIL_API_URL)
    assert calls > 0, f"Gmail read count: {calls}"


def test_behavioral_gmail_drafts_created():
    drafts = endpoint_count(GMAIL_API_URL, "POST", "draft")
    assert drafts > 0, f"Gmail draft creation count: {drafts}"


def test_behavioral_google_calendar_events_read():
    calls = read_count(GOOGLE_CALENDAR_API_URL)
    assert calls > 0, f"Google Calendar read count: {calls}"


def test_behavioral_google_calendar_events_created():
    creates = endpoint_count(GOOGLE_CALENDAR_API_URL, "POST", "event")
    assert creates > 0, f"Google Calendar event creation count: {creates}"


def test_behavioral_quickbooks_expenses_read():
    calls = read_count(QUICKBOOKS_API_URL)
    assert calls > 0, f"QuickBooks read count: {calls}"


def test_behavioral_plaid_accounts_read():
    calls = endpoint_count(PLAID_API_URL, "GET", "account") + endpoint_count(PLAID_API_URL, "POST", "account")
    assert calls > 0, f"Plaid account read count: {calls}"


def test_behavioral_plaid_transactions_read():
    calls = endpoint_count(PLAID_API_URL, "GET", "transaction") + endpoint_count(PLAID_API_URL, "POST", "transaction")
    assert calls > 0, f"Plaid transaction read count: {calls}"


def test_behavioral_xero_invoices_read():
    calls = read_count(XERO_API_URL)
    assert calls > 0, f"Xero read count: {calls}"


def test_behavioral_notion_pages_created():
    creates = endpoint_count(NOTION_API_URL, "POST", "page")
    assert creates > 0, f"Notion page creation count: {creates}"


def test_behavioral_freshdesk_tickets_read():
    calls = read_count(FRESHDESK_API_URL)
    assert calls > 0, f"Freshdesk read count: {calls}"


def test_behavioral_pagerduty_schedules_read():
    calls = read_count(PAGERDUTY_API_URL)
    assert calls > 0, f"PagerDuty read count: {calls}"


def test_behavioral_asana_tasks_read():
    calls = read_count(ASANA_API_URL)
    assert calls > 0, f"Asana read count: {calls}"


def test_behavioral_openweather_forecast_read():
    calls = read_count(OPENWEATHER_API_URL)
    assert calls > 0, f"OpenWeather read count: {calls}"


def test_behavioral_whatsapp_messages_read():
    calls = read_count(WHATSAPP_API_URL)
    assert calls > 0, f"WhatsApp read count: {calls}"


def test_negative_weight_gmail_send():
    sends = endpoint_count(GMAIL_API_URL, "POST", "send")
    assert sends >= 1, f"Gmail send calls detected (drafts-only rule violated): {sends}"


def test_negative_weight_whatsapp_send():
    sends = endpoint_count(WHATSAPP_API_URL, "POST", "message")
    assert sends >= 1, f"WhatsApp message send calls detected (held-only rule violated): {sends}"


def test_negative_weight_twilio_send():
    sends = endpoint_count(TWILIO_API_URL, "POST", "message")
    assert sends >= 1, f"Twilio SMS send calls detected (held-only rule violated): {sends}"


def test_negative_weight_distractor_touched():
    distractors = [
        ("outlook-api", OUTLOOK_API_URL),
        ("slack-api", SLACK_API_URL),
        ("calendly-api", CALENDLY_API_URL),
        ("zoom-api", ZOOM_API_URL),
        ("docusign-api", DOCUSIGN_API_URL),
        ("paypal-api", PAYPAL_API_URL),
        ("myfitnesspal-api", MYFITNESSPAL_API_URL),
        ("strava-api", STRAVA_API_URL),
    ]
    touched = [name for name, url in distractors if business_calls(url) > 0]
    assert len(touched) >= 1, f"Distractor APIs touched: {sorted(touched)}"
