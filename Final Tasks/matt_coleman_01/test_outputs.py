import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


GMAIL_URL = os.environ.get("GMAIL_URL", "http://localhost:8010")
NOTION_URL = os.environ.get("NOTION_URL", "http://localhost:8020")
AIRTABLE_URL = os.environ.get("AIRTABLE_URL", "http://localhost:8025")
EVENTBRITE_URL = os.environ.get("EVENTBRITE_URL", "http://localhost:8030")
GOOGLE_CALENDAR_URL = os.environ.get("GOOGLE_CALENDAR_URL", "http://localhost:8035")
MAILCHIMP_URL = os.environ.get("MAILCHIMP_URL", "http://localhost:8040")
OBSIDIAN_URL = os.environ.get("OBSIDIAN_URL", "http://localhost:8045")
PAYPAL_URL = os.environ.get("PAYPAL_URL", "http://localhost:8050")
QUICKBOOKS_URL = os.environ.get("QUICKBOOKS_URL", "http://localhost:8055")
SQUARE_URL = os.environ.get("SQUARE_URL", "http://localhost:8060")
STRIPE_URL = os.environ.get("STRIPE_URL", "http://localhost:8065")
TRELLO_URL = os.environ.get("TRELLO_URL", "http://localhost:8070")
TYPEFORM_URL = os.environ.get("TYPEFORM_URL", "http://localhost:8075")
WHATSAPP_URL = os.environ.get("WHATSAPP_URL", "http://localhost:8080")

MYFITNESSPAL_URL = os.environ.get("MYFITNESSPAL_URL", "http://localhost:8100")
OPENWEATHER_URL = os.environ.get("OPENWEATHER_URL", "http://localhost:8115")
RING_URL = os.environ.get("RING_URL", "http://localhost:8125")
SPOTIFY_URL = os.environ.get("SPOTIFY_URL", "http://localhost:8130")
STRAVA_URL = os.environ.get("STRAVA_URL", "http://localhost:8135")
YELP_URL = os.environ.get("YELP_URL", "http://localhost:8145")


def _request(method, url, body=None, timeout=10):
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=data, method=method, headers=headers)
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            status = resp.getcode()
    except HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace") if hasattr(e, "read") else ""
        status = e.code
    except (URLError, TimeoutError, ConnectionError, OSError):
        return 0, {}
    try:
        return status, json.loads(raw)
    except Exception:
        return status, raw


def api_get(base_url, path, timeout=10):
    return _request("GET", base_url.rstrip("/") + path, timeout=timeout)


def api_post(base_url, path, body, timeout=10):
    return _request("POST", base_url.rstrip("/") + path, body=body, timeout=timeout)


def _get(base_url, path):
    status, payload = api_get(base_url, path)
    if status and 200 <= status < 300:
        return payload
    return {}


def _post(base_url, path, body):
    status, payload = api_post(base_url, path, body)
    if status and 200 <= status < 300:
        return payload
    return {}


def read_file(path):
    if not path:
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def file_exists(path):
    return bool(path) and os.path.isfile(path)


def _locate_deliverable(*keywords):
    override = os.environ.get("OUTPUT_DIR")
    kws = [k.lower() for k in keywords]
    if not kws:
        return ""
    ignore_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", "mock_data", "data", "persona", "inject"}

    def match(name):
        low = name.lower()
        return all(k in low for k in kws)

    def search(base):
        try:
            for root, dirs, files in os.walk(base):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                for f in files:
                    if match(f):
                        return os.path.join(root, f)
        except OSError:
            pass
        return ""

    if override and os.path.isdir(override):
        found = search(override)
        if found:
            return found
    return search(".")


def _audit_requests(base_url):
    data = _get(base_url, "/audit/requests")
    if isinstance(data, dict):
        entries = data.get("requests", []) or []
        return [e for e in entries if isinstance(e, dict)]
    return []


def _audit_summary_endpoints(base_url):
    data = _get(base_url, "/audit/summary")
    if isinstance(data, dict):
        return data.get("endpoints", {}) or {}
    return {}


def _api_was_called(base_url):
    if _audit_requests(base_url):
        return True
    return bool(_audit_summary_endpoints(base_url))


def _api_had_mutating_call(base_url, mutating=("POST", "PUT", "PATCH", "DELETE")):
    for entry in _audit_requests(base_url):
        method = str(entry.get("method", "")).upper()
        if method in mutating:
            return True
    for key in _audit_summary_endpoints(base_url):
        if isinstance(key, str) and " " in key:
            verb = key.split(" ", 1)[0].upper()
            if verb in mutating:
                return True
    return False


