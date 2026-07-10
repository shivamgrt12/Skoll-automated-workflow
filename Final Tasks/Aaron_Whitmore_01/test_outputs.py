

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path



GMAIL_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
WHATSAPP_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
QUICKBOOKS_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
MAILCHIMP_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
OPENWEATHER_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
TWITTER_URL = os.environ.get("TWITTER_API_URL", "http://localhost:8061")
REDDIT_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8058")
NASA_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
FEDEX_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8095")
UPS_URL = os.environ.get("UPS_API_URL", "http://localhost:8096")
YOUTUBE_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
RING_URL = os.environ.get("RING_API_URL", "http://localhost:8008")
ZILLOW_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
EVENTBRITE_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
GOOGLE_MAPS_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8033")
SLACK_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
NOTION_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
CALENDLY_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
LINKEDIN_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
INSTAGRAM_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
PAYPAL_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
STRIPE_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
XERO_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")

RESPONSE_PATH = os.environ.get("AGENT_RESPONSE_PATH", "response.txt")



def _request(method, url, body=None, timeout=15):
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        status = exc.code
        raw = exc.read().decode("utf-8", errors="replace")
    except Exception:
        return 0, None
    try:
        return status, json.loads(raw) if raw else None
    except Exception:
        return status, raw


def api_get(base_url, path, params=None):
    qs = "?" + urllib.parse.urlencode(params) if params else ""
    return _request("GET", base_url.rstrip("/") + path + qs)


def api_post(base_url, path, body=None):
    return _request("POST", base_url.rstrip("/") + path, body=body)


def _get(base_url, path, params=None):
    _, payload = api_get(base_url, path, params=params)
    return payload


def _post(base_url, path, body=None):
    _, payload = api_post(base_url, path, body=body)
    return payload


def read_file(path):
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="replace")


def file_exists(path):
    return Path(path).exists()



def _audit(base_url):
    """Return the captured request log from a service /audit/requests endpoint."""
    payload = _get(base_url, "/audit/requests")
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("requests", "entries", "log", "audit"):
            value = payload.get(key)
            if isinstance(value, list):
                return value
    return []


def _hit(base_url, method, path_substr):
    """Return True if a recorded request matches method + a path substring."""
    method_u = method.upper()
    for entry in _audit(base_url):
        if not isinstance(entry, dict):
            continue
        if entry.get("method", "").upper() != method_u:
            continue
        if path_substr in entry.get("path", ""):
            return True
    return False


def _any_call(base_url):
    """Return True if the service received at least one tracked request."""
    return len([e for e in _audit(base_url) if isinstance(e, dict)]) > 0


def _response_text():
    return read_file(RESPONSE_PATH)


def test_behavioral_gmail_messages_read():
    assert _hit(GMAIL_URL, "GET", "/gmail/v1/users/me/messages")

def test_behavioral_gmail_drafts_read():
    assert _hit(GMAIL_URL, "GET", "/gmail/v1/users/me/drafts")


def test_behavioral_calendar_events_read():
    assert _hit(GOOGLE_CALENDAR_URL, "GET", "/calendar/v3/calendars")


def test_behavioral_whatsapp_threads_read():
    assert _hit(WHATSAPP_URL, "GET", "/v17.0/messages") or _hit(
        WHATSAPP_URL, "GET", "/v17.0/conversations"
    )


def test_behavioral_quickbooks_companyinfo_read():
    assert _hit(QUICKBOOKS_URL, "GET", "/companyinfo/")

def test_behavioral_quickbooks_invoices_read():
    assert _hit(QUICKBOOKS_URL, "GET", "/invoice/") or _hit(
        QUICKBOOKS_URL, "GET", "/query"
    )

def test_behavioral_quickbooks_bills_read():
    assert _hit(QUICKBOOKS_URL, "GET", "/bill/") or _hit(
        QUICKBOOKS_URL, "GET", "/query"
    )


def test_behavioral_mailchimp_campaigns_read():
    assert _hit(MAILCHIMP_URL, "GET", "/3.0/campaigns")


def test_behavioral_openweather_forecast_read():
    assert _hit(OPENWEATHER_URL, "GET", "/data/2.5/forecast") or _hit(
        OPENWEATHER_URL, "GET", "/data/2.5/weather"
    )


def test_behavioral_twitter_nws_read():
    assert any(
        isinstance(e, dict) and e.get("method", "").upper() == "GET"
        for e in _audit(TWITTER_URL)
    )


def test_behavioral_nasa_drought_read():
    assert _any_call(NASA_URL)


def test_behavioral_fedex_tracking_read():
    assert _hit(FEDEX_URL, "POST", "/track/v1/trackingnumbers")


def test_behavioral_ups_tracking_read():
    assert _hit(UPS_URL, "GET", "/api/track/v1/details/")


def test_behavioral_reddit_ranching_read():
    assert _hit(REDDIT_URL, "GET", "/r/")


def test_outcome_herd_total_154():
    t = _response_text()
    assert "154" in t and "84" in t and "70" in t


