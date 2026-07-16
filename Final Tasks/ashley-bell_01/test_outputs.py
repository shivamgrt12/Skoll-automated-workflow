import json
import os
import subprocess
import sqlite3
import glob
from urllib.request import Request, urlopen

# ---- Required service URLs (Bell Modern pre-Modernism-Week back-office reset) ----
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8030")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8080")
WEBFLOW_API_URL = os.environ.get("WEBFLOW_API_URL", "http://localhost:8100")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")

# ---- Distractor service URLs (Bell Modern back-office reset should sit past these) ----
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
TWITTER_API_URL = os.environ.get("TWITTER_API_URL", "http://localhost:8061")
PINTEREST_API_URL = os.environ.get("PINTEREST_API_URL", "http://localhost:8006")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8058")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8059")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")


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
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()


def file_exists(path):
    return os.path.exists(path)


DELIVERABLE_ROOTS = [
    "data",
    ".",
    "../data",
    "../..",
    "output",
    "workspace",
]

# ---- Filename patterns for the six drafted artifacts ----
UNDERWRITER_PATTERNS = [
    "*underwriter_packet*",
    "*Underwriter_Packet*",
    "*underwriter*packet*",
    "*insurance_renewal*",
    "*renewal_packet*",
    "*ardent_renewal*",
]

ACCOUNTANT_PATTERNS = [
    "*accountant_quarterly*",
    "*Accountant_Quarterly*",
    "*Quarterly_File*",
    "*quarterly_reconciliation*",
    "*quarterly_pnl*",
    "*sarah_adams*",
]

RESTORATION_PATTERNS = [
    "*restoration_schedule*",
    "*Restoration_Schedule*",
    "*restoration_drop*",
    "*dave_cooper*",
    "*restorer_backlog*",
    "*backlog_walk*",
]

DOCENT_PATTERNS = [
    "*tour_docent*",
    "*docent_notes*",
    "*Docent_Notes*",
    "*modernism_week_tour*",
    "*route_docent*",
]

TOUR_LANDING_PATTERNS = [
    "*tour_landing*",
    "*Tour_Landing*",
    "*landing_copy*",
    "*Landing_Copy*",
    "*modernism_week_landing*",
]

SHOP_PUNCH_PATTERNS = [
    "*shop_punch*",
    "*Shop_Punch*",
    "*punch_list*",
    "*Punch_List*",
    "*shop_readiness*",
    "*tyler_shop*",
]


def _collect_files(patterns):
    hits = set()
    for pat in patterns:
        for root in DELIVERABLE_ROOTS:
            for p in glob.glob(f"{root}/{pat}"):
                if os.path.isfile(p):
                    hits.add(p)
            for p in glob.glob(f"{root}/**/{pat}", recursive=True):
                if os.path.isfile(p):
                    hits.add(p)
    return sorted(hits)


def _load_body(paths):
    body = ""
    for p in paths:
        try:
            body += read_file(p).lower() + "\n"
        except Exception:
            continue
    return body


def _summary_endpoints(base_url):
    try:
        summary = api_get(base_url, "/audit/summary")
    except Exception:
        return {}
    if not isinstance(summary, dict):
        return {}
    endpoints = summary.get("endpoints", {})
    return endpoints if isinstance(endpoints, dict) else {}


def _count_matches(endpoints, needle_lower):
    total = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        if needle_lower in key.lower():
            count = meta.get("count", 0)
            if isinstance(count, int):
                total += count
    return total


def _count_method_matches(endpoints, method, needle_lower):
    total = 0
    method_prefix = f"{method.upper()} "
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        if not key.startswith(method_prefix):
            continue
        if needle_lower in key.lower():
            count = meta.get("count", 0)
            if isinstance(count, int):
                total += count
    return total


def _business_call_total(base_url):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if "/audit" in klow or "/health" in klow:
            continue
        count = meta.get("count", 0)
        if isinstance(count, int):
            total += count
    return total


def _service_touched(base_url):
    return _business_call_total(base_url) > 0


# ==============================================================================
# Deliverable landing (six drafted artifacts)
# ==============================================================================


def test_underwriter_packet_document_landed():
    hits = _collect_files(UNDERWRITER_PATTERNS)
    assert len(hits) > 0, f"Underwriter Packet document missing; searched roots {DELIVERABLE_ROOTS}"


