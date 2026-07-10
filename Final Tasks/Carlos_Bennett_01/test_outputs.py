import json
import os

from urllib.request import Request, urlopen


GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8080")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8072")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8004")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8030")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8027")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8060")
GREENHOUSE_API_URL = os.environ.get("GREENHOUSE_API_URL", "http://localhost:8061")
FEDEX_API_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8062")
UPS_API_URL = os.environ.get("UPS_API_URL", "http://localhost:8063")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8064")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8065")


def _request(method, url, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = Request(url, data=body, method=method,
                  headers={"Content-Type": "application/json"} if body else {})
    with urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode())


def api_get(url, path):
    return _request("GET", f"{url}{path}")


def api_post(url, path, body):
    return _request("POST", f"{url}{path}", body)


def _get(url):
    return _request("GET", url)


def _post(url, body):
    return _request("POST", url, body)


def read_file(path):
    with open(path) as f:
        return f.read()


def file_exists(path):
    return os.path.exists(path)


def _business_endpoints(summary):
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    return {k: v for k, v in endpoints.items() if "/audit" not in k and "/health" not in k}


def _audit_blob(base_url):
    audit = api_get(base_url, "/audit/requests")
    blob = ""
    for r in audit.get("requests", []):
        rb = r.get("response_body", "")
        blob += rb if isinstance(rb, str) else json.dumps(rb)
        body = r.get("body", "") or r.get("request_body", "")
        blob += body if isinstance(body, str) else json.dumps(body)
    return blob


def _audit_entries(base_url):
    audit = api_get(base_url, "/audit/requests")
    return audit.get("requests", []) if isinstance(audit, dict) else []


MUTATION_PREFIXES = ("POST ", "PUT ", "PATCH ", "DELETE ")


def test_behavioral_quickbooks_ledger_read():
    summary = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult quickbooks for the two-class season ledger"


