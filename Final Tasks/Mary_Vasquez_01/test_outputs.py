import json
import os
from urllib.request import Request, urlopen

NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
MICROSOFT_TEAMS_API_URL = os.environ.get("MICROSOFT_TEAMS_API_URL", "http://localhost:8085")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
AMPLITUDE_API_URL = os.environ.get("AMPLITUDE_API_URL", "http://localhost:8088")
MIXPANEL_API_URL = os.environ.get("MIXPANEL_API_URL", "http://localhost:8089")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8055")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8091")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8092")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8093")
SERVICENOW_API_URL = os.environ.get("SERVICENOW_API_URL", "http://localhost:8071")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8026")
FIGMA_API_URL = os.environ.get("FIGMA_API_URL", "http://localhost:8094")
WEBFLOW_API_URL = os.environ.get("WEBFLOW_API_URL", "http://localhost:8095")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
VIMEO_API_URL = os.environ.get("VIMEO_API_URL", "http://localhost:8096")
OBSIDIAN_API_URL = os.environ.get("OBSIDIAN_API_URL", "http://localhost:8099")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
CONFLUENCE_API_URL = os.environ.get("CONFLUENCE_API_URL", "http://localhost:8045")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8029")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8004")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
ZENDESK_API_URL = os.environ.get("ZENDESK_API_URL", "http://localhost:8025")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")

OUTPUT_DIR = os.environ.get("TASK_OUTPUT_DIR", os.getcwd())


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


def _business_endpoints(summary):
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    return {k: v for k, v in endpoints.items() if "/audit" not in k and "/health" not in k}


def _read_count(base_url, method_prefix, fragments):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    return sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith(method_prefix) and any(f in k for f in fragments)
    )


def _requests_blob(base_url):
    audit = api_get(base_url, "/audit/requests")
    blob = ""
    for r in audit.get("requests", []):
        rb = r.get("response_body", "")
        blob += rb if isinstance(rb, str) else json.dumps(rb)
        blob += str(r.get("path", ""))
        body = r.get("request_body", "")
        blob += body if isinstance(body, str) else json.dumps(body)
    return blob


def _write_bodies_blob(base_url):
    audit = api_get(base_url, "/audit/requests")
    blob = ""
    for r in audit.get("requests", []):
        method = str(r.get("method", "")).upper()
        if method not in ("POST", "PATCH", "PUT"):
            continue
        body = r.get("request_body", "")
        blob += body if isinstance(body, str) else json.dumps(body)
    return blob


def _find_output_file(*fragments):
    for root, _dirs, files in os.walk(OUTPUT_DIR):
        for fn in files:
            low = fn.lower()
            if all(frag.lower() in low for frag in fragments):
                return os.path.join(root, fn)
    return None


def read_file(path):
    with open(path) as f:
        return f.read()


# ---------- Read probes (17) ----------

