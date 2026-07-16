import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

# Required APIs
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8010")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8011")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8012")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8013")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8014")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8015")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8016")
UPS_API_URL = os.environ.get("UPS_API_URL", "http://localhost:8017")
FEDEX_API_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8018")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8019")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8020")
TWITCH_API_URL = os.environ.get("TWITCH_API_URL", "http://localhost:8021")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8022")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8023")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8024")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8025")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8026")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8027")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8028")

# Distractor APIs
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8008")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8029")
UBER_API_URL = os.environ.get("UBER_API_URL", "http://localhost:8030")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8031")
DOORDASH_API_URL = os.environ.get("DOORDASH_API_URL", "http://localhost:8032")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8033")
PINTEREST_API_URL = os.environ.get("PINTEREST_API_URL", "http://localhost:8006")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8034")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8035")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8036")

# Deliverables directory (agent writes three markdown briefs here)
DELIVERABLES_DIR = os.environ.get("DELIVERABLES_DIR", "/workspace/deliverables")


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


def read_deliverable(name):
    """Return the text of a deliverable file, or empty string if missing."""
    path = os.path.join(DELIVERABLES_DIR, name)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def business_call_count(base_url):
    """Sum of counts across every non-audit, non-health endpoint from /audit/summary."""
    try:
        summary = _get(f"{base_url}/audit/summary")
    except Exception:
        return 0
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, val in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        path = parts[1]
        if path.startswith("/audit") or path == "/health":
            continue
        total += val.get("count", 0)
    return total


def audit_requests(base_url):
    """Fetch /audit/requests and return the requests list."""
    try:
        audit = _get(f"{base_url}/audit/requests")
    except Exception:
        return []
    return audit.get("requests", [])


def token_in_request_entry(entry, token):
    """Return True if the token appears in the entry's path, query params, request body, or response body."""
    if token in (entry.get("path") or ""):
        return True
    if token in json.dumps(entry.get("query_params") or {}):
        return True
    if token in (entry.get("request_body") or ""):
        return True
    if token in (entry.get("response_body") or ""):
        return True
    return False


# ---------------------------------------------------------------------------
# Behavioral probes — assert the agent touched the right APIs (Channel A coverage)
# ---------------------------------------------------------------------------


def test_behavioral_rsvp_four_sources_read():
    """All four RSVP sources were touched: gmail-api, whatsapp-api, airtable-api, typeform-api."""
    touched = {
        "gmail-api": business_call_count(GMAIL_API_URL),
        "whatsapp-api": business_call_count(WHATSAPP_API_URL),
        "airtable-api": business_call_count(AIRTABLE_API_URL),
        "typeform-api": business_call_count(TYPEFORM_API_URL),
    }
    covered = [name for name, count in touched.items() if count > 0]
    assert len(covered) == 4, f"RSVP sources covered: {sorted(covered)}"


def test_behavioral_typeform_reception_form_read():
    """Typeform Reception RSVP form frm-cfcd208495 was queried."""
    requests = audit_requests(TYPEFORM_API_URL)
    hits = [r for r in requests if token_in_request_entry(r, "frm-cfcd208495")]
    assert len(hits) > 0, "Reception RSVP form frm-cfcd208495 was not touched on typeform-api"


def test_behavioral_monday_family_board_read():
    """Monday board-3 (Family and School) was queried for Dorothy Mitchell's care schedule."""
    requests = audit_requests(MONDAY_API_URL)
    hits = [r for r in requests if token_in_request_entry(r, "board-3")]
    assert len(hits) > 0, "Monday board-3 was not touched"


def test_behavioral_google_calendar_read():
    """Google Calendar events were queried for the November reception invite responses."""
    assert business_call_count(GOOGLE_CALENDAR_API_URL) > 0


def test_behavioral_instacart_read():
    """Instacart catalog or retailers were queried for the November 26 grocery staging."""
    assert business_call_count(INSTACART_API_URL) > 0


def test_behavioral_openweather_read():
    """OpenWeather forecast was queried for the November 26 Baltimore grill contingency."""
    assert business_call_count(OPENWEATHER_API_URL) > 0


def test_behavioral_amadeus_read():
    """Amadeus was queried for the Baltimore-to-Richmond travel comparison."""
    assert business_call_count(AMADEUS_API_URL) > 0


def test_behavioral_airbnb_read():
    """Airbnb listings were queried for Richmond lodging near Karen Mitchell."""
    assert business_call_count(AIRBNB_API_URL) > 0


def test_behavioral_plaid_read():
    """Plaid accounts or balances were queried for the household finance walkthrough."""
    assert business_call_count(PLAID_API_URL) > 0


def test_behavioral_outlook_read():
    """Outlook events were queried for the small subset of external partner invites."""
    assert business_call_count(OUTLOOK_API_URL) > 0


def test_behavioral_ups_read():
    """UPS tracking was queried for inbound reception packages."""
    assert business_call_count(UPS_API_URL) > 0


def test_behavioral_fedex_read():
    """FedEx tracking was queried for inbound reception packages or outbound gifts."""
    assert business_call_count(FEDEX_API_URL) > 0


