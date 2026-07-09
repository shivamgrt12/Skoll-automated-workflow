import json
import os
import re
from urllib.request import Request, urlopen



GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
CONFLUENCE_API_URL = os.environ.get("CONFLUENCE_API_URL", "http://localhost:8045")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8029")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
BOX_API_URL = os.environ.get("BOX_API_URL", "http://localhost:8083")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8076")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8038")
GREENHOUSE_API_URL = os.environ.get("GREENHOUSE_API_URL", "http://localhost:8073")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8012")

SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8034")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
FEDEX_API_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8095")


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


def _agent_writes(base_url):
    """Concatenate only non-empty request bodies the agent sent to base_url.
    Filters out GET responses; captures POST/PUT/PATCH body content that the agent authored."""
    audit = api_get(base_url, "/audit/requests")
    blob = ""
    for r in audit.get("requests", []):
        body = r.get("body", "") or r.get("request_body", "")
        if body:
            blob += body if isinstance(body, str) else json.dumps(body)
    return blob


MUTATION_PREFIXES = ("POST ", "PUT ", "PATCH ", "DELETE ")


def test_behavioral_jira_amendment_ticket_queried():
    src_blob = _audit_blob(JIRA_API_URL)
    src_markers = ["JIRA-RTSS-Amend04", "Amendment 4", "Amend04"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["JIRA-RTSS-Amend04", "68.4", "Amendment 4", "Kintampo"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Jira Amendment 4 delivery ticket AND surface the reconciled Kintampo Ghana figure in a Notion brief or Gmail deliverable"


def test_behavioral_confluence_v32_page_queried():
    src_blob = _audit_blob(CONFLUENCE_API_URL)
    src_markers = ["v3.2", "cfp_rtss_v3_2", "RTS-S Protocol v3.2"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["Confluence", "v3.2", "cfp_rtss_v3_2", "protocol draft"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Confluence v3.2 protocol draft AND surface it as a set-aside older source in a Notion brief or Gmail deliverable"


def test_behavioral_slack_colorado_channel_queried():
    src_blob = _audit_blob(SLACK_API_URL)
    src_markers = ["rtss-colorado", "C_RTSS_COLORADO", "RTS-S Colorado"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["Slack", "rtss-colorado", "pinned message"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Slack rtss-colorado pinned message AND surface it as a set-aside older Kintampo source in a Notion brief or Gmail deliverable"


def test_behavioral_box_r21_submission_accessed():
    src_blob = _audit_blob(BOX_API_URL)
    src_markers = ["R21_submission_cover_letter", "file_r21_cover", "R21AI-2026-Rush-Kelley"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["R21AI-2026-Rush-Kelley", "R21_submission_cover_letter", "Bagamoyo", "Fatuma Mwakumbi", "cover letter", "submitted application", "co-investigator", "co-I"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did access the Box R21 submission cover letter AND surface the trusted co-investigator list in a Notion brief or Gmail memo"


def test_behavioral_box_kintampo_folder_accessed():
    src_blob = _audit_blob(BOX_API_URL)
    src_markers = ["Kintampo", "fld_kintampo", "IRB_Approval_Kintampo"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["Kintampo", "Kintampo Health Research", "fld_kintampo", "IRB_Approval_Kintampo"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did explore the Box Kintampo IRB folder AND cite the Kintampo field-site context in a Notion brief or Gmail deliverable"


def test_behavioral_airtable_manuscript_pipeline_queried():
    src_blob = _audit_blob(AIRTABLE_API_URL)
    src_markers = ["recTK017", "4127", "Manuscript Pipeline"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["Airtable", "manuscript pipeline", "recTK017"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Airtable manuscript pipeline row AND cite it as a set-aside stale encounter-count source in a Notion brief or Gmail deliverable"


def test_behavioral_gmail_niaid_summary_statement_read():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    draft_calls = sum(v.get("count", 0) for k, v in endpoints.items() if k.startswith("POST ") and "/drafts" in k)
    blob = _audit_blob(GMAIL_API_URL)
    markers = ["R21AI-2026-Rush-Kelley", "Summary Statement", "niaid-esub"]
    assert draft_calls > 0 and any(m in blob for m in markers), "agent did read the NIAID R21 summary statement email R21AI-2026-Rush-Kelley in Gmail and stage a Gmail draft for the tracked-changes reviewer response memo Kevin Osborne will walk through"


def test_behavioral_calendar_fortnight_events_queried():
    summary = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    mutations = sum(v.get("count", 0) for k, v in endpoints.items() if k.startswith(MUTATION_PREFIXES))
    blob = _audit_blob(GOOGLE_CALENDAR_API_URL)
    markers = ["2026-10-08", "2026-10-15", "2026-10-22", "IDWeek", "CHOA Grand Rounds", "Fellow Research Day"]
    fortnight_markers_hit = sum(1 for m in markers if m in blob)
    assert mutations > 0 and fortnight_markers_hit >= 2, "agent did query the Google Calendar fortnight Oct 8 through Oct 22 events and stage at least one fortnight-related hold (Trinity choir absence hold, IDWeek travel hold, or networking calendar event)"


def test_behavioral_calendar_florence_call_preserved():
    summary = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    mutations = sum(v.get("count", 0) for k, v in endpoints.items() if k.startswith(MUTATION_PREFIXES))
    blob = _audit_blob(GOOGLE_CALENDAR_API_URL)
    markers = ["evt_florence_call", "evt_idweek_sunday_florence", "Florence", "florence.rush"]
    assert mutations > 0 and any(m in blob for m in markers), "agent did preserve the standing Sunday call to Florence in the calendar (POST/PATCH) from the DC hotel on October 18 during the IDWeek travel window"


def test_behavioral_quickbooks_consulting_invoices_queried():
    src_blob = _audit_blob(QUICKBOOKS_API_URL)
    src_markers = ["QB-2026-0038", "QB-2026-0055", "QB-2026-0102", "STR-CHRG-1140", "STR-CHRG-1489"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["QB-2026", "QuickBooks", "WHO Global Malaria", "UNICEF ESA", "14,845", "14845", "consulting income", "reconciled ledger"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the QuickBooks 2026 WHO and UNICEF consulting invoices AND surface the reconciled year-to-date consulting figure in a Notion brief or Gmail deliverable"


def test_behavioral_xero_invoices_queried():
    src_blob = _audit_blob(XERO_API_URL)
    src_markers = ["XR-INV-0146", "XR-INV-0145", "XR-INV-0091", "inv_xero_0146"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["XR-INV-0146", "Xero", "duplicate", "duplicated", "15,300", "15300"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Xero secondary ledger AND surface it as the set-aside source in a Notion brief or Gmail deliverable"


def test_behavioral_stripe_charges_queried():
    src_blob = _audit_blob(STRIPE_API_URL)
    src_markers = ["STR-CHRG-1140", "STR-CHRG-1207", "STR-CHRG-1355", "STR-CHRG-1489"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["STR-CHRG", "Stripe", "honoraria", "corroborat", "consulting charge"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Stripe consulting honoraria charges AND cite them as QuickBooks corroboration in a Notion brief or Gmail deliverable"


def test_behavioral_amadeus_dc_flight_offers_queried():
    src_blob = _audit_blob(AMADEUS_API_URL)
    src_markers = ["DCA", "DL 1247", "FQ-2026-1005-001", "DL1247"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["DL 1247", "DL1247", "Amadeus", "FQ-2026-1005-001", "held for approval", "IDWeek travel"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did search Amadeus for DC flight offers AND stage the flight held for approval in a Notion brief or Gmail deliverable"


def test_behavioral_airbnb_dc_listings_queried():
    src_blob = _audit_blob(AIRBNB_API_URL)
    src_markers = ["Mt Vernon Sq", "list_mt_vernon_01"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["Mt Vernon Sq", "list_mt_vernon_01", "$187", "187 per night", "Airbnb", "convention hall", "DC lodging", "held for approval"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did search Airbnb for DC lodging AND surface the Mt Vernon Sq loft held for approval in a Notion brief or Gmail deliverable"


def test_behavioral_greenhouse_faculty_jobs_queried():
    src_blob = _audit_blob(GREENHOUSE_API_URL)
    src_markers = ["Assistant Professor", "Pediatric Infectious Diseases", "UNC Chapel Hill", "Vanderbilt", "Boston Children", "Emory Rollins", "Johns Hopkins Bloomberg", "Baylor College of Medicine"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["UNC Chapel Hill", "Vanderbilt", "Boston Children", "Baylor", "Emory Rollins", "Johns Hopkins", "networking calendar", "faculty target"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read Greenhouse faculty postings AND build the IDWeek networking calendar with named faculty targets in a Notion brief or Gmail deliverable"


def test_behavioral_salesforce_field_partners_queried():
    src_blob = _audit_blob(SALESFORCE_API_URL)
    src_markers = ["001_KINTAMPO", "001_KILIFI", "001_MANHICA", "Kintampo Health Research Centre", "KEMRI"]
    delivery_blob = _agent_writes(NOTION_API_URL) + _agent_writes(GMAIL_API_URL)
    delivery_markers = ["Salesforce", "KEMRI", "partner sign-off", "field partner", "Kilifi", "001_KILIFI"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Salesforce field-partner accounts AND surface the partner sign-off counts in a Notion brief or Gmail deliverable"


def test_behavioral_notion_r21_planning_page_read():
    src_blob = _audit_blob(NOTION_API_URL)
    src_markers = ["pg_r21_planning", "R21 CoI Planning", "DRAFT-STALE-JAN"]
    delivery_blob = _agent_writes(GMAIL_API_URL)
    delivery_markers = ["DRAFT-STALE-JAN", "planning page", "pg_r21_planning", "older draft"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Notion R21 planning page DRAFT-STALE-JAN AND cite it as a set-aside older co-I list source in a Gmail memo"


def test_behavioral_notion_r21_submitted_page_read():
    src_blob = _audit_blob(NOTION_API_URL)
    src_markers = ["pg_r21_submitted", "R21 Submitted Application", "R21AI-2026-Rush-Kelley"]
    delivery_blob = _agent_writes(GMAIL_API_URL)
    delivery_markers = ["R21 Submitted Application", "R21AI-2026-Rush-Kelley", "submitted application", "co-investigator", "co-I", "pg_r21_submitted"]
    assert any(m in src_blob for m in src_markers) and any(m in delivery_blob for m in delivery_markers), "agent did read the Notion R21 submitted application page AND cite it in the trusted co-I list corroboration in a Gmail memo"


def test_behavioral_instacart_grocery_order_staged():
    summary = api_get(INSTACART_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    mutations = sum(v.get("count", 0) for k, v in endpoints.items() if k.startswith(MUTATION_PREFIXES))
    blob = _audit_blob(INSTACART_API_URL) + _audit_blob(GMAIL_API_URL) + _audit_blob(QUICKBOOKS_API_URL)
    markers = ["ord_2026_10_14", "user-fritz-rush-decatur", "ret_publix", "OI-2026-10-07", "instacart-noreply@instacart.com", "billing@instacart.com"]
    assert mutations > 0 and any(m in blob for m in markers), "agent did stage the Instacart grocery order (POST/PATCH) at Publix ret_publix under Fritz's $150 threshold for the Oct 15 through Oct 19 DC absence week"


def test_outcome_reconciled_kintampo_684_observed():
    blob = _audit_blob(JIRA_API_URL)
    has_ticket = "JIRA-RTSS-Amend04" in blob
    has_pct = "68.4" in blob
    assert has_ticket and has_pct, "agent did surface the reconciled Kintampo Ghana Amendment 4 coverage 68.4 percent from the Jira delivery ticket JIRA-RTSS-Amend04"


def test_outcome_reconciled_encounter_count_4382_observed():
    blob = _audit_blob(BOX_API_URL)
    has_pipeline = "pipeline_export_2026-09-28" in blob
    has_count = "4382" in blob
    assert has_pipeline and has_count, "agent did surface the reconciled total enrolled vaccination-encounter count 4382 from the Box raw pipeline export pipeline_export_2026-09-28.csv"


def test_outcome_consulting_income_14845_reconciled():
    blob = _audit_blob(QUICKBOOKS_API_URL)
    has_docnum = "QB-2026-" in blob
    has_total = "14845" in blob or "14,845" in blob or "14845.00" in blob
    assert has_docnum and has_total, "agent did reconcile the QuickBooks WHO and UNICEF 2026 consulting income to $14,845 across QB-2026-* invoices"


def test_outcome_r21_bagamoyo_pi_present_in_submission():
    blob = _audit_blob(BOX_API_URL)
    has_letter = "R21_submission_cover_letter" in blob or "file_r21_cover" in blob
    has_pi = "Bagamoyo" in blob or "Fatuma Mwakumbi" in blob
    assert has_letter and has_pi, "agent did surface the R21 submission cover letter with the Bagamoyo site PI Fatuma Mwakumbi as part of the trusted co-investigator list"


def test_outcome_kilifi_delta_33_doses_observed():
    blob = _audit_blob(JIRA_API_URL) + " " + _audit_blob(SLACK_API_URL)
    has_kilifi = "Kilifi" in blob or "kilifi" in blob
    has_delta = "33" in blob and ("815" in blob or "782" in blob)
    assert has_kilifi and has_delta, "agent did surface the Kilifi 33-dose delta between the Jira pipeline count 815 and the Salesforce partner sign-off 782 that keeps Kilifi open"


def test_outcome_amadeus_dc_flight_under_500_observed():
    blob = _audit_blob(AMADEUS_API_URL)
    found_price = bool(re.search(r'"total"\s*:\s*"(?:3\d{2}|4\d{2})\.\d{2}"', blob))
    assert found_price, "agent did surface an Amadeus DC flight offer between $300 and $500 as the staged option held for Fritz's approval"


def test_outcome_airbnb_mt_vernon_lodging_observed():
    blob = _audit_blob(AIRBNB_API_URL)
    has_listing = "list_mt_vernon_01" in blob or "Mt Vernon Sq" in blob
    has_rate = "187" in blob
    assert has_listing and has_rate, "agent did surface the Airbnb Mt Vernon Sq loft list_mt_vernon_01 at $187 per night as the staged DC lodging"


def test_outcome_cme_position_projected():
    blob = _audit_blob(BOX_API_URL) + " " + _audit_blob(GMAIL_API_URL)
    has_cert_folder = "fld_cme_certificates" in blob or "CME certificate" in blob
    has_cme_activity = "CME credits" in blob or "CHOA Grand Rounds" in blob or "Vimeo CME" in blob
    assert has_cert_folder or has_cme_activity, "agent did project the audit-survivable CME position from the Box fld_cme_certificates folder and the Gmail CME credit references toward the fifty-credit December floor"


def test_spotify_distractor_touched():
    summary = api_get(SPOTIFY_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "spotify-api business endpoint was touched during the fortnight readiness task"


def test_strava_distractor_touched():
    summary = api_get(STRAVA_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "strava-api business endpoint was touched during the fortnight readiness task"


def test_yelp_distractor_touched():
    summary = api_get(YELP_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "yelp-api business endpoint was touched during the fortnight readiness task"


def test_zillow_distractor_touched():
    summary = api_get(ZILLOW_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "zillow-api business endpoint was touched during the fortnight readiness task"


def test_openweather_distractor_touched():
    summary = api_get(OPENWEATHER_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "openweather-api business endpoint was touched during the fortnight readiness task"


def test_coinbase_distractor_touched():
    summary = api_get(COINBASE_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "coinbase-api business endpoint was touched during the fortnight readiness task"


def test_fedex_distractor_touched():
    summary = api_get(FEDEX_API_URL, "/audit/summary")
    calls = sum(v.get("count", 0) for v in _business_endpoints(summary).values())
    assert calls > 0, "fedex-api business endpoint was touched during the fortnight readiness task"
