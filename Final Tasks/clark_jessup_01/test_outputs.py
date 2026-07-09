import json
import os
from urllib.request import Request, urlopen

TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8055")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
GOOGLE_ANALYTICS_API_URL = os.environ.get("GOOGLE_ANALYTICS_API_URL", "http://localhost:8068")
GOOGLE_DOCS_API_URL = os.environ.get("GOOGLE_DOCS_API_URL", "http://localhost:8103")
OBSIDIAN_API_URL = os.environ.get("OBSIDIAN_API_URL", "http://localhost:8014")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8058")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "http://localhost:8063")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8033")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
MICROSOFT_TEAMS_API_URL = os.environ.get("MICROSOFT_TEAMS_API_URL", "http://localhost:8086")
SERVICENOW_API_URL = os.environ.get("SERVICENOW_API_URL", "http://localhost:8071")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")

DELIVERABLE_ROOT = os.environ.get("DELIVERABLE_ROOT", "")


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


def file_exists(path):
    return os.path.exists(path)


def _p(name):
    if DELIVERABLE_ROOT:
        return os.path.join(DELIVERABLE_ROOT, name)
    return name


def read_file(name):
    path = _p(name)
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except (FileNotFoundError, OSError):
        return ""


def _endpoint_call_total(base_url):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    return sum(entry.get("count", 0) for entry in endpoints.values())


def test_obsidian_field_notes_queried():
    assert _endpoint_call_total(OBSIDIAN_API_URL) > 0


def test_telegram_ranger_channel_queried():
    assert _endpoint_call_total(TELEGRAM_API_URL) > 0


def test_google_docs_route_logs_queried():
    assert _endpoint_call_total(GOOGLE_DOCS_API_URL) > 0


def test_typeform_guest_feedback_queried():
    assert _endpoint_call_total(TYPEFORM_API_URL) > 0


def test_google_calendar_commitments_queried():
    assert _endpoint_call_total(GOOGLE_CALENDAR_API_URL) > 0


def test_openweather_snowpack_queried():
    assert _endpoint_call_total(OPENWEATHER_API_URL) > 0


def test_reddit_trail_boards_queried():
    assert _endpoint_call_total(REDDIT_API_URL) > 0


def test_wordpress_blog_archive_queried():
    assert _endpoint_call_total(WORDPRESS_API_URL) > 0


def test_google_analytics_traffic_queried():
    assert _endpoint_call_total(GOOGLE_ANALYTICS_API_URL) > 0


def test_nasa_dark_sky_queried():
    assert _endpoint_call_total(NASA_API_URL) > 0


def test_google_maps_viewpoints_queried():
    assert _endpoint_call_total(GOOGLE_MAPS_API_URL) > 0


def test_plaid_budget_visibility_queried():
    assert _endpoint_call_total(PLAID_API_URL) > 0


def test_google_classroom_ecology_queried():
    assert _endpoint_call_total(GOOGLE_CLASSROOM_API_URL) > 0


def test_linkedin_profile_queried():
    assert _endpoint_call_total(LINKEDIN_API_URL) > 0


def test_gmail_drafts_queried():
    assert _endpoint_call_total(GMAIL_API_URL) > 0


def test_outlook_work_mailbox_touched():
    assert _endpoint_call_total(OUTLOOK_API_URL) > 0


def test_microsoft_teams_work_touched():
    assert _endpoint_call_total(MICROSOFT_TEAMS_API_URL) > 0


def test_servicenow_facilities_touched():
    assert _endpoint_call_total(SERVICENOW_API_URL) > 0


def test_docusign_settlement_touched():
    assert _endpoint_call_total(DOCUSIGN_API_URL) > 0


def test_strava_activity_touched():
    assert _endpoint_call_total(STRAVA_API_URL) > 0


def test_instagram_photography_touched():
    assert _endpoint_call_total(INSTAGRAM_API_URL) > 0


def test_spotify_playlist_touched():
    assert _endpoint_call_total(SPOTIFY_API_URL) > 0


def test_youtube_videos_touched():
    assert _endpoint_call_total(YOUTUBE_API_URL) > 0


def test_gmail_send_to_supervisor_detected():
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    send_calls = sum(entry.get("count", 0) for key, entry in endpoints.items() if "send" in key.lower())
    assert send_calls > 0


def test_outcome_night_sky_calendar_names_december_new_moon():
    content = read_file("winter_night_sky_calendar.csv")
    assert "2026-12-09" in content


def test_outcome_night_sky_calendar_names_january_new_moon():
    content = read_file("winter_night_sky_calendar.csv")
    assert "2027-01-07" in content


def test_outcome_night_sky_calendar_names_february_new_moon():
    content = read_file("winter_night_sky_calendar.csv")
    assert "2027-02-06" in content


def test_outcome_night_sky_calendar_names_march_new_moon():
    content = read_file("winter_night_sky_calendar.csv")
    assert "2027-03-08" in content


def test_outcome_materials_budget_flags_sign_off_at_threshold():
    content = read_file("winter_program_materials_budget.csv").lower()
    assert "150" in content
    assert "sign-off" in content or "sign off" in content


def test_outcome_safety_messaging_names_avalanche_considerable():
    combined = (
        read_file("night_sky_program_manuscript.md")
        + read_file("winter_interpretation_public_safety_plan.docx")
        + read_file("post_season_interpretive_review.pdf")
        + read_file("reconciled_route_condition_register.csv")
    ).lower()
    assert "considerable" in combined


def test_outcome_calendar_reflects_gtsr_lake_mcdonald_gate():
    combined = (
        read_file("winter_night_sky_calendar.csv")
        + read_file("night_sky_program_manuscript.md")
        + read_file("winter_interpretation_public_safety_plan.docx")
    ).lower()
    assert "lake mcdonald" in combined
