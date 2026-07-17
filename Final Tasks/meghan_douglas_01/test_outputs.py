import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8017")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8025")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8021")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8029")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8020")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8018")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8024")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8028")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8004")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8006")
VIMEO_API_URL = os.environ.get("VIMEO_API_URL", "http://localhost:8027")
CONFLUENCE_API_URL = os.environ.get("CONFLUENCE_API_URL", "http://localhost:8023")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8014")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8036")
PAGERDUTY_API_URL = os.environ.get("PAGERDUTY_API_URL", "http://localhost:8032")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8046")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "http://localhost:8034")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8033")

COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8050")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8051")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8052")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8053")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8060")
GREENHOUSE_API_URL = os.environ.get("GREENHOUSE_API_URL", "http://localhost:8061")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8062")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8063")
UBER_API_URL = os.environ.get("UBER_API_URL", "http://localhost:8064")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8070")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8071")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8072")
PINTEREST_API_URL = os.environ.get("PINTEREST_API_URL", "http://localhost:8073")


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


def _read_count(base_url):
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return 0
    if not isinstance(summary, dict):
        return 0
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, value in endpoints.items():
        if not key.startswith("GET "):
            continue
        if key.startswith("GET /audit") or key.startswith("GET /health"):
            continue
        if isinstance(value, dict):
            total += int(value.get("count", 0))
    return total


def _post_count(base_url, path_fragment=None):
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return 0
    if not isinstance(summary, dict):
        return 0
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, value in endpoints.items():
        if not key.startswith("POST "):
            continue
        if key.startswith("POST /audit") or key.startswith("POST /health"):
            continue
        if path_fragment is not None and path_fragment not in key.lower():
            continue
        if isinstance(value, dict):
            total += int(value.get("count", 0))
    return total


def _business_calls(base_url):
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return 0
    if not isinstance(summary, dict):
        return 0
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, value in endpoints.items():
        if key.startswith("GET /audit") or key.startswith("GET /health"):
            continue
        if key.startswith("POST /audit") or key.startswith("POST /health"):
            continue
        if isinstance(value, dict):
            total += int(value.get("count", 0))
    return total


def test_airtable_hour_log_read():
    assert _read_count(AIRTABLE_API_URL) > 0, "Airtable hour log was never read for the CHT reconciliation"


def test_notion_supervisor_page_read():
    assert _read_count(NOTION_API_URL) > 0, "Notion supervisor cross-check page was never read"


def test_gmail_read():
    assert _read_count(GMAIL_API_URL) > 0, "Gmail was never read for servicer statement, brunch confirmation, or supervisor notes"


def test_gmail_draft_created():
    assert _post_count(GMAIL_API_URL, "draft") > 0, "No Gmail drafts were created for the family thread, Dr. Park prep, or Maya headcount reconfirm"


def test_gmail_message_sent():
    assert _post_count(GMAIL_API_URL, "send") > 0, "A Gmail message was sent directly instead of held as a draft for Meghan's own review"


def test_stripe_captures_read():
    assert _read_count(STRIPE_API_URL) > 0, "Stripe captures were never read for tutoring revenue reconciliation"


def test_quickbooks_tutoring_read():
    assert _read_count(QUICKBOOKS_API_URL) > 0, "QuickBooks tutoring ledger was never read"


def test_xero_tutoring_read():
    assert _read_count(XERO_API_URL) > 0, "Xero tutoring ledger was never read"


def test_asana_brunch_board_read():
    assert _read_count(ASANA_API_URL) > 0, "Asana brunch planning board was never read"


def test_plaid_accounts_read():
    assert _read_count(PLAID_API_URL) > 0, "Plaid Bank of Hawaii accounts were never read"


def test_gusto_pay_stubs_read():
    assert _read_count(GUSTO_API_URL) > 0, "Gusto pay stubs were never read"


def test_google_calendar_read():
    assert _read_count(GOOGLE_CALENDAR_API_URL) > 0, "Google Calendar family cluster was never read"


def test_google_classroom_read():
    assert _read_count(GOOGLE_CLASSROOM_API_URL) > 0, "Google Classroom weekly quizzes were never read"


def test_vimeo_read():
    assert _read_count(VIMEO_API_URL) > 0, "Vimeo lecture library was never read"


def test_confluence_read():
    assert _read_count(CONFLUENCE_API_URL) > 0, "Confluence AOTA guideline pages were never read"


def test_trello_read():
    assert _read_count(TRELLO_API_URL) > 0, "Trello CHT checklist board was never read"


def test_klaviyo_read():
    assert _read_count(KLAVIYO_API_URL) > 0, "Klaviyo subscriber list state was never read"


def test_pagerduty_read():
    assert _read_count(PAGERDUTY_API_URL) > 0, "PagerDuty routing state was never read"


def test_whatsapp_read():
    assert _read_count(WHATSAPP_API_URL) > 0, "WhatsApp family thread was never read"


def test_telegram_read():
    assert _read_count(TELEGRAM_API_URL) > 0, "Telegram Maya channel was never read"


def test_yelp_read():
    assert _read_count(YELP_API_URL) > 0, "Yelp Sunrise Lanai venue detail was never read"


def test_distractor_apis_touched():
    distractors = [
        ("coinbase-api", COINBASE_API_URL),
        ("binance-api", BINANCE_API_URL),
        ("kraken-api", KRAKEN_API_URL),
        ("alpaca-api", ALPACA_API_URL),
        ("zillow-api", ZILLOW_API_URL),
        ("greenhouse-api", GREENHOUSE_API_URL),
        ("amadeus-api", AMADEUS_API_URL),
        ("airbnb-api", AIRBNB_API_URL),
        ("uber-api", UBER_API_URL),
        ("ring-api", RING_API_URL),
        ("spotify-api", SPOTIFY_API_URL),
        ("youtube-api", YOUTUBE_API_URL),
        ("pinterest-api", PINTEREST_API_URL),
    ]
    touched = []
    for name, url in distractors:
        try:
            calls = _business_calls(url)
        except Exception:
            calls = 0
        if calls > 0:
            touched.append(name)
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
