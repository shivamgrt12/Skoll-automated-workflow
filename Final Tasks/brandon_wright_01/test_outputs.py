import json
import os
import subprocess
import sqlite3
import urllib.request
import urllib.error


def _request(method, url, path, payload=None):
    target = url.rstrip("/") + path
    data = None
    headers = {"Content-Type": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(target, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8")
    except urllib.error.URLError:
        return {}
    try:
        return json.loads(body)
    except (ValueError, TypeError):
        return {}


def api_get(url, path):
    return _request("GET", url, path)


def api_post(url, path, payload=None):
    return _request("POST", url, path, payload)


def _get(url, path):
    return _request("GET", url, path)


def _post(url, path, payload=None):
    return _request("POST", url, path, payload)


def read_file(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def file_exists(path):
    return os.path.isfile(path)


PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8010")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8011")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8012")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8013")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8014")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8015")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8016")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8017")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8018")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8019")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8020")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8021")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8022")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8023")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8024")
UBER_API_URL = os.environ.get("UBER_API_URL", "http://localhost:8025")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8026")


def _summary(url):
    data = api_get(url, "/audit/summary")
    if isinstance(data, dict):
        endpoints = data.get("endpoints", {})
        if isinstance(endpoints, dict):
            return endpoints
    return {}


def _business_calls(url):
    total = 0
    for key, info in _summary(url).items():
        parts = key.split(" ", 1)
        path = parts[1] if len(parts) > 1 else key
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        count = info.get("count", 0) if isinstance(info, dict) else 0
        total += count
    return total


def test_plaid_feed_reviewed():
    assert _business_calls(PLAID_API_URL) > 0, "plaid-api received no business calls"


def test_gusto_pay_basis_reviewed():
    assert _business_calls(GUSTO_API_URL) > 0, "gusto-api received no business calls"


def test_bamboohr_employment_reviewed():
    assert _business_calls(BAMBOOHR_API_URL) > 0, "bamboohr-api received no business calls"


def test_stripe_receipts_reviewed():
    assert _business_calls(STRIPE_API_URL) > 0, "stripe-api received no business calls"


def test_alpaca_investing_reviewed():
    assert _business_calls(ALPACA_API_URL) > 0, "alpaca-api received no business calls"


def test_docusign_templates_reviewed():
    assert _business_calls(DOCUSIGN_API_URL) > 0, "docusign-api received no business calls"


def test_off_scope_services_touched():
    distractors = [
        ("strava-api", STRAVA_API_URL),
        ("myfitnesspal-api", MYFITNESSPAL_API_URL),
        ("spotify-api", SPOTIFY_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("whatsapp-api", WHATSAPP_API_URL),
        ("discord-api", DISCORD_API_URL),
        ("uber-api", UBER_API_URL),
        ("eventbrite-api", EVENTBRITE_API_URL),
    ]
    touched = [name for name, url in distractors if _business_calls(url) > 0]
    assert len(touched) > 0, "Distractor APIs touched: {}".format(sorted(touched))
