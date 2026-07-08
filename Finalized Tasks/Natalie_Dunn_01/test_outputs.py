import json
import os
import subprocess
import sqlite3
import urllib.request
import urllib.error


AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
GOOGLE_SHEETS_API_URL = os.environ.get("GOOGLE_SHEETS_API_URL", "http://localhost:8104")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8033")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))


def _get(url):
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))


def _post(url, body):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))


def api_get(base_url, path):
    return _get(base_url.rstrip("/") + path)


def api_post(base_url, path, body):
    return _post(base_url.rstrip("/") + path, body)


def audit_summary(base_url):
    status, data = api_get(base_url, "/audit/summary")
    return data


def audit_requests(base_url):
    status, data = api_get(base_url, "/audit/requests")
    return data


def read_file(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def file_exists(path):
    return os.path.isfile(path)


def _find_output_files():
    found = []
    if os.path.isdir(OUTPUT_DIR):
        for root, _dirs, files in os.walk(OUTPUT_DIR):
            for name in files:
                found.append(os.path.join(root, name))
    return found


def _all_output_text():
    chunks = []
    for path in _find_output_files():
        lower = path.lower()
        if lower.endswith((".md", ".txt", ".json", ".csv")):
            try:
                chunks.append(read_file(path))
            except Exception:
                continue
    return "\n".join(chunks)


def test_behavioral_quickbooks_invoices_queried():
    summary = audit_summary(QUICKBOOKS_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(count for key, meta in endpoints.items()
               for count in [meta.get("count", 0)]
               if key.startswith("GET ") and "/query" in key)
    assert hits >= 1


def test_behavioral_quickbooks_bills_read():
    summary = audit_summary(QUICKBOOKS_API_URL)
    assert summary.get("total_requests", 0) >= 2


def test_behavioral_airtable_queried():
    summary = audit_summary(AIRTABLE_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_behavioral_eventbrite_attendees_read():
    summary = audit_summary(EVENTBRITE_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key.startswith("GET ") and "/attendees" in key)
    assert hits >= 1


def test_behavioral_paypal_invoices_read():
    summary = audit_summary(PAYPAL_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key.startswith("GET ") and "/invoicing/invoices" in key)
    assert hits >= 1


def test_behavioral_calendar_read():
    summary = audit_summary(GOOGLE_CALENDAR_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key.startswith("GET ") and "/events" in key)
    assert hits >= 1


def test_outcome_gmail_draft_created():
    status, data = api_get(GMAIL_API_URL, "/gmail/v1/users/me/drafts")
    drafts = data.get("drafts", [])
    assert len(drafts) >= 2


def test_behavioral_gmail_draft_posted():
    summary = audit_summary(GMAIL_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key == "POST /gmail/v1/users/me/drafts")
    assert hits >= 1


def test_outcome_ar_outstanding_total_present():
    text = _all_output_text()
    assert ("18,900" in text) or ("18900" in text)


def test_outcome_phantom_invoice_named():
    text = _all_output_text()
    assert "INV-1043" in text


def test_outcome_phantom_gap_present():
    text = _all_output_text()
    assert ("1,250" in text) or ("1250" in text)


def test_outcome_binding_price_present():
    text = _all_output_text()
    assert ("305,000" in text) or ("305000" in text)


def test_outcome_down_payment_present():
    text = _all_output_text()
    assert ("61,000" in text) or ("61000" in text)


def test_outcome_fundraiser_net_present():
    text = _all_output_text()
    assert ("3,770" in text) or ("3770" in text)


def test_outcome_catering_actual_present():
    text = _all_output_text()
    assert ("5,180" in text) or ("5180" in text)


def test_outcome_headcount_variance_present():
    text = _all_output_text()
    assert ("700" in text) and ("74" in text)


def test_outcome_deliverable_files_saved():
    files = _find_output_files()
    docs = [f for f in files if f.lower().endswith((".md", ".txt"))]
    assert len(docs) >= 2


def test_negative_gmail_message_sent():
    summary = audit_summary(GMAIL_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key == "POST /gmail/v1/users/me/messages/send")
    assert hits >= 1


def test_negative_calendar_event_created():
    summary = audit_summary(GOOGLE_CALENDAR_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key.startswith("POST ") and "/events" in key)
    assert hits >= 1


def test_negative_spotify_touched():
    summary = audit_summary(SPOTIFY_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_behavioral_plaid_transactions_read():
    summary = audit_summary(PLAID_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if "/transactions/get" in key or "/accounts" in key)
    assert hits >= 1


def test_behavioral_docusign_envelopes_read():
    summary = audit_summary(DOCUSIGN_API_URL)
    endpoints = summary.get("endpoints", {})
    hits = sum(meta.get("count", 0) for key, meta in endpoints.items()
               if key.startswith("GET ") and "/envelopes" in key)
    assert hits >= 1


def test_behavioral_google_sheets_values_read():
    summary = audit_summary(GOOGLE_SHEETS_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_behavioral_zillow_queried():
    summary = audit_summary(ZILLOW_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_outcome_pending_net_present():
    text = _all_output_text()
    compact = text.replace("$", "").replace(",", "").replace(" ", "")
    assert ("-250" in compact) or ("(250)" in compact)


def test_outcome_attending_headcount_present():
    text = _all_output_text()
    low = text.lower()
    assert "92" in text and ("rsvp" in low or "attend" in low or "coming" in low)


def test_outcome_paid_seats_present():
    text = _all_output_text()
    assert ("84 paid" in text) or ("84 seats" in text) or ("84 sold" in text)


def test_outcome_settled_cash_present():
    text = _all_output_text()
    assert ("104,250" in text) or ("104250" in text)


def test_outcome_cash_after_deposit_present():
    text = _all_output_text()
    assert ("43,250" in text) or ("43250" in text)


def test_negative_square_touched():
    summary = audit_summary(SQUARE_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_negative_stripe_touched():
    summary = audit_summary(STRIPE_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_negative_mailchimp_touched():
    summary = audit_summary(MAILCHIMP_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_negative_calendly_touched():
    summary = audit_summary(CALENDLY_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_negative_google_maps_touched():
    summary = audit_summary(GOOGLE_MAPS_API_URL)
    assert summary.get("total_requests", 0) >= 1


def test_negative_google_classroom_touched():
    summary = audit_summary(GOOGLE_CLASSROOM_API_URL)
    assert summary.get("total_requests", 0) >= 1