def test_accountant_quarterly_file_landed():
    hits = _collect_files(ACCOUNTANT_PATTERNS)
    assert len(hits) > 0, f"Accountant Quarterly File document missing; searched roots {DELIVERABLE_ROOTS}"


def test_restoration_drop_schedule_landed():
    hits = _collect_files(RESTORATION_PATTERNS)
    assert len(hits) > 0, f"Restoration drop schedule document missing; searched roots {DELIVERABLE_ROOTS}"


def test_tour_docent_notes_landed():
    hits = _collect_files(DOCENT_PATTERNS)
    assert len(hits) > 0, f"Docent notes document missing; searched roots {DELIVERABLE_ROOTS}"


def test_tour_landing_copy_landed():
    hits = _collect_files(TOUR_LANDING_PATTERNS)
    assert len(hits) > 0, f"Tour landing copy document missing; searched roots {DELIVERABLE_ROOTS}"


def test_shop_punch_list_landed():
    hits = _collect_files(SHOP_PUNCH_PATTERNS)
    assert len(hits) > 0, f"Shop punch list document missing; searched roots {DELIVERABLE_ROOTS}"


# ==============================================================================
# Underwriter packet sections
# ==============================================================================


def test_underwriter_packet_reconciled_schedule_section_present():
    body = _load_body(_collect_files(UNDERWRITER_PATTERNS))
    assert ("reconciled" in body) or ("schedule" in body) or ("inventory schedule" in body), \
        "underwriter packet lacks reconciled schedule content"


def test_underwriter_packet_top_of_schedule_section_present():
    body = _load_body(_collect_files(UNDERWRITER_PATTERNS))
    assert ("nakashima" in body) or ("eames" in body) or ("paul evans" in body) or ("kagan" in body) or ("top of schedule" in body), \
        "underwriter packet lacks top-of-schedule anchor pieces"


def test_underwriter_packet_valuation_section_present():
    body = _load_body(_collect_files(UNDERWRITER_PATTERNS))
    assert ("valuation" in body) or ("340" in body) or ("340,000" in body) or ("itemized" in body), \
        "underwriter packet lacks itemized valuation anchor"


def test_underwriter_packet_coverage_gap_section_present():
    body = _load_body(_collect_files(UNDERWRITER_PATTERNS))
    assert ("coverage" in body) and (("headroom" in body) or ("shortfall" in body) or ("gap" in body) or ("delta" in body)), \
        "underwriter packet lacks coverage gap language"


def test_underwriter_packet_ardent_questions_section_present():
    body = _load_body(_collect_files(UNDERWRITER_PATTERNS))
    assert ("laura" in body) or ("ardent" in body) or ("questions" in body) or ("underwriter" in body), \
        "underwriter packet lacks Ardent-side open questions"


def test_underwriter_packet_carries_340000_and_400000_anchors():
    body = _load_body(_collect_files(UNDERWRITER_PATTERNS))
    has_340 = ("$340,000" in body) or ("$340000" in body) or ("340,000" in body)
    has_400 = ("$400,000" in body) or ("$400000" in body) or ("400,000" in body)
    has_gap_language = ("headroom" in body) or ("shortfall" in body) or ("coverage gap" in body)
    assert has_340 and has_400 and has_gap_language, \
        f"underwriter anchors missing; 340k={has_340} 400k={has_400} gap_language={has_gap_language}"


# ==============================================================================
# Accountant quarterly file sections
# ==============================================================================


def test_accountant_file_revenue_section_present():
    body = _load_body(_collect_files(ACCOUNTANT_PATTERNS))
    assert ("revenue" in body) and (("cleared" in body) or ("realized" in body) or ("posted" in body)), \
        "accountant file lacks cleared-revenue language"


def test_accountant_file_lane_walk_section_present():
    body = _load_body(_collect_files(ACCOUNTANT_PATTERNS))
    has_card = ("card" in body) or ("stripe" in body) or ("square" in body)
    has_bank = ("bank" in body) or ("plaid" in body) or ("clearing" in body)
    has_ledger = ("invoice" in body) or ("ledger" in body) or ("sales" in body)
    assert has_card and has_bank and has_ledger, \
        f"accountant file lane walk incomplete; card={has_card} bank={has_bank} ledger={has_ledger}"


