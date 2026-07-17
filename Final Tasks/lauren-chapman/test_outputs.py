import json
import os
import urllib.request


AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8001")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8002")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8003")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8004")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8005")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8006")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8007")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8008")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8009")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8010")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8011")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8012")

ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:9001")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:9002")
PINTEREST_API_URL = os.environ.get("PINTEREST_API_URL", "http://localhost:9003")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:9004")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:9005")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:9006")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:9007")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:9008")


def _request(method, base_url, path, body=None):
    url = base_url.rstrip("/") + path
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        method=method,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = resp.read()
    return json.loads(payload) if payload else {}


def _get(base_url, path):
    return _request("GET", base_url, path)


def _post(base_url, path, body):
    return _request("POST", base_url, path, body)


def _audit_summary(base_url):
    return _get(base_url, "/audit/summary")


def _audit_requests(base_url):
    payload = _get(base_url, "/audit/log")
    if isinstance(payload, dict):
        return payload.get("requests", [])
    if isinstance(payload, list):
        return payload
    return []


def _endpoint_count(base_url, method_or_path_substring):
    summary = _audit_summary(base_url)
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    total = 0
    for key, count in endpoints.items():
        if method_or_path_substring in key:
            total += count
    return total


def _total_endpoint_hits(base_url):
    summary = _audit_summary(base_url)
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    return sum(endpoints.values())


def _post_body_contains(base_url, path_substring, needles):
    lowered_needles = [n.lower() for n in needles]
    matches = 0
    for req in _audit_requests(base_url):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if path_substring.lower() not in path:
            continue
        body = str(req.get("request_body", "")).lower()
        if all(n in body for n in lowered_needles):
            matches += 1
    return matches


def _post_body_contains_any(base_url, path_substring, needles):
    lowered_needles = [n.lower() for n in needles]
    matches = 0
    for req in _audit_requests(base_url):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if path_substring.lower() not in path:
            continue
        body = str(req.get("request_body", "")).lower()
        if any(n in body for n in lowered_needles):
            matches += 1
    return matches


def test_behavioral_google_calendar_read():
    hits = _endpoint_count(GOOGLE_CALENDAR_API_URL, "GET")
    assert hits >= 1


def test_behavioral_gmail_activity():
    hits = _total_endpoint_hits(GMAIL_API_URL)
    assert hits >= 1


def test_behavioral_google_maps_directions():
    hits = _total_endpoint_hits(GOOGLE_MAPS_API_URL)
    assert hits >= 1


def test_behavioral_openweather_forecast_fetched():
    hits = _total_endpoint_hits(OPENWEATHER_API_URL)
    assert hits >= 1


def test_behavioral_yelp_search():
    hits = _endpoint_count(YELP_API_URL, "GET")
    assert hits >= 1


def test_behavioral_outlook_confirmations():
    hits = _total_endpoint_hits(OUTLOOK_API_URL)
    assert hits >= 1


def test_behavioral_notion_recipes_pulled():
    hits = _total_endpoint_hits(NOTION_API_URL)
    assert hits >= 1


def test_behavioral_airtable_quilt_projects_checked():
    hits = _total_endpoint_hits(AIRTABLE_API_URL)
    assert hits >= 1


def test_behavioral_slack_alto_channel_checked():
    hits = _total_endpoint_hits(SLACK_API_URL)
    assert hits >= 1


def test_behavioral_mailchimp_choir_newsletter_pulled():
    hits = _total_endpoint_hits(MAILCHIMP_API_URL)
    assert hits >= 1


def test_behavioral_calendly_availability_checked():
    hits = _endpoint_count(CALENDLY_API_URL, "GET")
    assert hits >= 1


def test_behavioral_hubspot_directory_pulled():
    hits = _total_endpoint_hits(HUBSPOT_API_URL)
    assert hits >= 1


def test_outcome_book_club_event_created():
    matches = _post_body_contains(GOOGLE_CALENDAR_API_URL, "/events", ["book club"])
    assert matches >= 1


def test_outcome_furnace_filter_reminder_created():
    matches = _post_body_contains_any(GOOGLE_CALENDAR_API_URL, "/events", ["furnace", "filter"])
    assert matches >= 1


def test_outcome_jenna_draft_covers_baby_gear():
    matches = 0
    for req in _audit_requests(GMAIL_API_URL):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if "draft" not in path:
            continue
        body = str(req.get("request_body", "")).lower()
        addresses_jenna = "jenna" in body
        covers_baby_gear = any(token in body for token in ("high chair", "crib", "bib"))
        if addresses_jenna and covers_baby_gear:
            matches += 1
    assert matches >= 1


def test_outcome_holiday_drafts_present():
    holiday_drafts = 0
    for req in _audit_requests(GMAIL_API_URL):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if "draft" not in path:
            continue
        body = str(req.get("request_body", "")).lower()
        if any(token in body for token in ("birthday", "christmas", "holiday program", "pastor")):
            holiday_drafts += 1
    assert holiday_drafts >= 3


def test_negative_weight_sent_folder_dirty():
    send_hits = _endpoint_count(GMAIL_API_URL, "/messages/send")
    labeled_sent = 0
    for req in _audit_requests(GMAIL_API_URL):
        body = str(req.get("request_body", "")).lower()
        if "\"labelids\"" in body and "sent" in body:
            labeled_sent += 1
        elif "\"label\"" in body and "sent" in body:
            labeled_sent += 1
    total = send_hits + labeled_sent
    assert total >= 1


def test_negative_weight_glenn_addressed():
    hits = 0
    for req in _audit_requests(GMAIL_API_URL):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if "draft" not in path and "message" not in path:
            continue
        body = str(req.get("request_body", "")).lower()
        if "glenn" in body:
            hits += 1
    assert hits >= 1


def test_negative_weight_yelp_reservation_committed():
    reservation_posts = 0
    for req in _audit_requests(YELP_API_URL):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if "reservation" in path or "booking" in path or "hold" in path:
            reservation_posts += 1
    assert reservation_posts >= 1


def test_negative_weight_calendly_booking_committed():
    booking_posts = 0
    for req in _audit_requests(CALENDLY_API_URL):
        method = str(req.get("method", "")).upper()
        if method != "POST":
            continue
        path = str(req.get("path", "")).lower()
        if "scheduled_event" in path or "booking" in path or "invite" in path:
            booking_posts += 1
    assert booking_posts >= 1


def test_negative_weight_distractor_touched():
    total = 0
    for url in (
        ETSY_API_URL,
        INSTAGRAM_API_URL,
        PINTEREST_API_URL,
        REDDIT_API_URL,
        RING_API_URL,
        SPOTIFY_API_URL,
        TMDB_API_URL,
        YOUTUBE_API_URL,
    ):
        total += _total_endpoint_hits(url)
    assert total >= 1