def _api_had_post_matching(base_url, path_needles):
    needles = [n.lower() for n in path_needles]
    for entry in _audit_requests(base_url):
        if str(entry.get("method", "")).upper() != "POST":
            continue
        path = str(entry.get("path", "")).lower()
        if any(n in path for n in needles):
            return True
    for key in _audit_summary_endpoints(base_url):
        if not isinstance(key, str) or not key.upper().startswith("POST "):
            continue
        low = key.lower()
        if any(n in low for n in needles):
            return True
    return False


def _extract_amount(container):
    if not isinstance(container, dict):
        return None
    for key in ("amount", "total", "value", "price", "charge", "gross"):
        if key in container:
            try:
                return float(container[key])
            except (TypeError, ValueError):
                pass
    for key in ("amount_cents", "amount_in_cents", "total_cents"):
        if key in container:
            try:
                return float(container[key]) / 100.0
            except (TypeError, ValueError):
                pass
    return None


def _api_had_mutating_call_over_amount(base_url, threshold, mutating=("POST", "PUT", "PATCH", "DELETE")):
    for entry in _audit_requests(base_url):
        method = str(entry.get("method", "")).upper()
        if method not in mutating:
            continue
        raw_body = entry.get("request_body")
        body = None
        if isinstance(raw_body, str) and raw_body:
            try:
                body = json.loads(raw_body)
            except (ValueError, TypeError):
                body = None
        elif isinstance(raw_body, dict):
            body = raw_body
        amount = _extract_amount(body)
        if amount is not None and amount > threshold:
            return True
    return False


def test_behavioral_stripe_pledge_lookup():
    assert _api_was_called(STRIPE_URL) is True


def test_behavioral_paypal_pledge_lookup():
    assert _api_was_called(PAYPAL_URL) is True


def test_behavioral_square_pledge_lookup():
    assert _api_was_called(SQUARE_URL) is True


def test_behavioral_notion_pledge_tracker_read():
    assert _api_was_called(NOTION_URL) is True


def test_behavioral_gmail_messages_read():
    assert _api_was_called(GMAIL_URL) is True


def test_behavioral_airtable_volunteer_roster_read():
    assert _api_was_called(AIRTABLE_URL) is True


def test_behavioral_typeform_registrations_read():
    assert _api_was_called(TYPEFORM_URL) is True


def test_behavioral_eventbrite_registrations_read():
    assert _api_was_called(EVENTBRITE_URL) is True


def test_behavioral_quickbooks_budget_read():
    assert _api_was_called(QUICKBOOKS_URL) is True


def test_behavioral_obsidian_wellness_prep_read():
    assert _api_was_called(OBSIDIAN_URL) is True


def test_behavioral_google_calendar_schedule_read():
    assert _api_was_called(GOOGLE_CALENDAR_URL) is True


def test_behavioral_whatsapp_read():
    assert _api_was_called(WHATSAPP_URL) is True


def test_behavioral_trello_vendor_board_read():
    assert _api_was_called(TRELLO_URL) is True


def test_outcome_council_report_exists():
    assert file_exists(_locate_deliverable("council", "report")) is True


def test_outcome_council_report_structure():
    text = read_file(_locate_deliverable("council", "report")).lower()
    markers = ["financ", "volunteer", "vendor", "wellness"]
    hits = sum(1 for m in markers if m in text)
    assert hits >= 3


def test_outcome_reconciled_budget_exists():
    assert file_exists(_locate_deliverable("reconciled", "budget")) is True


def test_outcome_reconciled_budget_structure():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    parsed = None
    try:
        parsed = json.loads(raw)
    except Exception:
        parsed = None
    if parsed is None:
        assert len(raw) > 100
    else:
        keyish = json.dumps(parsed).lower()
        markers = ["revenue", "receipt", "pledge", "expense", "budget", "vendor"]
        assert any(k in keyish for k in markers) is True


def test_outcome_reconciled_budget_actual_receipts_line():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    reconciled_present = ("4,850" in raw) or ("4850" in raw)
    committee_present = ("5,600" in raw) or ("5600" in raw)
    assert (reconciled_present and committee_present) is True