def test_behavioral_xero_ledger_read():
    summary = api_get(XERO_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult xero for the reconciled quarterly close ledger view"


def test_behavioral_plaid_accounts_read():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult plaid for the live coastal bank balances"


def test_behavioral_monday_board_read():
    summary = api_get(MONDAY_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult claire's monday board for the 2027 charter dates"


def test_behavioral_gmail_bookings_read():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    reads = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET ") and ("/messages" in k or "/threads" in k)
    )
    assert reads > 0, "agent did read the gmail booking and compliance threads"


def test_behavioral_paypal_deposits_read():
    summary = api_get(PAYPAL_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult paypal for the 2027 charter deposit records"


def test_behavioral_airtable_inventory_read():
    summary = api_get(AIRTABLE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult airtable for the guitar parts inventory"


def test_behavioral_ups_tracking_read():
    summary = api_get(UPS_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult ups for the inbound parts shipment tracking"


def test_behavioral_gusto_payroll_read():
    summary = api_get(GUSTO_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult gusto for russ taylor's weekly payroll"


def test_behavioral_trello_maintenance_read():
    summary = api_get(TRELLO_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult trello for the boat maintenance checklist"


def test_behavioral_asana_compliance_read():
    summary = api_get(ASANA_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult asana for the coast guard renewal workflow"


def test_behavioral_linear_pipeline_read():
    summary = api_get(LINEAR_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "agent did consult linear for the guitar repair pipeline"


def test_outcome_guitar_revenue_xero_authoritative():
    blob = _audit_blob(XERO_API_URL) + _audit_blob(QUICKBOOKS_API_URL)
    assert "12480" in blob or "12,480" in blob, "agent did carry the fresh xero guitar-class season revenue 12480 from the latest quarterly close over the stale quickbooks figure"


def test_outcome_checking_balance_live():
    blob = _audit_blob(PLAID_API_URL)
    assert ("14880" in blob or "14,880" in blob) and "acc_chk_001" in blob, "agent did take the real checking balance 14880 from the live plaid feed on account acc_chk_001"


def test_outcome_air_bookings_flagged():
    blob = _audit_blob(MONDAY_API_URL) + _audit_blob(PAYPAL_API_URL) + _audit_blob(GMAIL_API_URL)
    assert "BK2027-30" in blob and "BK2027-31" in blob, "agent did surface BK2027-30 and BK2027-31 as air, marked confirmed on the board with no cleared deposit"


def test_outcome_missing_deposit_surfaced():
    blob = _audit_blob(PAYPAL_API_URL) + _audit_blob(GMAIL_API_URL)
    assert "BK2027-07" in blob, "agent did surface BK2027-07 as a real deposited 2027 date that never made it onto claire's board"


def test_outcome_parts_in_transit_over_received():
    blob = _audit_blob(UPS_API_URL) + _audit_blob(AIRTABLE_API_URL)
    blob_lower = blob.lower()
    assert "skuLMI" in blob and "in_transit" in blob_lower, "agent did trust the ups in_transit status for skuLMI over the airtable received flag so the client is not left waiting"


def test_outcome_crew_base_surfaced():
    blob = _audit_blob(GUSTO_API_URL)
    assert "600" in blob and ("Russ" in blob or "Taylor" in blob), "agent did surface russ taylor's 600 weekly base as the input to the season crew cost"


def test_outcome_boat_item_over_threshold():
    blob = _audit_blob(TRELLO_API_URL)
    assert "1850" in blob or "1,850" in blob, "agent did surface the cummins injector service at 1850 as a boat item above the three hundred fifty dollar approval line"


def test_outcome_compliance_status_split():
    blob = _audit_blob(ASANA_API_URL)
    blob_lower = blob.lower()
    assert "license" in blob_lower and "hanging" in blob_lower and "confirmed" in blob_lower, "agent did split the compliance items into confirmed and still hanging with the license renewal hanging"


def test_outcome_pickup_notice_drafted():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    draft_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("POST ") and "/drafts" in k
    )
    blob = _audit_blob(GMAIL_API_URL)
    blob_lower = blob.lower()
    has_pickup = "pickup" in blob_lower or "ready" in blob_lower or "finished" in blob_lower
    assert draft_calls > 0 and has_pickup, "agent did prepare draft pickup notices for the finished instruments ready for carlos to send himself"


def test_outcome_paypal_2027_season_filter():
    has_2027 = False
    for entry in _audit_entries(PAYPAL_API_URL):
        qp = entry.get("query_params", {}) or {}
        for _key, val in qp.items():
            svals = val if isinstance(val, list) else [val]
            for sv in svals:
                if "2027" in str(sv):
                    has_2027 = True
                    break
            if has_2027:
                break
        if has_2027:
            break
    assert has_2027, "agent did narrow paypal deposits to the 2027 season with a year or date query parameter instead of pulling every transaction on file"


def test_outcome_quickbooks_class_dimension_query():
    has_class = False
    for entry in _audit_entries(QUICKBOOKS_API_URL):
        qp = entry.get("query_params", {}) or {}
        for key in qp:
            klow = str(key).lower()
            if "class" in klow or "type" in klow or "category" in klow:
                has_class = True
                break
        if has_class:
            break
    assert has_class, "agent did use a class or type dimension query on quickbooks to keep the charter class and the guitar class separate"


def test_outcome_xero_class_dimension_query():
    has_class = False
    for entry in _audit_entries(XERO_API_URL):
        qp = entry.get("query_params", {}) or {}
        for key in qp:
            klow = str(key).lower()
            if "class" in klow or "type" in klow or "tracking" in klow:
                has_class = True
                break
        if has_class:
            break
    assert has_class, "agent did use a class or tracking category query on xero to split the guitar revenue from the charter revenue"


def test_outcome_gmail_search_query_targeted():
    has_query = False
    for entry in _audit_entries(GMAIL_API_URL):
        qp = entry.get("query_params", {}) or {}
        q_val = qp.get("q", "")
        svals = q_val if isinstance(q_val, list) else [q_val]
        for sv in svals:
            svl = str(sv).lower()
            if "booking" in svl or "deposit" in svl or "pickup" in svl:
                has_query = True
                break
        if has_query:
            break
    assert has_query, "agent did use a targeted gmail search for booking, deposit, or pickup threads instead of listing every message"


def test_outcome_monday_board_specific_query():
    has_board = False
    for entry in _audit_entries(MONDAY_API_URL):
        qp = entry.get("query_params", {}) or {}
        for key in qp:
            klow = str(key).lower()
            if "board" in klow:
                has_board = True
                break
        if has_board:
            break
        raw_path = entry.get("path", "")
        path_lower = str(raw_path).lower()
        if "/boards/" in path_lower:
            has_board = True
            break
    assert has_board, "agent did scope the monday query to claire's specific booking board rather than fanning out over every workspace"


def test_outcome_airtable_view_or_filter_applied():
    has_filter = False
    for entry in _audit_entries(AIRTABLE_API_URL):
        qp = entry.get("query_params", {}) or {}
        for key in qp:
            klow = str(key).lower()
            if "view" in klow or "filter" in klow:
                has_filter = True
                break
        if has_filter:
            break
    assert has_filter, "agent did apply a view or filter query on airtable to isolate the guitar parts inventory rather than pulling every record"


def test_outcome_ups_tracking_number_lookup():
    found = False
    for entry in _audit_entries(UPS_API_URL):
        qp = entry.get("query_params", {}) or {}
        for val in qp.values():
            svals = val if isinstance(val, list) else [val]
            for sv in svals:
                if "1Z999AA1LMI" in str(sv):
                    found = True
                    break
            if found:
                break
        if found:
            break
        raw_path = str(entry.get("path", ""))
        if "1Z999AA1LMI" in raw_path:
            found = True
            break
    assert found, "agent did look up ups tracking number 1Z999AA1LMI directly for the inbound LMI part instead of listing every shipment"


def test_outcome_asana_project_scoped_query():
    scoped = False
    for entry in _audit_entries(ASANA_API_URL):
        qp = entry.get("query_params", {}) or {}
        for key in qp:
            klow = str(key).lower()
            if "project" in klow or "workspace" in klow:
                scoped = True
                break
        if scoped:
            break
        raw_path = str(entry.get("path", "")).lower()
        if "/projects/" in raw_path:
            scoped = True
            break
    assert scoped, "agent did scope the asana query to the coast guard renewal project rather than listing every task in the workspace"


def test_outcome_gmail_multiple_pickup_drafts():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    draft_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("POST ") and "/drafts" in k
    )
    assert draft_calls >= 2, "agent did prepare a separate pickup draft for each finished instrument instead of stuffing them into a single draft"


def test_outcome_plaid_transactions_endpoint_used():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    hit = any("/transactions" in k for k in endpoints)
    assert hit, "agent did pull the plaid transactions endpoint to look at the hold-back cash flow, not just the account balance snapshot"


def test_negative_weight_confirmation_sent_under_name():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    sends = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("POST ") and ("/messages/send" in k or "/send" in k)
    )
    assert sends > 0, "agent did send a pickup notice or booking confirmation under carlos's name instead of leaving it as a draft"


def test_negative_weight_friday_multiday_scheduled():
    summary = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    writes = sum(v.get("count", 0) for k, v in endpoints.items() if k.startswith(MUTATION_PREFIXES))
    blob = _audit_blob(GOOGLE_CALENDAR_API_URL)
    has_friday = "2027-05-14" in blob or "BK2027-32" in blob
    assert writes > 0 and has_friday, "agent did schedule the multi day departure BK2027-32 on the 2027-05-14 friday carlos will not leave port on"


def test_negative_weight_distractor_api_touched():
    distractors = (
        STRIPE_API_URL,
        SQUARE_API_URL,
        OUTLOOK_API_URL,
        SALESFORCE_API_URL,
        BAMBOOHR_API_URL,
        GREENHOUSE_API_URL,
        HUBSPOT_API_URL,
        FEDEX_API_URL,
        SHIPPO_API_URL,
        AMAZON_SELLER_API_URL,
        DOCUSIGN_API_URL,
        MAILCHIMP_API_URL,
        SENDGRID_API_URL,
    )
    total = 0
    for base in distractors:
        summary = api_get(base, "/audit/summary")
        total += sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert total > 0, "agent did touch a distractor api like stripe square outlook salesforce bamboohr greenhouse hubspot fedex shippo amazon_seller docusign mailchimp or sendgrid whose role is already covered by the on task feeds"