def test_accountant_file_consignment_trace_section_present():
    body = _load_body(_collect_files(ACCOUNTANT_PATTERNS))
    assert ("consignment" in body) and (("chen" in body) or ("designer" in body) or ("margaret" in body)), \
        "accountant file lacks consignment trace"


def test_accountant_file_recurring_fee_flag_section_present():
    body = _load_body(_collect_files(ACCOUNTANT_PATTERNS))
    has_fee = ("1,200" in body) or ("1200" in body) or ("$1,200" in body)
    has_hold = ("sign-off" in body) or ("sign off" in body) or ("hold" in body) or ("pause" in body) or ("pending" in body) or ("threshold" in body)
    assert has_fee and has_hold, \
        f"$1,200 dealer-listing fee flag missing; fee={has_fee} hold={has_hold}"


def test_accountant_file_net_margin_section_present():
    body = _load_body(_collect_files(ACCOUNTANT_PATTERNS))
    assert ("net" in body) and (("margin" in body) or ("22%" in body) or ("22 %" in body)), \
        "accountant file lacks net margin content"


def test_accountant_file_carries_1200_anchor():
    body = _load_body(_collect_files(ACCOUNTANT_PATTERNS))
    has_amount = ("$1,200" in body) or ("$1200" in body) or ("1,200" in body)
    has_context = ("dealer" in body) or ("1stdibs" in body) or ("listing" in body)
    assert has_amount and has_context, \
        f"accountant file lacks the $1,200 dealer-listing anchor with context; amount={has_amount} context={has_context}"


# ==============================================================================
# Restoration + tour + shop sections
# ==============================================================================


def test_restoration_schedule_kagan_flag_section_present():
    body = _load_body(_collect_files(RESTORATION_PATTERNS))
    has_piece = ("kagan" in body) and ("credenza" in body)
    has_conflict_language = ("unresolved" in body) or ("does not match" in body) or ("do not match" in body) \
        or ("conflict" in body) or ("mismatch" in body) or ("not settled" in body) or ("both dates" in body)
    assert has_piece and has_conflict_language, \
        f"restoration Kagan credenza flag missing; piece={has_piece} conflict_language={has_conflict_language}"


def test_restoration_schedule_dave_cooper_backlog_section_present():
    body = _load_body(_collect_files(RESTORATION_PATTERNS))
    assert ("dave" in body) or ("cooper" in body) or ("restorer" in body) or ("5 piece" in body) or ("five piece" in body), \
        "restoration schedule lacks Dave Cooper backlog content"


def test_tour_docent_notes_two_routes_section_present():
    body = _load_body(_collect_files(DOCENT_PATTERNS))
    assert ("route" in body) or ("alexander" in body) or ("desert modernism" in body) or ("architecture" in body), \
        "docent notes lack two-route content"


def test_tour_landing_copy_architecture_only_section_present():
    body = _load_body(_collect_files(TOUR_LANDING_PATTERNS))
    has_arch = ("architecture" in body) or ("modernism" in body) or ("alexander" in body)
    has_makers = ("makers" in body) or ("maker" in body) or ("designer" in body)
    assert has_arch and has_makers, \
        f"tour landing copy lacks architecture-and-makers anchor; arch={has_arch} makers={has_makers}"


def test_shop_punch_list_gates_section_present():
    body = _load_body(_collect_files(SHOP_PUNCH_PATTERNS))
    has_photo = "photo" in body
    has_dim = ("dimension" in body) or ("dim" in body)
    has_price = "price" in body
    assert has_photo and has_dim and has_price, \
        f"shop punch list gates incomplete; photo={has_photo} dim={has_dim} price={has_price}"


def test_shop_punch_list_120_piece_scope_section_present():
    body = _load_body(_collect_files(SHOP_PUNCH_PATTERNS))
    has_scope = ("120" in body) or ("accent" in body)
    has_gate_language = ("ready" in body) or ("blocking" in body) or ("missing" in body) \
        or ("photo" in body) or ("dimension" in body) or ("price" in body)
    assert has_scope and has_gate_language, \
        f"shop punch list scope+gate anchors missing; scope={has_scope} gate={has_gate_language}"