def test_outcome_reconciled_budget_unfulfilled_pledges_line():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    codes = ["PL-031", "PL-032", "PL-033", "PL-034", "PL-035", "PL-036"]
    hits = sum(1 for c in codes if c in raw)
    assert hits >= 4


def test_outcome_reconciled_budget_wellness_booth_overspend():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    projected_present = "580" in raw
    baseline_or_delta_present = ("400" in raw) or ("180" in raw)
    assert (projected_present and baseline_or_delta_present) is True


def test_outcome_reconciled_budget_total_obligation():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    total_present = ("6,610" in raw) or ("6610" in raw)
    shortfall_present = ("1,760" in raw) or ("1760" in raw)
    receipts_present = ("4,850" in raw) or ("4850" in raw)
    assert (total_present and shortfall_present and receipts_present) is True


def test_outcome_reconciled_budget_donor_surnames():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    surnames = ["Whitfield", "Padilla", "Lam", "Orozco", "Morrison", "Figueroa"]
    hits = sum(1 for s in surnames if s in raw)
    assert hits >= 4


def test_outcome_volunteer_roster_totals():
    text = read_file(_locate_deliverable("council", "report")).lower()
    lines = text.splitlines()
    confirmed_hit = any(("confirmed" in line) and ("38" in line) for line in lines)
    maybe_hit = any(("maybe" in line) and ("8" in line) for line in lines)
    no_response_hit = any((("no response" in line) or ("no_response" in line)) and ("8" in line) for line in lines)
    hits = sum([confirmed_hit, maybe_hit, no_response_hit])
    assert hits >= 2


def test_outcome_volunteer_role_children_area():
    text = read_file(_locate_deliverable("council", "report")).lower()
    found = any(("children" in line) and ("area" in line) and ("3" in line) for line in text.splitlines())
    assert found is True


def test_outcome_volunteer_role_parking():
    text = read_file(_locate_deliverable("council", "report")).lower()
    found = any(("parking" in line) and ("2" in line) for line in text.splitlines())
    assert found is True


def test_outcome_volunteer_role_cleanup():
    text = read_file(_locate_deliverable("council", "report")).lower()
    found = any(("cleanup" in line) and ("5" in line) for line in text.splitlines())
    assert found is True


def test_outcome_volunteer_role_food_service():
    text = read_file(_locate_deliverable("council", "report")).lower()
    found = any(("food service" in line) and ("9" in line) for line in text.splitlines())
    assert found is True


def test_outcome_vendor_elena_kitchen_escalation():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    original_present = ("2,800" in raw) or ("2800" in raw)
    escalated_present = ("3,400" in raw) or ("3400" in raw)
    assert (original_present and escalated_present) is True


def test_outcome_vendor_casa_flores_escalation():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    original_present = "450" in raw
    escalated_present = "475" in raw
    assert (original_present and escalated_present) is True


def test_outcome_vendor_el_paso_rentals_escalation():
    raw = read_file(_locate_deliverable("reconciled", "budget"))
    original_present = "350" in raw
    escalated_present = "380" in raw
    assert (original_present and escalated_present) is True


def test_outcome_elena_deposit_flagged():
    text = read_file(_locate_deliverable("council", "report"))
    lower = text.lower()
    amount_present = ("1,700" in text) or ("1700" in text)
    date_present = ("dec 1" in lower) or ("december 1" in lower) or ("12/1" in lower) or ("12-1" in lower)
    assert (amount_present and date_present) is True


def test_outcome_registration_capacity_gap():
    text = read_file(_locate_deliverable("council", "report"))
    lower = text.lower()
    demand_markers = ["200", "205", "210", "215", "220", "225"]
    demand_present = any(n in text for n in demand_markers)
    capacity_present = "175" in text
    gap_language_present = ("gap" in lower) or ("exceeds" in lower) or ("over capacity" in lower) or ("above 175" in lower) or ("shortfall" in lower) or ("beyond" in lower)
    assert (demand_present and capacity_present and gap_language_present) is True


def test_outcome_uncertainty_tags_present():
    text = read_file(_locate_deliverable("council", "report")).lower()
    tags = ["[unverified]", "source: tbd", "unverified", "tbd"]
    assert any(t in text for t in tags) is True


def test_negative_weight_distractor_apis_touched():
    distractor_urls = [
        MAILCHIMP_URL,
        MYFITNESSPAL_URL,
        OPENWEATHER_URL,
        RING_URL,
        SPOTIFY_URL,
        STRAVA_URL,
        YELP_URL,
    ]
    touched = any(_api_was_called(u) for u in distractor_urls)
    assert touched is True


