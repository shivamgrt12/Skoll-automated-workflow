
import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8075")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8076")
GITHUB_API_URL = os.environ.get("GITHUB_API_URL", "http://localhost:8019")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")


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


def _business_endpoint_count(base_url):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, data in endpoints.items():
        if key.startswith("GET /audit") or key.startswith("POST /audit"):
            continue
        if key.endswith("/health") or key.endswith(" /health"):
            continue
        total += data.get("count", 0)
    return total


def test_google_classroom_read():
    summary = api_get(GOOGLE_CLASSROOM_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    coursework_hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v1/courses" in key)
    assert coursework_hits > 0, "Google Classroom coursework endpoints were never queried"


def test_notion_read():
    summary = api_get(NOTION_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v1/" in key and "/audit" not in key and "/health" not in key)
    assert hits > 0, "Notion pages, databases, or search were never queried"


def test_airtable_read():
    summary = api_get(AIRTABLE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v0/" in key)
    assert hits > 0, "Airtable bases, tables, or records were never queried"


def test_asana_read():
    summary = api_get(ASANA_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/api/1.0/" in key)
    assert hits > 0, "Asana projects or tasks were never queried"


def test_salesforce_read():
    summary = api_get(SALESFORCE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/services/data/" in key)
    assert hits > 0, "Salesforce sObjects or SOQL query endpoints were never queried"


def test_gusto_read():
    summary = api_get(GUSTO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v1/companies/" in key or "/v1/payrolls/" in key or "/v1/employees/" in key)
    assert hits > 0, "Gusto companies, payrolls, or employees were never queried"


def test_plaid_read():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/transactions/get" in key or "/accounts/get" in key or "/accounts/balance/get" in key)
    assert hits > 0, "Plaid transactions or account balances were never queried"


def test_quickbooks_read():
    summary = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v3/company/" in key)
    assert hits > 0, "QuickBooks company entities or reports were never queried"


def test_xero_read():
    summary = api_get(XERO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/api.xro/2.0/" in key)
    assert hits > 0, "Xero invoices, contacts, or accounts were never queried"


def test_paypal_read():
    summary = api_get(PAYPAL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v2/invoicing/" in key or "/v1/payments/" in key or "/v2/payments/" in key or "/v2/checkout/orders" in key)
    assert hits > 0, "PayPal invoicing, checkout orders, or payments endpoints were never queried"


def test_docusign_read():
    summary = api_get(DOCUSIGN_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/restapi/v2.1/accounts/" in key)
    assert hits > 0, "DocuSign envelopes or templates endpoints were never queried"


def test_calendly_read():
    summary = api_get(CALENDLY_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/scheduled_events" in key or "/event_types" in key or "/users/me" in key)
    assert hits > 0, "Calendly scheduled events, event types, or user endpoints were never queried"


def test_hubspot_read():
    summary = api_get(HUBSPOT_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/crm/v3/" in key)
    assert hits > 0, "HubSpot CRM contacts, companies, deals, or pipelines were never queried"


def test_whatsapp_read():
    summary = api_get(WHATSAPP_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/v17.0/" in key)
    assert hits > 0, "WhatsApp business, contacts, conversations, or messages were never queried"


def test_salesforce_soql_query_used():
    summary = api_get(SALESFORCE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/services/data/v59.0/query" in key)
    assert hits > 0, "Salesforce SOQL /query endpoint was never used"


def test_docusign_envelope_documents_read():
    summary = api_get(DOCUSIGN_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/documents" in key and "/restapi/v2.1/accounts/" in key)
    assert hits > 0, "DocuSign envelope /documents endpoint was never used"


def test_plaid_balance_get_used():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/accounts/balance/get" in key)
    assert hits > 0, "Plaid /accounts/balance/get was never called"


def test_xero_contacts_read():
    summary = api_get(XERO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = sum(data.get("count", 0) for key, data in endpoints.items() if "/api.xro/2.0/Contacts" in key)
    assert hits > 0, "Xero /api.xro/2.0/Contacts endpoint was never queried"


def test_distractor_apis_touched():
    distractors = [
        ("spotify-api", SPOTIFY_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("youtube-api", YOUTUBE_API_URL),
        ("ticketmaster-api", TICKETMASTER_API_URL),
        ("amadeus-api", AMADEUS_API_URL),
        ("github-api", GITHUB_API_URL),
        ("amazon-seller-api", AMAZON_SELLER_API_URL),
        ("strava-api", STRAVA_API_URL),
    ]
    touched = [name for name, url in distractors if _business_endpoint_count(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
