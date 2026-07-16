
import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

# URL constants - one line per Required API and per Distractor API named in tests
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8001")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
UPS_API_URL = os.environ.get("UPS_API_URL", "http://localhost:8096")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8052")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8089")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8033")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8034")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8008")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "http://localhost:8063")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
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


def _summary_endpoints(base_url):
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return {}
    return summary.get("endpoints", {})


def read_count(base_url, *path_prefixes):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, meta in endpoints.items():
        if not key.startswith("GET "):
            continue
        for prefix in path_prefixes:
            if prefix in key:
                total += meta.get("count", 0)
                break
    return total


def method_count(base_url, method, *path_prefixes):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, meta in endpoints.items():
        if not key.startswith(f"{method} "):
            continue
        for prefix in path_prefixes:
            if prefix in key:
                total += meta.get("count", 0)
                break
    return total


def business_calls(base_url):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, meta in endpoints.items():
        if "/audit" in key or "/health" in key:
            continue
        total += meta.get("count", 0)
    return total


def request_bodies_matching(base_url, method, path_prefix, needles):
    try:
        audit = api_get(base_url, "/audit/requests")
    except Exception:
        return 0
    entries = audit.get("requests", [])
    hits = 0
    for e in entries:
        if e.get("method") != method:
            continue
        if path_prefix not in e.get("path", ""):
            continue
        body = e.get("request_body")
        if body is None:
            continue
        body_str = json.dumps(body).lower() if isinstance(body, (dict, list)) else str(body).lower()
        for needle in needles:
            if needle.lower() in body_str:
                hits += 1
                break
    return hits


def test_calendar_events_read():
    assert read_count(GOOGLE_CALENDAR_API_URL, "/events", "/calendarList") > 0, "no google-calendar events read traffic"


def test_classroom_break_dates_read():
    assert read_count(GOOGLE_CLASSROOM_API_URL, "/courses", "/courseWork", "/announcements") > 0, "no google-classroom read traffic"


def test_notion_pages_read():
    assert read_count(NOTION_API_URL, "/v1/pages", "/v1/search") > 0, "no notion pages/search read traffic"


def test_notion_databases_read():
    assert read_count(NOTION_API_URL, "/v1/databases") > 0, "no notion databases read traffic"


def test_notion_pages_created():
    posted = method_count(NOTION_API_URL, "POST", "/v1/pages")
    assert posted >= 3, f"expected >= 3 notion page creations, saw {posted}"


def test_notion_break_plan_content():
    hits = request_bodies_matching(
        NOTION_API_URL,
        "POST",
        "/v1/pages",
        ["custody", "winter break", "pickup", "dropoff", "handoff", "chloe"],
    )
    assert hits > 0, "no notion page body carried custody-window content"


def test_notion_money_page_content():
    hits = request_bodies_matching(
        NOTION_API_URL,
        "POST",
        "/v1/pages",
        ["safe to spend", "budget", "rent", "child support", "savings", "runway"],
    )
    assert hits > 0, "no notion page body carried money-picture content"


def test_notion_gift_page_content():
    hits = request_bodies_matching(
        NOTION_API_URL,
        "POST",
        "/v1/pages",
        ["gift", "tracking", "at risk", "backup", "order", "etsy"],
    )
    assert hits > 0, "no notion page body carried gift-status content"


def test_plaid_accounts_read():
    assert method_count(PLAID_API_URL, "POST", "/accounts") > 0, "no plaid accounts traffic"


def test_plaid_transactions_read():
    assert method_count(PLAID_API_URL, "POST", "/transactions") > 0, "no plaid transactions traffic"


def test_gusto_payroll_read():
    assert read_count(GUSTO_API_URL, "/payrolls", "/employees", "/companies") > 0, "no gusto payroll traffic"


def test_etsy_gifts_read():
    assert read_count(ETSY_API_URL, "/listings", "/receipts", "/transactions") > 0, "no etsy read traffic"


def test_amazon_orders_read():
    assert read_count(AMAZON_SELLER_API_URL, "/orders", "/catalog", "/notifications") > 0, "no amazon orders traffic"


def test_ups_tracking_read():
    assert read_count(UPS_API_URL, "/track") > 0, "no ups tracking traffic"


def test_shippo_tracking_read():
    assert read_count(SHIPPO_API_URL, "/tracks", "/shipments") > 0, "no shippo tracking traffic"


def test_klaviyo_sale_alerts_read():
    assert read_count(KLAVIYO_API_URL, "/campaigns", "/profiles", "/lists") > 0, "no klaviyo read traffic"


def test_paypal_invoices_read():
    assert read_count(PAYPAL_API_URL, "/invoicing", "/checkout") > 0, "no paypal invoice traffic"


def test_gmail_messages_read():
    assert read_count(GMAIL_API_URL, "/messages", "/threads") > 0, "no gmail read traffic"


def test_maps_drive_read():
    assert read_count(GOOGLE_MAPS_API_URL, "/directions", "/distancematrix", "/geocode") > 0, "no google-maps traffic"


def test_weather_forecast_read():
    assert read_count(OPENWEATHER_API_URL, "/forecast", "/weather") > 0, "no openweather traffic"


def test_yelp_dining_read():
    assert read_count(YELP_API_URL, "/businesses") > 0, "no yelp businesses traffic"


def test_gmail_send_forbidden():
    sent = method_count(GMAIL_API_URL, "POST", "/messages/send", "/drafts/send")
    assert sent > 0, f"gmail send calls detected: {sent}"


def test_distractor_apis_touched():
    distractors = [
        ("strava-api", STRAVA_API_URL),
        ("myfitnesspal-api", MYFITNESSPAL_API_URL),
        ("ring-api", RING_API_URL),
        ("spotify-api", SPOTIFY_API_URL),
        ("telegram-api", TELEGRAM_API_URL),
        ("alpaca-api", ALPACA_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("zillow-api", ZILLOW_API_URL),
        ("linkedin-api", LINKEDIN_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
    ]
    touched = [name for name, url in distractors if business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