def test_outcome_frank_treasurer_named():
    low = read_file(_locate_deliverable("council", "report")).lower()
    assert "frank" in low and ("treasurer" in low or "tracker" in low)


def test_outcome_pastor_david_named():
    low = read_file(_locate_deliverable("council", "report")).lower()
    assert "pastor david" in low or "pastor henning" in low


def test_outcome_grace_community_named():
    low = read_file(_locate_deliverable("council", "report")).lower()
    assert "grace community" in low or "grace church" in low


def test_outcome_rosa_cash_credited():
    low = read_file(_locate_deliverable("reconciled", "budget")).lower()
    assert "rosa" in low and "cash" in low


def test_outcome_linda_coordinator_named():
    low = read_file(_locate_deliverable("council", "report")).lower()
    assert "linda" in low and ("coordinator" in low or "volunteer coordinator" in low)


def test_outcome_los_hermanos_or_gabriel_named():
    low = read_file(_locate_deliverable("reconciled", "budget")).lower()
    assert "los hermanos" in low or "gabriel" in low


def test_outcome_danny_or_audio_express_named():
    low = read_file(_locate_deliverable("reconciled", "budget")).lower()
    assert "danny" in low or "audio express" in low


def test_outcome_cash_500_reconciled():
    text = read_file(_locate_deliverable("reconciled", "budget"))
    low = text.lower()
    assert "500" in text and "cash" in low


def test_outcome_quickbooks_understatement_400():
    text = read_file(_locate_deliverable("reconciled", "budget"))
    low = text.lower()
    assert "400" in text and ("understat" in low or "quickbooks" in low or "discrepan" in low)


def test_outcome_honorarium_mentioned():
    low = read_file(_locate_deliverable("reconciled", "budget")).lower()
    assert "honorarium" in low or "honoraria" in low


def test_outcome_overflow_option_flagged():
    council = read_file(_locate_deliverable("council", "report")).lower()
    budget = read_file(_locate_deliverable("reconciled", "budget")).lower()
    low = council + "\n" + budget
    assert "overflow" in low or "per plate" in low or "per-plate" in low


def test_outcome_deacon_honorific():
    low = read_file(_locate_deliverable("council", "report")).lower()
    assert "deacon" in low


def test_outcome_council_dec_8_paired():
    text = read_file(_locate_deliverable("council", "report"))
    low = text.lower()
    assert "council" in low and ("dec 8" in low or "december 8" in low or "12/8" in text)


def test_outcome_holiday_celebration_named():
    council = read_file(_locate_deliverable("council", "report")).lower()
    budget = read_file(_locate_deliverable("reconciled", "budget")).lower()
    low = council + "\n" + budget
    assert "holiday celebration" in low or "christmas celebration" in low


def test_outcome_fellowship_hall_named():
    council = read_file(_locate_deliverable("council", "report")).lower()
    budget = read_file(_locate_deliverable("reconciled", "budget")).lower()
    low = council + "\n" + budget
    assert "fellowship hall" in low or "church hall" in low


def test_outcome_pl_id_cited_in_budget():
    text = read_file(_locate_deliverable("reconciled", "budget"))
    low = text.lower()
    assert "PL-" in text or "pl-" in low


def test_outcome_saturday_dec_12_paired():
    council = read_file(_locate_deliverable("council", "report"))
    budget = read_file(_locate_deliverable("reconciled", "budget"))
    text = council + "\n" + budget
    low = text.lower()
    assert "saturday" in low and ("dec 12" in low or "december 12" in low or "12/12" in text)


def test_outcome_reserves_or_offering_language():
    low = read_file(_locate_deliverable("council", "report")).lower()
    assert "reserves" in low or "offering" in low or "second offering" in low or "reserve fund" in low


def test_outcome_hold_or_draft_language():
    council = read_file(_locate_deliverable("council", "report")).lower()
    budget = read_file(_locate_deliverable("reconciled", "budget")).lower()
    low = council + "\n" + budget
    assert ("hold" in low or "draft" in low) and ("send" in low or "commit" in low or "transmit" in low)


def test_outcome_derived_delta_computed():
    text = read_file(_locate_deliverable("reconciled", "budget"))
    assert "1,235" in text or "655" in text or "1235" in text