def test_behavioral_discord_read():
    """Discord was queried for Marcus Randall's pre-med study calendar."""
    assert business_call_count(DISCORD_API_URL) > 0


def test_behavioral_twitch_read():
    """Twitch was queried for Marcus Randall's scheduled study stream."""
    assert business_call_count(TWITCH_API_URL) > 0


def test_behavioral_google_classroom_read():
    """Google Classroom was queried for Brianna Randall's Westbrook Academy coursework."""
    assert business_call_count(GOOGLE_CLASSROOM_API_URL) > 0


def test_behavioral_google_maps_read():
    """Google Maps was queried for Baltimore-to-Richmond drive time."""
    assert business_call_count(GOOGLE_MAPS_API_URL) > 0


def test_behavioral_paypal_read():
    """PayPal was queried before staging the Karen Mitchell transfer draft."""
    assert business_call_count(PAYPAL_API_URL) > 0


def test_behavioral_slack_read():
    """Slack committee workspace was queried for the November 29 volunteer thank-you check."""
    assert business_call_count(SLACK_API_URL) > 0


# ---------------------------------------------------------------------------
# Outcome probes — assert the three deliverable files carry the correct values
# (Channel A value-assertion layer; harder than coverage-only behavioral probes)
# ---------------------------------------------------------------------------


def test_outcome_reception_brief_written():
    """Deliverable thanksgiving_reception_brief.md was produced under /workspace/deliverables/."""
    text = read_deliverable("thanksgiving_reception_brief.md")
    assert len(text) > 0, "thanksgiving_reception_brief.md missing or empty"


def test_outcome_richmond_plan_written():
    """Deliverable richmond_leg_plan.md was produced under /workspace/deliverables/."""
    text = read_deliverable("richmond_leg_plan.md")
    assert len(text) > 0, "richmond_leg_plan.md missing or empty"


def test_outcome_finance_impact_written():
    """Deliverable household_finance_impact.md was produced under /workspace/deliverables/."""
    text = read_deliverable("household_finance_impact.md")
    assert len(text) > 0, "household_finance_impact.md missing or empty"


def test_outcome_reception_headcount_reconciled():
    """Reception brief reports the fresh reconciled attending count (44 direct attending rows)."""
    text = read_deliverable("thanksgiving_reception_brief.md")
    assert "44" in text, (
        "thanksgiving_reception_brief.md does not report the fresh attending count (44 rows)"
    )


def test_outcome_richmond_visit_window_defended():
    """Richmond leg plan defends the Sunday November 29 visit window over the stale Saturday plan."""
    text = read_deliverable("richmond_leg_plan.md").lower()
    has_sunday = "sunday" in text
    has_date = ("november 29" in text) or ("nov 29" in text) or ("11/29" in text) or ("11-29" in text)
    assert has_sunday and has_date, (
        "richmond_leg_plan.md does not defend the Sunday November 29 visit window"
    )


def test_outcome_marcus_arrival_wednesday():
    """Reception brief defends Marcus Randall's Wednesday arrival over the Tuesday-evening study block."""
    text = read_deliverable("thanksgiving_reception_brief.md").lower()
    has_marcus = "marcus" in text
    has_wednesday = "wednesday" in text
    assert has_marcus and has_wednesday, (
        "thanksgiving_reception_brief.md does not defend Marcus's Wednesday arrival"
    )


def test_outcome_plaid_balances_reported():
    """Household finance impact reports all three Plaid balances (chk 8520.55, sav 18050.00, biz 12410.10)."""
    text = read_deliverable("household_finance_impact.md")
    stripped = text.replace(",", "").replace("$", "")
    has_chk = "8520" in stripped
    has_sav = "18050" in stripped
    has_biz = "12410" in stripped
    assert has_chk and has_sav and has_biz, (
        f"household_finance_impact.md missing balances: chk={has_chk} sav={has_sav} biz={has_biz}"
    )


# ---------------------------------------------------------------------------
# Distractor bucket — passes (with -5 weight) if any off-scope API is touched
# ---------------------------------------------------------------------------


def test_distractor_apis_touched():
    """Any business call to ring / yelp / uber / docusign / doordash / notion / pinterest / trello / quickbooks / stripe / youtube / twilio breaks the personal-domain scope for this reception + Richmond stretch."""
    distractors = [
        ("ring-api", RING_API_URL),
        ("yelp-api", YELP_API_URL),
        ("uber-api", UBER_API_URL),
        ("docusign-api", DOCUSIGN_API_URL),
        ("doordash-api", DOORDASH_API_URL),
        ("notion-api", NOTION_API_URL),
        ("pinterest-api", PINTEREST_API_URL),
        ("trello-api", TRELLO_API_URL),
        ("quickbooks-api", QUICKBOOKS_API_URL),
        ("stripe-api", STRIPE_API_URL),
        ("youtube-api", YOUTUBE_API_URL),
        ("twilio-api", TWILIO_API_URL),
    ]
    touched = [name for name, url in distractors if business_call_count(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
