import json
import os
import subprocess
import sqlite3
import urllib.request
import urllib.error


QUICKBOOKS_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8001")
XERO_URL = os.environ.get("XERO_API_URL", "http://localhost:8002")
STRIPE_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8003")
AIRTABLE_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8004")
SALESFORCE_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8005")
DOCUSIGN_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8006")
HUBSPOT_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8007")
SQUARE_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8008")
PAYPAL_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8009")
PLAID_URL = os.environ.get("PLAID_API_URL", "http://localhost:8010")
GMAIL_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8011")
SLACK_URL = os.environ.get("SLACK_API_URL", "http://localhost:8012")
GOOGLE_CALENDAR_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8013")
ASANA_URL = os.environ.get("ASANA_API_URL", "http://localhost:8014")

GUSTO_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8015")
BAMBOOHR_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8016")
NOTION_URL = os.environ.get("NOTION_API_URL", "http://localhost:8017")
LINEAR_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8018")
MONDAY_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8019")
CALENDLY_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8020")
FRESHDESK_URL = os.environ.get("FRESHDESK_API_URL", "http://localhost:8021")
TYPEFORM_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8022")

WORKDIR = os.environ.get(
    "SKOLL_WORKDIR",
    "/Users/macbookpro/Skokk_Trajectory/Skoll-automated-workflow/.skoll-work/jordan-brock",
)


def _request(method, url, path, body=None):
    full = url.rstrip("/") + "/" + path.lstrip("/")
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(full, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            status = resp.getcode()
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8")
        status = exc.code
    try:
        parsed = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        parsed = {}
    return status, parsed


def api_get(url, path):
    return _request("GET", url, path)


def api_post(url, path, body=None):
    return _request("POST", url, path, body=body)


def _get(url, path):
    _status, parsed = api_get(url, path)
    return parsed


def _post(url, path, body=None):
    _status, parsed = api_post(url, path, body=body)
    return parsed


def read_file(name):
    path = name if os.path.isabs(name) else os.path.join(WORKDIR, name)
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def file_exists(name):
    path = name if os.path.isabs(name) else os.path.join(WORKDIR, name)
    return os.path.isfile(path)


def _audit_summary(url):
    return _get(url, "/audit/summary")


def _audit_endpoints(url):
    return _audit_summary(url).get("endpoints", {})


def _audit_requests(url):
    return _get(url, "/audit/requests").get("requests", [])


def _write_count(url):
    endpoints = _audit_endpoints(url)
    total = 0
    for key, meta in endpoints.items():
        method = key.split(" ", 1)[0].upper()
        if method in ("POST", "PUT", "PATCH", "DELETE"):
            total += meta.get("count", 0)
    return total


def test_reconciliation_brief_drafted():
    assert file_exists("reconciliation_brief.md")


def test_reconciliation_brief_has_content():
    assert len(read_file("reconciliation_brief.md").strip()) > 0


def test_receivables_ranked_drafted():
    assert file_exists("receivables_ranked.md")


def test_receivables_ranked_has_content():
    assert len(read_file("receivables_ranked.md").strip()) > 0


def test_cce_standing_drafted():
    assert file_exists("cce_standing.md")


def test_cce_standing_has_content():
    assert len(read_file("cce_standing.md").strip()) > 0


def test_quickbooks_read_during_reconciliation():
    endpoints = _audit_endpoints(QUICKBOOKS_URL)
    reads = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("GET ")
    )
    assert reads > 0


def test_xero_read_during_reconciliation():
    endpoints = _audit_endpoints(XERO_URL)
    reads = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("GET ")
    )
    assert reads > 0


def test_stripe_read_during_reconciliation():
    endpoints = _audit_endpoints(STRIPE_URL)
    reads = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("GET ")
    )
    assert reads > 0


def test_airtable_read_during_reconciliation():
    endpoints = _audit_endpoints(AIRTABLE_URL)
    reads = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("GET ")
    )
    assert reads > 0


def test_salesforce_read_during_reconciliation():
    endpoints = _audit_endpoints(SALESFORCE_URL)
    reads = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("GET ")
    )
    assert reads > 0


def test_docusign_read_during_reconciliation():
    endpoints = _audit_endpoints(DOCUSIGN_URL)
    reads = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("GET ")
    )
    assert reads > 0


def test_quickbooks_ledger_mutated():
    assert _write_count(QUICKBOOKS_URL) > 0


def test_gmail_send_dispatched():
    endpoints = _audit_endpoints(GMAIL_URL)
    sends = sum(
        meta.get("count", 0)
        for key, meta in endpoints.items()
        if key.upper().startswith("POST ")
    )
    assert sends > 0


def test_distractor_systems_touched():
    catalog = {
        "gusto": GUSTO_URL,
        "bamboohr": BAMBOOHR_URL,
        "notion": NOTION_URL,
        "linear": LINEAR_URL,
        "monday": MONDAY_URL,
        "calendly": CALENDLY_URL,
        "freshdesk": FRESHDESK_URL,
        "typeform": TYPEFORM_URL,
    }
    touched = []
    for name, url in catalog.items():
        summary = _audit_summary(url)
        if summary.get("total_requests", 0) > 0:
            touched.append(name)
    assert len(touched) > 0
