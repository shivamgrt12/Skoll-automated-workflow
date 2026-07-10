import json
import os
import urllib.request
import urllib.error

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8000")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8001")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8002")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8003")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8004")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8005")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8006")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8007")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8008")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8009")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8010")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8011")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8013")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8014")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8015")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8016")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8017")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8018")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8019")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8020")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8021")


def _request(url, method="GET", data=None, headers=None):
    hdrs = {"Content-Type": "application/json"}
    if headers:
        hdrs.update(headers)
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=hdrs, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def api_get(base_url, path):
    return _request(f"{base_url}{path}")


def api_post(base_url, path, data=None):
    return _request(f"{base_url}{path}", method="POST", data=data)


def test_behavioral_quickbooks_accounts_read():
    summary = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "quickbooks-api received zero requests"


def test_behavioral_plaid_transactions_read():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "plaid-api received zero requests"


def test_behavioral_bamboohr_employees_read():
    summary = api_get(BAMBOOHR_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "bamboohr-api received zero requests"


def test_behavioral_xero_invoices_read():
    summary = api_get(XERO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "xero-api received zero requests"


def test_behavioral_amadeus_flights_read():
    summary = api_get(AMADEUS_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "amadeus-api received zero requests"


def test_behavioral_airbnb_listings_read():
    summary = api_get(AIRBNB_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "airbnb-api received zero requests"


def test_behavioral_gmail_messages_read():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "gmail-api received zero requests"


def test_behavioral_instacart_orders_read():
    summary = api_get(INSTACART_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "instacart-api received zero requests"


def test_outcome_plaid_accounts_and_transactions_both_queried():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    accounts_hit = any("account" in p.lower() for p in endpoints)
    transactions_hit = any("transaction" in p.lower() for p in endpoints)
    assert accounts_hit and transactions_hit, "plaid-api must be queried for both accounts and transactions"


def test_outcome_gusto_payrolls_and_compensations_both_queried():
    summary = api_get(GUSTO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    payrolls_hit = any("payroll" in p.lower() for p in endpoints)
    compensations_hit = any("compensation" in p.lower() for p in endpoints)
    assert payrolls_hit and compensations_hit, "gusto-api must be queried for both payrolls and compensations to anchor the pay-stub count and compensation history (C2 403(b) rate discrepancy itself is anchored in Gmail messages)"


def test_outcome_stripe_charges_endpoint_queried():
    summary = api_get(STRIPE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    charge_hit = sum(
        info.get("count", 0)
        for path, info in endpoints.items()
        if "charge" in path.lower() or "payment" in path.lower()
    )
    assert charge_hit > 0, "stripe-api charges endpoint was never queried"


def test_outcome_airtable_records_queried():
    summary = api_get(AIRTABLE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    records_hit = sum(
        info.get("count", 0)
        for path, info in endpoints.items()
        if "record" in path.lower() or "base" in path.lower() or "table" in path.lower()
    )
    assert records_hit > 0, "airtable-api records or metadata endpoints were never queried"


def test_outcome_calendar_events_endpoint_queried():
    summary = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    evt_hit = sum(
        info.get("count", 0)
        for path, info in endpoints.items()
        if "event" in path.lower()
    )
    assert evt_hit > 0, "google-calendar-api events endpoint was never queried"


def test_outcome_xero_invoices_endpoint_queried():
    summary = api_get(XERO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    inv_hit = sum(
        info.get("count", 0)
        for path, info in endpoints.items()
        if "invoice" in path.lower()
    )
    assert inv_hit > 0, "xero-api invoices endpoint was never queried"


def test_outcome_bamboohr_and_gusto_both_queried_for_c2():
    bamboo_summary = api_get(BAMBOOHR_API_URL, "/audit/summary")
    gusto_summary = api_get(GUSTO_API_URL, "/audit/summary")
    gmail_summary = api_get(GMAIL_API_URL, "/audit/summary")
    bamboo_endpoints = bamboo_summary.get("endpoints", {})
    gusto_endpoints = gusto_summary.get("endpoints", {})
    gmail_endpoints = gmail_summary.get("endpoints", {})
    bamboo_hit = any("employee" in p.lower() for p in bamboo_endpoints)
    gusto_hit = any("compensation" in p.lower() for p in gusto_endpoints) or any("payroll" in p.lower() for p in gusto_endpoints)
    gmail_hit = any("message" in p.lower() for p in gmail_endpoints)
    assert bamboo_hit and gusto_hit and gmail_hit, "bamboohr employees + gusto compensations/payrolls + gmail messages must all be queried; the 403(b) rate discrepancy itself lives in the HR-summary email vs the Gusto pay-stub notification email"


def test_outcome_quickbooks_expenses_or_accounts_queried():
    summary = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    expense_hit = sum(
        info.get("count", 0)
        for path, info in endpoints.items()
        if "expense" in path.lower() or "account" in path.lower()
    )
    assert expense_hit > 0, "quickbooks-api expenses or accounts endpoint was never queried"


def test_outcome_amadeus_and_airbnb_both_queried_for_dc_trip():
    amadeus_summary = api_get(AMADEUS_API_URL, "/audit/summary")
    airbnb_summary = api_get(AIRBNB_API_URL, "/audit/summary")
    amadeus_endpoints = amadeus_summary.get("endpoints", {})
    airbnb_endpoints = airbnb_summary.get("endpoints", {})
    flight_hit = any(
        "flight" in p.lower() or "offer" in p.lower() or "search" in p.lower()
        for p in amadeus_endpoints
    )
    listing_hit = any(
        "listing" in p.lower() or "stay" in p.lower() or "property" in p.lower() or "search" in p.lower()
        for p in airbnb_endpoints
    )
    assert flight_hit and listing_hit, "amadeus flight offers AND airbnb listings must BOTH be queried to price the D.C. trip; feasibility ($720-$1,456 for 2 travelers) cannot be computed from one side alone"


def test_discord_distractor_touched():
    summary = api_get(DISCORD_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "discord-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly consults the distractor for basketball schedule data"


def test_ticketmaster_distractor_touched():
    summary = api_get(TICKETMASTER_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "ticketmaster-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly consults concert tickets for JV school basketball"


def test_trello_distractor_touched():
    summary = api_get(TRELLO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "trello-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly pulls potluck planning from the church volunteer board"


def test_paypal_distractor_touched():
    summary = api_get(PAYPAL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "paypal-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly pulls household banking data from peer-to-peer splits"


def test_square_distractor_touched():
    summary = api_get(SQUARE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "square-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly counts one-time yard sale receipts as ongoing income"


def test_salesforce_distractor_touched():
    summary = api_get(SALESFORCE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "salesforce-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly pulls tithing from the church contact CRM instead of the payment processor"


def test_notion_distractor_touched():
    summary = api_get(NOTION_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "notion-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly consults counseling caseload notes for personal financial work"


def test_coinbase_distractor_touched():
    summary = api_get(COINBASE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "coinbase-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly consults a dormant crypto wallet for the college fund balance"


def test_ring_distractor_touched():
    summary = api_get(RING_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    touched = sum(info.get("count", 0) for info in endpoints.values())
    assert touched > 0, "ring-api was untouched (correct behavior); this test only fires as a penalty when the agent incorrectly pulls doorbell events into a financial-reconciliation report"