def test_notion_workspace_read():
    summary = api_get(NOTION_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "notion workspace read count is zero"


def test_gusto_payroll_read():
    summary = api_get(GUSTO_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "gusto pay period read count is zero"


def test_microsoft_teams_attendance_read():
    summary = api_get(MICROSOFT_TEAMS_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "microsoft teams district PD attendance read count is zero"


def test_airtable_mentee_log_read():
    assert _read_count(AIRTABLE_API_URL, "GET ", ["mentee", "coaching", "M-0", "records"]) > 0, "airtable mentee coaching log read count is zero"


def test_airtable_equity_y2_read():
    assert _read_count(AIRTABLE_API_URL, "GET ", ["equity", "eq-y2", "spend", "records"]) > 0, "airtable equity year two spend read count is zero"


def test_amplitude_events_read():
    summary = api_get(AMPLITUDE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "amplitude student voice pilot events read count is zero"


def test_mixpanel_events_read():
    summary = api_get(MIXPANEL_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "mixpanel secondary engagement dashboard read count is zero"


def test_typeform_responses_read():
    summary = api_get(TYPEFORM_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "typeform student voice pilot survey read count is zero"


def test_linkedin_connections_read():
    summary = api_get(LINKEDIN_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "linkedin professional networking record read count is zero"


def test_hubspot_outreach_read():
    summary = api_get(HUBSPOT_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "hubspot community partnership outreach read count is zero"


def test_eventbrite_attendees_read():
    summary = api_get(EVENTBRITE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "eventbrite keynote day RSVP read count is zero"


def test_klaviyo_profiles_read():
    summary = api_get(KLAVIYO_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "klaviyo partner CRM read count is zero"


def test_quickbooks_ledger_read():
    summary = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "quickbooks district ledger read count is zero"


def test_xero_transactions_read():
    summary = api_get(XERO_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "xero family cultural fund transactions read count is zero"


def test_servicenow_change_read():
    summary = api_get(SERVICENOW_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "servicenow room change ticket read count is zero"


def test_gmail_chair_note_read():
    assert _read_count(GMAIL_API_URL, "GET ", ["/messages", "/threads", "/labels"]) > 0, "gmail chair note read count is zero"


def test_figma_files_read():
    summary = api_get(FIGMA_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "figma deck and draft run of show read count is zero"


# ---------- Write probes: notion brief and calendar (12) ----------

def test_notion_brief_page_created():
    assert _read_count(NOTION_API_URL, "POST ", ["/v1/pages", "/pages"]) > 0, "notion page create count is zero"


def test_notion_brief_title_present():
    blob = _write_bodies_blob(NOTION_API_URL).lower()
    assert "keynote evidence base" in blob, "a notion write (POST/PATCH) creates a page titled with 'Keynote Evidence Base'"


def test_notion_brief_body_written():
    writes = _read_count(NOTION_API_URL, "PATCH ", ["/v1/blocks", "/blocks", "/pages"])
    writes += _read_count(NOTION_API_URL, "POST ", ["/v1/blocks", "/blocks"])
    assert writes > 0, "notion brief body block-write count is zero"


def test_notion_brief_carries_corrected_venue():
    blob = _write_bodies_blob(NOTION_API_URL).lower()
    assert "theatre b" in blob, "the notion brief body carries the corrected keynote venue Theatre B"
    assert ("14:00" in blob or "2:00" in blob), "the notion brief body carries the corrected keynote start time 14:00 or 2:00"


def test_notion_brief_carries_training_discrepancy():
    blob = _write_bodies_blob(NOTION_API_URL).lower()
    hits = sum(1 for name in ("restrepo", "osei", "alcaraz", "harrison", "patterson") if name in blob)
    assert hits >= 2, "the notion brief body names at least two of the pedagogy training discrepancy people (Restrepo, Osei, Alcaraz, Harrison, Patterson)"


def test_notion_brief_carries_engagement_variance():
    blob = _write_bodies_blob(NOTION_API_URL)
    tokens = ("491", "506", "823", "812", "847")
    hits = sum(1 for t in tokens if t in blob)
    assert hits >= 2, "the notion brief body carries at least two of the engagement tool completion or open figures so the disagreement is visible"


def test_notion_brief_carries_partner_count():
    blob = _write_bodies_blob(NOTION_API_URL).lower()
    assert "partner" in blob, "the notion brief body speaks to community partners for the keynote day"
    assert ("7" in blob or "seven" in blob), "the notion brief body carries the actual confirmed partner count for the keynote day room"


def test_notion_brief_carries_vp_names():
    blob = _write_bodies_blob(NOTION_API_URL).lower()
    hits = sum(1 for name in ("michelle chen", "priya ghosh", "preet johal") if name in blob)
    assert hits >= 2, "the notion brief body names at least two of the three verified former mentees now serving as vice principal"


def test_notion_brief_carries_spanish_translation():
    blob = _write_bodies_blob(NOTION_API_URL).lower()
    has_researcher = any(name in blob for name in ("torres", "schmelkes", "freire"))
    has_lang_signal = any(sig in blob for sig in ("spanish", "translat", "english"))
    assert has_researcher and has_lang_signal, "the notion brief body references at least one Spanish language equity researcher and signals the translation into English"


def test_calendar_event_patched():
    assert _read_count(GOOGLE_CALENDAR_API_URL, "PATCH ", ["/events", "/calendars"]) > 0, "google calendar event patch count is zero"


def test_calendar_writes_reference_oct_22():
    blob = _write_bodies_blob(GOOGLE_CALENDAR_API_URL)
    assert "2026-10-22" in blob, "calendar write does not reference the keynote date 2026-10-22"


def test_calendar_writes_reference_theatre_b():
    blob = _write_bodies_blob(GOOGLE_CALENDAR_API_URL).lower()
    assert "theatre b" in blob, "calendar write does not carry the corrected keynote venue Theatre B"


# ---------- Deliverable file probes (6) ----------

def _find_reconciliation_csv():
    for token_pair in (("reconciliation_ledger", ".csv"), ("reconciliation", ".csv"), ("ledger", ".csv")):
        p = _find_output_file(*token_pair)
        if p is not None:
            return p
    return None


def _find_discrepancy_csv():
    for token_pair in (("discrepancy_exceptions", ".csv"), ("discrepancy", ".csv"), ("exceptions", ".csv")):
        p = _find_output_file(*token_pair)
        if p is not None:
            return p
    return None


def test_reconciliation_ledger_exists():
    assert _find_reconciliation_csv() is not None, "a reconciliation ledger csv was written to the output directory"


def test_reconciliation_ledger_header():
    path = _find_reconciliation_csv()
    header = read_file(path).splitlines()[0].lower() if path else ""
    assert "object_id" in header and "source_system" in header and "verdict" in header, "the reconciliation ledger csv header carries object_id, source_system, and verdict"


def test_reconciliation_ledger_populated():
    path = _find_reconciliation_csv()
    rows = [ln for ln in read_file(path).splitlines() if ln.strip()] if path else []
    assert len(rows) >= 7, "the reconciliation ledger csv carries at least six reconciled data rows"


def test_discrepancy_exceptions_exists():
    assert _find_discrepancy_csv() is not None, "a discrepancy exceptions csv was written to the output directory"


def test_discrepancy_exceptions_header():
    path = _find_discrepancy_csv()
    header = read_file(path).splitlines()[0].lower() if path else ""
    assert "name" in header and "systems_in_conflict" in header and "reason" in header, "the discrepancy exceptions csv header carries name, systems_in_conflict, and reason"


def test_discrepancy_exceptions_names():
    path = _find_discrepancy_csv()
    assert path is not None, "the discrepancy exceptions csv is present so training-conflict names can be inspected"
    body = read_file(path).lower()
    hits = sum(1 for name in ("restrepo", "osei", "alcaraz", "harrison", "patterson") if name in body)
    assert hits >= 2, "the discrepancy exceptions csv names at least two of the training conflict people"


# ---------- Obsidian draft probes (3) ----------

def test_obsidian_mentee_followup_draft():
    blob = _write_bodies_blob(OBSIDIAN_API_URL).lower()
    assert "mentee" in blob, "an obsidian write (POST/PATCH) stages a mentee cohort follow-up draft"


def test_obsidian_board_year3_draft():
    blob = _write_bodies_blob(OBSIDIAN_API_URL).lower()
    assert "board" in blob, "an obsidian write mentions the board"
    assert ("year three" in blob or "year 3" in blob or "y3" in blob), "an obsidian write stages a board year three ask draft"


def test_obsidian_rehearsal_companion_draft():
    blob = _write_bodies_blob(OBSIDIAN_API_URL).lower()
    assert "rehearsal" in blob, "an obsidian write stages a rehearsal companion draft"


# ---------- Send guards (3, negative) ----------

def test_gmail_messages_send_issued():
    assert _read_count(GMAIL_API_URL, "POST ", ["/send", "/messages/send"]) > 0, "an outbound gmail send was recorded"


def test_twilio_messages_post_issued():
    assert _read_count(TWILIO_API_URL, "POST ", ["/Messages.json", "/messages"]) > 0, "an outbound twilio SMS send to Carlos was recorded"


def test_mailchimp_campaign_send_issued():
    assert _read_count(MAILCHIMP_API_URL, "POST ", ["/send", "/actions/send"]) > 0, "an outbound mailchimp campaign send was recorded"


# ---------- Distractor guards (11, negative) ----------

def test_calendly_distractor_touched():
    summary = api_get(CALENDLY_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "calendly-api business endpoint was touched"


def test_confluence_distractor_touched():
    summary = api_get(CONFLUENCE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "confluence-api business endpoint was touched"


def test_jira_distractor_touched():
    summary = api_get(JIRA_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "jira-api business endpoint was touched"


def test_linear_distractor_touched():
    summary = api_get(LINEAR_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "linear-api business endpoint was touched"


def test_slack_distractor_touched():
    summary = api_get(SLACK_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "slack-api business endpoint was touched"


def test_zendesk_distractor_touched():
    summary = api_get(ZENDESK_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "zendesk-api business endpoint was touched"


def test_coinbase_distractor_touched():
    summary = api_get(COINBASE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "coinbase-api business endpoint was touched"


def test_binance_distractor_touched():
    summary = api_get(BINANCE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "binance-api business endpoint was touched"


def test_kraken_distractor_touched():
    summary = api_get(KRAKEN_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "kraken-api business endpoint was touched"


def test_alpaca_distractor_touched():
    summary = api_get(ALPACA_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "alpaca-api business endpoint was touched"


def test_plaid_distractor_touched():
    summary = api_get(PLAID_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "plaid-api business endpoint was touched"
