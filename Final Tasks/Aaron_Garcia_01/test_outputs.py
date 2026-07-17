import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8047")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8036")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8046")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
GREENHOUSE_API_URL = os.environ.get("GREENHOUSE_API_URL", "http://localhost:8090")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8021")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8082")

AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8081")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8076")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8074")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
OBSIDIAN_API_URL = os.environ.get("OBSIDIAN_API_URL", "http://localhost:8080")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8025")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8078")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8020")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8075")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8059")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    try:
        with urlopen(req, timeout=8) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return {}


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


def _audit_endpoints(base_url):
    data = api_get(base_url, "/audit/summary")
    if isinstance(data, dict):
        return data.get("endpoints", data)
    return {}


def _business_calls(base_url):
    total = 0
    endpoints = _audit_endpoints(base_url)
    if isinstance(endpoints, dict):
        for key, val in endpoints.items():
            if isinstance(key, str) and (key.startswith("/audit") or "/health" in key):
                continue
            if isinstance(val, dict):
                total += val.get("count", 0)
            elif isinstance(val, int):
                total += val
    return total


def _distinct_endpoints(base_url):
    endpoints = _audit_endpoints(base_url)
    if not isinstance(endpoints, dict):
        return 0
    return sum(
        1
        for k in endpoints.keys()
        if isinstance(k, str) and not k.startswith("/audit") and "/health" not in k
    )


def _output_dir():
    return os.environ.get("AGENT_OUTPUT_DIR", "/workspace")


def _all_output_files():
    base = _output_dir()
    if not os.path.isdir(base):
        return []
    return [
        os.path.join(base, f)
        for f in os.listdir(base)
        if os.path.isfile(os.path.join(base, f))
    ]


def _read_all_output_files():
    combined = ""
    for path in _all_output_files():
        try:
            combined += read_file(path) + "\n"
        except Exception:
            pass
    return combined


def _content():
    return _read_all_output_files().lower()


def _has_amount(content, *variants):
    return any(v in content for v in variants)


def _has_all(content, *tokens):
    return all(t in content for t in tokens)


def test_deliverables_written():
    files = _all_output_files()
    substantive = {os.path.basename(f).lower() for f in files if os.path.getsize(f) > 500}
    assert len(substantive) >= 4


def test_airtable_shift_board_read():
    assert _business_calls(AIRTABLE_API_URL) >= 12 and _distinct_endpoints(AIRTABLE_API_URL) >= 4


def test_gusto_payroll_read():
    assert _business_calls(GUSTO_API_URL) >= 10 and _distinct_endpoints(GUSTO_API_URL) >= 4


def test_quickbooks_restaurant_books_read():
    assert _business_calls(QUICKBOOKS_API_URL) >= 15 and _distinct_endpoints(QUICKBOOKS_API_URL) >= 6


def test_xero_rental_book_read():
    assert _business_calls(XERO_API_URL) >= 12 and _distinct_endpoints(XERO_API_URL) >= 5


def test_bamboohr_roster_read():
    assert _business_calls(BAMBOOHR_API_URL) >= 8 and _distinct_endpoints(BAMBOOHR_API_URL) >= 3


def test_google_calendar_tax_cadence_read():
    assert _business_calls(GOOGLE_CALENDAR_API_URL) >= 8


def test_notion_deal_box_read():
    assert _business_calls(NOTION_API_URL) >= 10 and _distinct_endpoints(NOTION_API_URL) >= 4


def test_greenhouse_open_reqs_read():
    assert _business_calls(GREENHOUSE_API_URL) >= 8 and _distinct_endpoints(GREENHOUSE_API_URL) >= 3


def test_zillow_market_comps_read():
    assert _business_calls(ZILLOW_API_URL) >= 10 and _distinct_endpoints(ZILLOW_API_URL) >= 4


def test_docusign_owner_package_staged():
    assert _business_calls(DOCUSIGN_API_URL) >= 6 and _distinct_endpoints(DOCUSIGN_API_URL) >= 3


def test_ninety_day_horizon_named():
    content = _content()
    horizon = "ninety-day" in content or "ninety day" in content
    assert horizon and "mid-january" in content and ("post-close" in content or "post close" in content)


def test_both_locations_covered():
    content = _content()
    assert (
        "alt 19" in content
        and "original location" in content
        and "721 dodecanese" in content
        and "mykonos taverna ii" in content
    )


def test_three_staffing_scenarios_named():
    content = _content()
    market = "hire two at market rate" in content
    temp = ("hire one" in content) and ("temp coverage" in content)
    absorb = ("absorb with existing crew" in content) and ("pay overtime" in content or "pay the overtime" in content)
    assert market and temp and absorb


def test_thirty_five_percent_labor_target():
    content = _content()
    target = "35%" in content or "thirty-five percent" in content
    assert (
        target
        and "labor" in content
        and "week by week" in content
        and "revenue" in content
        and "alt 19" in content
        and "original location" in content
    )


def test_property3_insurance_reserved():
    content = _content()
    assert (
        "citizens property" in content
        and ("$2,680" in content or "2,680" in content)
        and ("duplex" in content or "property 3" in content or "p3" in content)
        and ("uplift" in content or "carrier-flagged" in content)
        and "reserve" in content
    )