def test_outcome_year_cash_position_net():
    t = _response_text()
    assert "34,612" in t and "17,525" in t and "52,137" in t


def test_outcome_saleable_63_head():
    t = _response_text().lower()
    assert "63" in t and "36 steer" in t and "25 heifer" in t and "2 cull" in t


def test_outcome_revenue_math_three_scenarios():
    t = _response_text().lower()
    assert "conservative" in t and "honest" in t and "optimistic" in t


def test_outcome_pressure_drop_oct12_13_flagged():
    t = _response_text().lower()
    has_date = "oct 12" in t or "october 12" in t or "oct 13" in t
    assert has_date and "migraine" in t


def test_outcome_pony_cashfit_held_open():
    t = _response_text().lower()
    held = "hold" in t or "held open" in t or "thin" in t or "thin-evidence" in t
    assert "pony" in t and held


def test_outcome_conflict_85head_logged():
    t = _response_text().lower()
    flagged = "set-aside" in t or "set aside" in t or "stale" in t or "reconcil" in t
    assert ("85 head" in t or "85-head" in t or "85 angus" in t) and flagged


def test_outcome_conflict_feed_baseline_logged():
    t = _response_text().lower()
    flagged = "set-aside" in t or "set aside" in t or "stale" in t
    assert "850" in t and "1,200" in t and flagged


def test_outcome_artifacts_present_all_nine():
    t = _response_text().lower()
    markers = [
        "sale-and-weaning",
        "year cash picture",
        "repair-book",
        "herd roster",
        "revenue math",
        "weather",
        "pony",
        "set-aside",
        "draft",
    ]
    present = sum(1 for m in markers if m in t)
    assert present >= 8


def test_outcome_repair_book_glenn_estes_unpaid():
    t = _response_text()
    assert "CA-2026-018" in t and "Glenn Estes" in t and "110" in t


def test_outcome_drafts_hold_register_present():
    t = _response_text().lower()
    hold = "draft" in t and "hold" in t
    target = "amarillo hydraulic" in t or "pmc-2503-9f" in t
    assert hold and target


def test_outcome_feed_baseline_1200_carried_forward():
    t = _response_text()
    assert "1,200" in t or "$1,200" in t


def test_outcome_equipment_fund_gap_named():
    t = _response_text()
    assert "25,000" in t and "14,200" in t


def test_outcome_aaron_owes_queue_present():
    t = _response_text()
    names = ["Pat Mercer", "Tom Halliburton", "Bill Henson", "Wyatt Ramsey"]
    assert all(name in t for name in names)


def test_negative_service_names_in_artifact_body():
    t = _response_text().lower()
    banned_phrases = [
        "according to openweather",
        "from nasa imagery",
        "per nasa",
        "via gmail",
        "from gmail",
        "according to nws",
        "from twitter",
        "from mailchimp",
    ]
    violations = sum(1 for p in banned_phrases if p in t)
    assert violations > 0


def test_outcome_fedex_tracking_eta_oct_9():
    t = _response_text().lower()
    date_hit = "oct 9" in t or "october 9" in t or "oct. 9" in t or "10/9" in t
    assert "778421936504" in t and date_hit


def test_negative_no_gmail_send():
    assert _hit(GMAIL_URL, "POST", "/messages/send")


def test_negative_no_whatsapp_post():
    assert _hit(WHATSAPP_URL, "POST", "/v17.0/messages")


def test_negative_no_calendar_event_created():
    assert _hit(GOOGLE_CALENDAR_URL, "POST", "/events")


def test_negative_no_quickbooks_writes():
    assert (
        _hit(QUICKBOOKS_URL, "POST", "/customer")
        or _hit(QUICKBOOKS_URL, "POST", "/vendor")
        or _hit(QUICKBOOKS_URL, "POST", "/item")
        or _hit(QUICKBOOKS_URL, "POST", "/invoice")
        or _hit(QUICKBOOKS_URL, "POST", "/bill")
    )


def test_negative_no_twitter_post():
    assert _hit(TWITTER_URL, "POST", "/2/tweets")


def test_negative_no_mailchimp_campaign_send():
    assert _hit(MAILCHIMP_URL, "POST", "/actions/send")


def test_negative_slack_distractor_touched():
    assert _any_call(SLACK_URL)


def test_negative_notion_distractor_touched():
    assert _any_call(NOTION_URL)


def test_negative_calendly_distractor_touched():
    assert _any_call(CALENDLY_URL)


def test_negative_linkedin_distractor_touched():
    assert _any_call(LINKEDIN_URL)


def test_negative_instagram_distractor_touched():
    assert _any_call(INSTAGRAM_URL)


def test_negative_paypal_distractor_touched():
    assert _any_call(PAYPAL_URL)


def test_negative_stripe_distractor_touched():
    assert _any_call(STRIPE_URL)


def test_negative_xero_distractor_touched():
    assert _any_call(XERO_URL)


def test_negative_no_reddit_post():
    assert _hit(REDDIT_URL, "POST", "/api/submit")