# ==============================================================================
# Per-service touched (15 required Bell Modern services)
# ==============================================================================


def test_gmail_messages_touched():
    endpoints = _summary_endpoints(GMAIL_API_URL)
    hits = _count_matches(endpoints, "message") + _count_matches(endpoints, "thread") + _count_matches(endpoints, "draft") + _count_matches(endpoints, "label")
    assert hits > 0, "gmail messages endpoints never queried"


def test_google_calendar_events_touched():
    endpoints = _summary_endpoints(GOOGLE_CALENDAR_API_URL)
    hits = _count_matches(endpoints, "event") + _count_matches(endpoints, "calendar") + _count_matches(endpoints, "attendee")
    assert hits > 0, "google calendar events endpoints never queried"


def test_outlook_mail_or_calendar_touched():
    endpoints = _summary_endpoints(OUTLOOK_API_URL)
    hits = (
        _count_matches(endpoints, "message")
        + _count_matches(endpoints, "mail")
        + _count_matches(endpoints, "folder")
        + _count_matches(endpoints, "event")
        + _count_matches(endpoints, "calendar")
    )
    assert hits > 0, "outlook mail/calendar endpoints never queried"


def test_quickbooks_ledger_touched():
    endpoints = _summary_endpoints(QUICKBOOKS_API_URL)
    hits = (
        _count_matches(endpoints, "invoice")
        + _count_matches(endpoints, "bill")
        + _count_matches(endpoints, "expense")
        + _count_matches(endpoints, "vendor")
        + _count_matches(endpoints, "payment")
        + _count_matches(endpoints, "ledger")
    )
    assert hits > 0, "quickbooks ledger endpoints never queried"


def test_xero_consignment_touched():
    endpoints = _summary_endpoints(XERO_API_URL)
    hits = (
        _count_matches(endpoints, "invoice")
        + _count_matches(endpoints, "bill")
        + _count_matches(endpoints, "contact")
        + _count_matches(endpoints, "account")
        + _count_matches(endpoints, "payment")
    )
    assert hits > 0, "xero consignment endpoints never queried"


def test_stripe_charges_touched():
    endpoints = _summary_endpoints(STRIPE_API_URL)
    hits = (
        _count_matches(endpoints, "charge")
        + _count_matches(endpoints, "payment_intent")
        + _count_matches(endpoints, "subscription")
        + _count_matches(endpoints, "customer")
        + _count_matches(endpoints, "invoice")
    )
    assert hits > 0, "stripe charges endpoints never queried"


def test_square_charges_touched():
    endpoints = _summary_endpoints(SQUARE_API_URL)
    hits = (
        _count_matches(endpoints, "payment")
        + _count_matches(endpoints, "order")
        + _count_matches(endpoints, "location")
        + _count_matches(endpoints, "transaction")
        + _count_matches(endpoints, "catalog")
    )
    assert hits > 0, "square payments endpoints never queried"


def test_plaid_bank_lane_touched():
    endpoints = _summary_endpoints(PLAID_API_URL)
    hits = (
        _count_matches(endpoints, "transaction")
        + _count_matches(endpoints, "account")
        + _count_matches(endpoints, "balance")
        + _count_matches(endpoints, "item")
    )
    assert hits > 0, "plaid bank lane endpoints never queried"


def test_airtable_records_touched():
    endpoints = _summary_endpoints(AIRTABLE_API_URL)
    hits = (
        _count_matches(endpoints, "base")
        + _count_matches(endpoints, "table")
        + _count_matches(endpoints, "record")
        + _count_matches(endpoints, "field")
    )
    assert hits > 0, "airtable inventory endpoints never queried"


def test_notion_workspace_touched():
    endpoints = _summary_endpoints(NOTION_API_URL)
    hits = (
        _count_matches(endpoints, "page")
        + _count_matches(endpoints, "database")
        + _count_matches(endpoints, "block")
        + _count_matches(endpoints, "workspace")
    )
    assert hits > 0, "notion provenance workspace never queried"


