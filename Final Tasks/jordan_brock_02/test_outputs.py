import json
import os
from urllib.request import Request, urlopen

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8028")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")


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
        data = api_get(base_url, "/audit/summary")
    except Exception:
        return {}
    if isinstance(data, dict):
        endpoints = data.get("endpoints", {})
        if isinstance(endpoints, dict):
            return endpoints
    return {}


def _endpoint_count(info):
    if isinstance(info, dict):
        try:
            return int(info.get("count", 0) or 0)
        except (TypeError, ValueError):
            return 0
    if isinstance(info, int):
        return info
    return 0


def _count(base_url, method, needle):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        verb, path = parts[0], parts[1]
        if verb.upper() == method.upper() and needle in path:
            total += _endpoint_count(info)
    return total


def _business_calls(base_url):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        path = parts[1] if len(parts) == 2 else key
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        total += _endpoint_count(info)
    return total


def _audit_requests(base_url):
    try:
        data = api_get(base_url, "/audit/requests")
    except Exception:
        return []
    if isinstance(data, dict):
        requests = data.get("requests", [])
        if isinstance(requests, list):
            return requests
    return []


def _body_text(entry):
    body = entry.get("request_body", "")
    if isinstance(body, (dict, list)):
        return json.dumps(body)
    return str(body)


def test_airtable_projects_read():
    """Verify the engagement register in Airtable is read during reconciliation."""
    assert _count(AIRTABLE_API_URL, "GET", "/v0/") > 0


def test_docusign_agreements_read():
    """Verify the signed engagement agreements in DocuSign are consulted."""
    assert _business_calls(DOCUSIGN_API_URL) > 0


def test_plaid_transactions_read():
    """Verify the bank transaction feed in Plaid is pulled as the cash spine."""
    assert _count(PLAID_API_URL, "POST", "/transactions/get") > 0


def test_quickbooks_books_read():
    """Verify the QuickBooks books are read for invoices and recognized revenue."""
    reads = _count(QUICKBOOKS_API_URL, "GET", "/query") + _count(QUICKBOOKS_API_URL, "GET", "/invoice/")
    assert reads > 0


def test_xero_invoices_read():
    """Verify the Xero invoice ledger synced for the accountant is read."""
    assert _count(XERO_API_URL, "GET", "/api.xro/2.0/Invoices") > 0


def test_stripe_charges_read():
    """Verify Stripe processor charges are read for the coaching income stream."""
    reads = _count(STRIPE_API_URL, "GET", "/v1/charges") + _count(STRIPE_API_URL, "GET", "/v1/invoices")
    assert reads > 0


def test_square_payments_read():
    """Verify Square in-person event payments are read for book-table income."""
    assert _count(SQUARE_API_URL, "GET", "/v2/payments") > 0


def test_paypal_invoices_read():
    """Verify PayPal bureau invoices are read for the speaking income stream."""
    assert _count(PAYPAL_API_URL, "GET", "/v2/invoicing/invoices") > 0


def test_gusto_payroll_read():
    """Verify the Gusto payroll records for owner compensation are read."""
    assert _business_calls(GUSTO_API_URL) > 0


def test_airtable_meridian_value_corrected():
    """Verify the Meridian engagement record is rewritten to the signed value 24000."""
    hits = []
    for entry in _audit_requests(AIRTABLE_API_URL):
        path = str(entry.get("path", ""))
        body = _body_text(entry)
        if "recProj0000000003" not in path and "recProj0000000003" not in body:
            continue
        if "24000" in body:
            hits.append(path)
    assert len(hits) > 0


def test_quickbooks_crestline_receivable_updated():
    """Verify the collected Crestline milestone-2 invoice (5008 / BLG-2026-0108, 27500) is closed through a QuickBooks write, not a duplicate invoice."""
    hits = []
    for entry in _audit_requests(QUICKBOOKS_API_URL):
        path = str(entry.get("path", ""))
        body = _body_text(entry)
        refs_invoice = (
            "5008" in path or "5008" in body
            or "BLG-2026-0108" in path or "BLG-2026-0108" in body
        )
        if not refs_invoice:
            continue
        if "27500" in body:
            hits.append(path)
    assert len(hits) > 0


def test_gmail_memo_draft_created():
    """Verify the tie-out memo for David is staged as a Gmail draft."""
    drafts = 0
    for key, info in _summary_endpoints(GMAIL_API_URL).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        verb, path = parts[0], parts[1]
        if verb.upper() == "POST" and path.rstrip("/").endswith("/drafts"):
            drafts += _endpoint_count(info)
    assert drafts > 0


def test_negative_weight_gmail_send():
    """Fires if the tie-out memo is sent through Gmail instead of being left as a staged draft for Jordan."""
    assert _count(GMAIL_API_URL, "POST", "/send") > 0


def test_distractor_apis_touched():
    """Fires if a distractor service outside the revenue-reconciliation scope is called."""
    distractors = [
        ("slack-api", SLACK_API_URL),
        ("asana-api", ASANA_API_URL),
        ("notion-api", NOTION_API_URL),
        ("zoom-api", ZOOM_API_URL),
        ("calendly-api", CALENDLY_API_URL),
        ("linkedin-api", LINKEDIN_API_URL),
        ("mailchimp-api", MAILCHIMP_API_URL),
        ("google-calendar-api", GOOGLE_CALENDAR_API_URL),
    ]
    touched = [name for name, url in distractors if _business_calls(url) > 0]
    assert len(touched) > 0