def test_alt19_oven_balance_44850():
    content = _content()
    assert (
        ("44,850" in content or "$44,850" in content)
        and "bakers pride" in content
        and "ascend equipment finance" in content
        and ("1,362.16" in content or "$1,362.16" in content)
    )


def test_wedding_fund_pace_maintained():
    content = _content()
    assert (
        ("$19,500" in content or "19,500" in content)
        and ("$1,000/mo" in content or "$1,000 per month" in content or "$1,000/month" in content)
        and "sophia" in content
        and ("$30,000" in content or "30,000" in content or "$30k" in content)
        and "ally" in content
    )


def test_low_water_mark_weeks_labeled():
    content = _content()
    has_phrase = "low-water-mark" in content or "low water mark" in content
    has_date = "january 15" in content or "jan 15" in content
    has_dollar = "$" in content
    assert has_phrase and has_date and has_dollar and "week" in content


def test_three_rental_lines_separated():
    content = _content()
    tenants = _has_all(content, "johnson", "williams", "davis", "chen")
    rents = _has_all(content, "1,600", "2,000", "1,350", "1,400")
    assert tenants and rents and "mortgage" in content and "net" in content


def test_1031_candidate_analysis():
    content = _content()
    comped = "sold comps" in content or "recent sold" in content or "closing comps" in content
    figures = ("272" in content) and ("258" in content)
    assert "1031" in content and "palm harbor" in content and comped and figures


def test_market_comps_referenced():
    content = _content()
    context = "tarpon" in content and ("fourplex" in content or "4-unit" in content)
    quarter = "q4 2026" in content or "fourth quarter 2026" in content
    assert context and quarter and "cap rate" in content


def test_three_timing_windows():
    content = _content()
    now = "next ninety days" in content or "within the next ninety days" in content
    spring = "after tax season" in content and ("april" in content or "may" in content)
    autumn = "next autumn" in content or "fall 2027" in content
    assert now and spring and autumn and "decision matrix" in content


def test_deal_box_criteria_stated():
    content = _content()
    ceiling = ("$525" in content or "525k" in content) and ("$560" in content or "560k" in content)
    cap = "6.5%" in content and "cap rate" in content
    dscr = ("dscr" in content or "debt coverage" in content) and "1.25" in content
    ltv = "60%" in content and "ltv" in content
    assert ceiling and cap and dscr and ltv


def test_eleni_summary_delivered():
    content = _content()
    assert (
        "eleni" in content
        and ("one-page" in content or "one page" in content)
        and "bookkeeping window" in content
        and "owner summary" in content
    )


def test_payroll_hours_mismatch_by_name():
    content = _content()
    classification = ("data-entry" in content or "data entry" in content) and ("raise with" in content or "direct conversation" in content)
    named = ("maria kostopoulos" in content or "andreas garcia" in content) and "hours mismatch" in content
    assert classification and named


def test_docusign_three_envelopes_named():
    content = _content()
    assert (
        "eleni garcia" in content
        and "andreas garcia" in content
        and "maria kostopoulos" in content
        and "docusign" in content
        and "envelope" in content
    )


def test_dragging_property_named():
    content = _content()
    assert "dragging" in content and ("duplex" in content or "property 3" in content) and ("365" in content or "$365" in content)


def test_source_attribution_gusto_airtable():
    content = _content()
    assert (
        "gusto" in content
        and "airtable" in content
        and ("per gusto" in content or "gusto shows" in content or "source: gusto" in content)
        and ("per airtable" in content or "airtable shows" in content or "source: airtable" in content)
    )


def test_pascha_and_wedding_calendar():
    content = _content()
    assert (
        "pascha" in content
        and "wedding" in content
        and "april" in content
        and "sophia" in content
    )


def test_fasting_week_tip_pool():
    content = _content()
    assert (
        ("great lent" in content or "advent" in content or "fasting week" in content)
        and "tip" in content
        and ("front-of-house" in content or "foh" in content)
        and ("kitchen load" in content or "menu shift" in content)
    )


def test_george_hatzis_sundays_named():
    content = _content()
    assert (
        "george hatzis" in content
        and "sunday" in content
        and ("church" in content or "no sunday" in content or "does not work sundays" in content)
    )


def test_andreas_no_float_rule_named():
    content = _content()
    assert (
        "andreas" in content
        and ("no float" in content or "will not float" in content or "hold off float" in content)
        and ("live conversation" in content or "conversation from aaron" in content)
    )


def test_distractor_apis_touched():
    distractors = [
        ("amadeus-api", AMADEUS_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("google-maps-api", GOOGLE_MAPS_API_URL),
        ("myfitnesspal-api", MYFITNESSPAL_API_URL),
        ("nasa-api", NASA_API_URL),
        ("obsidian-api", OBSIDIAN_API_URL),
        ("openweather-api", OPENWEATHER_API_URL),
        ("ring-api", RING_API_URL),
        ("spotify-api", SPOTIFY_API_URL),
        ("strava-api", STRAVA_API_URL),
        ("tmdb-api", TMDB_API_URL),
        ("whatsapp-api", WHATSAPP_API_URL),
    ]
    touched = [name for name, url in distractors if _business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