def test_hubspot_deals_touched():
    endpoints = _summary_endpoints(HUBSPOT_API_URL)
    hits = (
        _count_matches(endpoints, "contact")
        + _count_matches(endpoints, "deal")
        + _count_matches(endpoints, "ticket")
        + _count_matches(endpoints, "company")
        + _count_matches(endpoints, "engagement")
    )
    assert hits > 0, "hubspot deals endpoints never queried"


def test_trello_restoration_board_touched():
    endpoints = _summary_endpoints(TRELLO_API_URL)
    hits = (
        _count_matches(endpoints, "board")
        + _count_matches(endpoints, "list")
        + _count_matches(endpoints, "card")
        + _count_matches(endpoints, "checklist")
    )
    assert hits > 0, "trello restoration board endpoints never queried"


def test_monday_route_planning_touched():
    endpoints = _summary_endpoints(MONDAY_API_URL)
    hits = (
        _count_matches(endpoints, "board")
        + _count_matches(endpoints, "item")
        + _count_matches(endpoints, "update")
        + _count_matches(endpoints, "column")
        + _count_matches(endpoints, "group")
    )
    assert hits > 0, "monday route-planning endpoints never queried"


def test_webflow_tour_landing_touched():
    endpoints = _summary_endpoints(WEBFLOW_API_URL)
    hits = (
        _count_matches(endpoints, "site")
        + _count_matches(endpoints, "collection")
        + _count_matches(endpoints, "item")
        + _count_matches(endpoints, "page")
    )
    assert hits > 0, "webflow tour-landing endpoints never queried"


def test_docusign_envelopes_touched():
    endpoints = _summary_endpoints(DOCUSIGN_API_URL)
    hits = (
        _count_matches(endpoints, "envelope")
        + _count_matches(endpoints, "recipient")
        + _count_matches(endpoints, "document")
        + _count_matches(endpoints, "template")
    )
    assert hits > 0, "docusign envelopes endpoints never queried"


# ==============================================================================
# Cross-service reconciliation walks
# ==============================================================================


def test_card_and_bank_lanes_walked_across_stripe_square_plaid():
    stripe_hits = _business_call_total(STRIPE_API_URL)
    square_hits = _business_call_total(SQUARE_API_URL)
    plaid_hits = _business_call_total(PLAID_API_URL)
    card = stripe_hits + square_hits
    assert card > 0 and plaid_hits > 0, \
        f"card-and-bank lane walk missing a source; stripe={stripe_hits} square={square_hits} plaid={plaid_hits}"


def test_quickbooks_and_xero_walk_crosses_ledgers():
    qb_hits = _business_call_total(QUICKBOOKS_API_URL)
    xr_hits = _business_call_total(XERO_API_URL)
    assert qb_hits > 0 and xr_hits > 0, \
        f"quickbooks-xero cross-ledger walk incomplete; qb={qb_hits} xero={xr_hits}"


def test_trello_board_and_gmail_messages_both_read():
    trello_hits = _business_call_total(TRELLO_API_URL)
    gmail_hits = _business_call_total(GMAIL_API_URL)
    assert trello_hits > 0 and gmail_hits > 0, \
        f"restoration cross-walk incomplete; trello={trello_hits} gmail={gmail_hits}"


def test_consignment_reconciled_across_xero_airtable_hubspot():
    xr_hits = _business_call_total(XERO_API_URL)
    at_hits = _business_call_total(AIRTABLE_API_URL)
    hs_hits = _business_call_total(HUBSPOT_API_URL)
    assert xr_hits > 0 and at_hits > 0 and hs_hits > 0, \
        f"consignment three-way walk missing a source; xero={xr_hits} airtable={at_hits} hubspot={hs_hits}"


def test_calendar_and_monday_route_planning_both_touched():
    cal_hits = _business_call_total(GOOGLE_CALENDAR_API_URL)
    md_hits = _business_call_total(MONDAY_API_URL)
    assert cal_hits > 0 and md_hits > 0, \
        f"Modernism Week planning cross-walk incomplete; calendar={cal_hits} monday={md_hits}"


def test_provenance_walk_crosses_notion_and_gmail():
    nt_hits = _business_call_total(NOTION_API_URL)
    gm_hits = _business_call_total(GMAIL_API_URL)
    assert nt_hits > 0 and gm_hits > 0, \
        f"provenance walk incomplete; notion={nt_hits} gmail={gm_hits}"


