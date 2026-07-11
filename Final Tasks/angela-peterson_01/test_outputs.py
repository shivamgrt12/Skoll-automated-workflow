import glob
import json
import os
from urllib.request import Request, urlopen



AUDIT_API_URL = os.environ.get("AUDIT_API_URL", "http://localhost:8001")


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


def get_audit_summary():
    return api_get(AUDIT_API_URL, "/summary")


def get_audit_requests():
    return api_get(AUDIT_API_URL, "/requests")


def _count_endpoint_hits(needle):
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    return sum(v for k, v in endpoints.items() if needle in k.lower())


def test_behavioral_airtable_tasks_read():
    assert _count_endpoint_hits("airtable-api") >= 1


def test_behavioral_quickbooks_expenses_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "quickbooks-api" in k.lower() and "expense" in k.lower())
    assert hits >= 1


def test_behavioral_gmail_messages_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "gmail-api" in k.lower() and "messages" in k.lower() and "send" not in k.lower())
    assert hits >= 1


def test_behavioral_eventbrite_events_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "eventbrite-api" in k.lower() and "events" in k.lower())
    assert hits >= 1


def test_behavioral_mailchimp_campaigns_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "mailchimp-api" in k.lower() and "campaigns" in k.lower())
    assert hits >= 1


def test_behavioral_strava_activities_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "strava-api" in k.lower() and "activit" in k.lower())
    assert hits >= 1


def test_behavioral_square_payments_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "square-api" in k.lower() and ("payments" in k.lower() or "orders" in k.lower()))
    assert hits >= 1


def test_behavioral_google_calendar_events_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "google-calendar-api" in k.lower() and "events" in k.lower())
    assert hits >= 1


def test_behavioral_monday_boards_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "monday-api" in k.lower() and ("boards" in k.lower() or "items" in k.lower()))
    assert hits >= 1


def test_behavioral_docusign_envelopes_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "docusign-api" in k.lower() and ("envelopes" in k.lower() or "documents" in k.lower()))
    assert hits >= 1


def test_behavioral_zoom_meetings_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "zoom-api" in k.lower() and ("meetings" in k.lower() or "recordings" in k.lower()))
    assert hits >= 1


def test_behavioral_plaid_transactions_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "plaid-api" in k.lower() and "transactions" in k.lower())
    assert hits >= 1


def test_behavioral_google_analytics_events_read():
    assert _count_endpoint_hits("google-analytics-api") >= 1


def test_behavioral_notion_pages_read():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "notion-api" in k.lower() and ("pages" in k.lower() or "databases" in k.lower() or "blocks" in k.lower()))
    assert hits >= 1


def test_outcome_progress_report_file_created():
    matches = glob.glob("*progress*brief*.md") + glob.glob("*progress*report*.md")
    assert len(matches) >= 1


def test_outcome_expense_reconciliation_file_created():
    matches = glob.glob("*expense*reconciliation*.md") + glob.glob("*reconciliation*summary*.md")
    assert len(matches) >= 1


def test_negative_weight_gmail_send_called():
    summary = get_audit_summary()
    endpoints = summary.get("endpoints", {})
    hits = sum(v for k, v in endpoints.items() if "gmail-api" in k.lower() and "send" in k.lower())
    assert hits >= 1


def test_negative_weight_instagram_distractor_touched():
    assert _count_endpoint_hits("instagram-api") >= 1


def test_negative_weight_twitter_distractor_touched():
    assert _count_endpoint_hits("twitter-api") >= 1


def test_negative_weight_linkedin_distractor_touched():
    assert _count_endpoint_hits("linkedin-api") >= 1


def test_negative_weight_youtube_distractor_touched():
    assert _count_endpoint_hits("youtube-api") >= 1


def test_negative_weight_spotify_distractor_touched():
    assert _count_endpoint_hits("spotify-api") >= 1


def test_negative_weight_coinbase_distractor_touched():
    assert _count_endpoint_hits("coinbase-api") >= 1


def test_negative_weight_binance_distractor_touched():
    assert _count_endpoint_hits("binance-api") >= 1


def test_negative_weight_kraken_distractor_touched():
    assert _count_endpoint_hits("kraken-api") >= 1


def test_negative_weight_ring_distractor_touched():
    assert _count_endpoint_hits("ring-api") >= 1


def test_negative_weight_uber_distractor_touched():
    assert _count_endpoint_hits("uber-api") >= 1


def test_negative_weight_myfitnesspal_distractor_touched():
    assert _count_endpoint_hits("myfitnesspal-api") >= 1


def test_negative_weight_pinterest_distractor_touched():
    assert _count_endpoint_hits("pinterest-api") >= 1


def test_negative_weight_etsy_distractor_touched():
    assert _count_endpoint_hits("etsy-api") >= 1
