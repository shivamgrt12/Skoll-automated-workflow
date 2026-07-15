import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
MIXPANEL_API_URL = os.environ.get("MIXPANEL_API_URL", "http://localhost:8056")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
ZENDESK_API_URL = os.environ.get("ZENDESK_API_URL", "http://localhost:8025")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8072")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8030")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
AMPLITUDE_API_URL = os.environ.get("AMPLITUDE_API_URL", "http://localhost:8091")
SERVICENOW_API_URL = os.environ.get("SERVICENOW_API_URL", "http://localhost:8071")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8075")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")


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


def _business_calls(base_url):
    try:
        summary = _get(f"{base_url}/audit/summary")
    except Exception:
        return 0
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    total = 0
    for key, info in endpoints.items():
        path = key.split(" ", 1)[1] if " " in key else key
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        if isinstance(info, dict):
            total += info.get("count", 0)
    return total


def test_grant_and_roster_surfaces_queried():
    """Cost-per-student needs both the stipend payroll and the program roster; confirms both were queried."""
    stipends = _business_calls(GUSTO_API_URL)
    roster = _business_calls(GOOGLE_CLASSROOM_API_URL)
    assert stipends > 0 and roster > 0, f"gusto={stipends} classroom={roster}"


def test_asana_cip_tracker_read():
    """Confirms the campus improvement plan tracker was queried for the goal audit."""
    assert _business_calls(ASANA_API_URL) > 0


def test_eventbrite_attendance_read():
    """Confirms the ticketed family-engagement check-in records were queried."""
    assert _business_calls(EVENTBRITE_API_URL) > 0


def test_hubspot_sponsor_pipeline_read():
    """Confirms the community-sponsor pipeline was queried for pledged versus paid."""
    assert _business_calls(HUBSPOT_API_URL) > 0


def test_zendesk_it_tickets_read():
    """Confirms the classroom-hardware help tickets were queried for blocking status."""
    assert _business_calls(ZENDESK_API_URL) > 0


def test_mixpanel_signup_funnel_read():
    """Confirms the program sign-up funnel was queried for the registration-to-attendance drop."""
    assert _business_calls(MIXPANEL_API_URL) > 0


def test_airtable_family_events_read():
    """Confirms the family-engagement event roster was queried for logged attendance."""
    assert _business_calls(AIRTABLE_API_URL) > 0


def test_distractor_apis_touched():
    """Distractor services outside the mid-year submission scope received business calls."""
    candidates = [
        ("trello-api", TRELLO_API_URL),
        ("quickbooks-api", QUICKBOOKS_API_URL),
        ("salesforce-api", SALESFORCE_API_URL),
        ("amplitude-api", AMPLITUDE_API_URL),
        ("servicenow-api", SERVICENOW_API_URL),
        ("ticketmaster-api", TICKETMASTER_API_URL),
        ("notion-api", NOTION_API_URL),
        ("paypal-api", PAYPAL_API_URL),
        ("mailchimp-api", MAILCHIMP_API_URL),
    ]
    touched = [name for name, url in candidates if _business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