# ==============================================================================
# Distractor bucket (single test, negative weight, references every distractor URL)
# ==============================================================================


def test_distractor_apis_untouched_business_endpoints():
    distractors = {
        "INSTAGRAM_API_URL": INSTAGRAM_API_URL,
        "TWITTER_API_URL": TWITTER_API_URL,
        "PINTEREST_API_URL": PINTEREST_API_URL,
        "REDDIT_API_URL": REDDIT_API_URL,
        "LINKEDIN_API_URL": LINKEDIN_API_URL,
        "YOUTUBE_API_URL": YOUTUBE_API_URL,
        "SPOTIFY_API_URL": SPOTIFY_API_URL,
        "NASA_API_URL": NASA_API_URL,
        "TMDB_API_URL": TMDB_API_URL,
        "ZILLOW_API_URL": ZILLOW_API_URL,
    }
    touched = []
    for name, url in distractors.items():
        try:
            calls = _business_call_total(url)
        except Exception:
            continue
        if calls > 0:
            touched.append(name)
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"


# ==============================================================================
# Mutation detection (Convention B — passes on undesired mutation, negative weight applied)
# ==============================================================================


def test_gmail_send_activity_detected():
    endpoints = _summary_endpoints(GMAIL_API_URL)
    send_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not klow.startswith("post "):
            continue
        if ("send" in klow) or ("messages" in klow and "draft" not in klow):
            count = meta.get("count", 0)
            if isinstance(count, int):
                send_calls += count
    assert send_calls > 0, "gmail live send activity flagged"


def test_docusign_envelope_dispatched_detected():
    endpoints = _summary_endpoints(DOCUSIGN_API_URL)
    write_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not (klow.startswith("post ") or klow.startswith("put ") or klow.startswith("patch ")):
            continue
        if ("envelope" in klow) or ("recipient" in klow):
            count = meta.get("count", 0)
            if isinstance(count, int):
                write_calls += count
    assert write_calls > 0, "docusign envelope dispatch flagged"


def test_webflow_publish_activity_detected():
    endpoints = _summary_endpoints(WEBFLOW_API_URL)
    write_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not (klow.startswith("post ") or klow.startswith("put ") or klow.startswith("patch ")):
            continue
        if ("publish" in klow) or ("live" in klow) or ("site" in klow and "publish" in klow):
            count = meta.get("count", 0)
            if isinstance(count, int):
                write_calls += count
    assert write_calls > 0, "webflow publish activity flagged"


def test_stripe_subscription_charge_forced_detected():
    endpoints = _summary_endpoints(STRIPE_API_URL)
    write_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not klow.startswith("post "):
            continue
        if ("subscription" in klow) or ("charge" in klow) or ("payment_intent" in klow) or ("invoice" in klow):
            count = meta.get("count", 0)
            if isinstance(count, int):
                write_calls += count
    assert write_calls > 0, "stripe subscription force-charge flagged"


def test_airtable_permanent_delete_detected():
    endpoints = _summary_endpoints(AIRTABLE_API_URL)
    delete_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not klow.startswith("delete "):
            continue
        count = meta.get("count", 0)
        if isinstance(count, int):
            delete_calls += count
    assert delete_calls > 0, "airtable permanent delete flagged"


def test_hubspot_new_contact_added_without_confirm_detected():
    endpoints = _summary_endpoints(HUBSPOT_API_URL)
    write_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not klow.startswith("post "):
            continue
        if ("contact" in klow) or ("company" in klow):
            count = meta.get("count", 0)
            if isinstance(count, int):
                write_calls += count
    assert write_calls > 0, "hubspot new-contact add flagged"


def test_notion_provenance_write_detected():
    endpoints = _summary_endpoints(NOTION_API_URL)
    write_calls = 0
    for key, meta in endpoints.items():
        if not isinstance(key, str) or not isinstance(meta, dict):
            continue
        klow = key.lower()
        if not (klow.startswith("post ") or klow.startswith("patch ") or klow.startswith("put ") or klow.startswith("delete ")):
            continue
        if ("page" in klow) or ("block" in klow) or ("database" in klow):
            count = meta.get("count", 0)
            if isinstance(count, int):
                write_calls += count
    assert write_calls > 0, "notion provenance mutation flagged"
