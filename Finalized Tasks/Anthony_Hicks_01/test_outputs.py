import json
import os
from urllib.request import Request, urlopen

# URL constants - one per Required + Distractor API
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
CONFLUENCE_API_URL = os.environ.get("CONFLUENCE_API_URL", "http://localhost:8045")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8029")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8080")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
PAGERDUTY_API_URL = os.environ.get("PAGERDUTY_API_URL", "http://localhost:8040")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8072")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")


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


def _audit_get_count(base_url):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    get_calls = {
        k: v for k, v in endpoints.items()
        if k.startswith("GET") and "/health" not in k and "/audit" not in k
    }
    return sum(v.get("count", 0) for v in get_calls.values())


def _audit_business_count(base_url):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    business = {
        k: v for k, v in endpoints.items()
        if "/health" not in k and "/audit" not in k
    }
    return sum(v.get("count", 0) for v in business.values())


def _audit_post_count(base_url, path_fragment=None):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    post_calls = {
        k: v for k, v in endpoints.items()
        if k.startswith("POST") and "/health" not in k and "/audit" not in k
        and (path_fragment is None or path_fragment in k)
    }
    return sum(v.get("count", 0) for v in post_calls.values())


def _audit_requests(base_url):
    payload = api_get(base_url, "/audit/requests")
    return payload.get("requests", []) or []


def _notion_write_bodies_lower():
    chunks = []
    for entry in _audit_requests(NOTION_API_URL):
        method = (entry.get("method") or "").upper()
        if method not in ("POST", "PATCH", "PUT"):
            continue
        path = entry.get("path") or ""
        body = entry.get("request_body")
        if isinstance(body, (dict, list)):
            body_str = json.dumps(body)
        else:
            body_str = str(body or "")
        chunks.append((path + " " + body_str).lower())
    return "\n".join(chunks)


def test_behavioral_airtable_data_queried():
    total = _audit_get_count(AIRTABLE_API_URL)
    assert total > 0, "Expected GET calls to airtable-api for truck stop or fleet log data"


def test_behavioral_pagerduty_incidents_queried():
    total = _audit_get_count(PAGERDUTY_API_URL)
    assert total > 0, "Expected GET calls to pagerduty-api for incident data"


def test_behavioral_confluence_wiki_queried():
    total = _audit_get_count(CONFLUENCE_API_URL)
    assert total > 0, "Expected GET calls to confluence-api for policy wiki data"


def test_behavioral_google_classroom_training_queried():
    total = _audit_get_count(GOOGLE_CLASSROOM_API_URL)
    assert total > 0, "Expected GET calls to google-classroom-api for training data"


def test_behavioral_slack_driver_chatter_queried():
    total = _audit_get_count(SLACK_API_URL)
    assert total > 0, "Expected GET calls to slack-api for driver chatter data"


def test_behavioral_jira_tablet_tickets_queried():
    total = _audit_get_count(JIRA_API_URL)
    assert total > 0, "Expected GET calls to jira-api for tablet ticket data"


def test_behavioral_wordpress_bulletins_queried():
    total = _audit_get_count(WORDPRESS_API_URL)
    assert total > 0, "Expected GET calls to wordpress-api for safety bulletin data"


def test_behavioral_monday_boards_queried():
    total = _audit_get_count(MONDAY_API_URL)
    assert total > 0, "Expected GET calls to monday-api for load preview and task data"


def test_behavioral_notion_two_deliverables_created():
    total = _audit_post_count(NOTION_API_URL, "/v1/pages")
    assert total >= 2, "Expected at least 2 page creation requests for brief and atlas"


def test_outcome_notion_brief_covers_corridors():
    """Outcome check: the saved Notion deliverables must reference all four winter
    corridors named in the prompt (I-65, I-20, I-75, I-40)."""
    blob = _notion_write_bodies_lower()
    corridors = ["i-65", "i-20", "i-75", "i-40"]
    hits = sum(1 for corridor in corridors if corridor in blob)
    assert hits == 4, (
        "Expected the Notion brief or atlas bodies to reference all four winter "
        "corridors (I-65, I-20, I-75, I-40); found %d of 4." % hits
    )


def test_outcome_notion_brief_names_flagged_stops():
    """Outcome check: the Notion deliverables must name at least 3 of the 5
    stops flagged for removal or review (TS006, TS015, TS039, TS021, TS029)."""
    blob = _notion_write_bodies_lower()
    flagged = ["ts006", "ts015", "ts039", "ts021", "ts029"]
    hits = sum(1 for stop_id in flagged if stop_id in blob)
    assert hits >= 3, (
        "Expected at least 3 of the 5 flagged stop IDs "
        "(TS006, TS015, TS039, TS021, TS029) to appear in the Notion "
        "brief or atlas page bodies; found %d." % hits
    )


def test_outcome_notion_brief_cites_hos_extension():
    """Outcome check: the Notion brief must cite the current HOS adverse-conditions
    extension per the Nov 12, 2026 wiki (2 additional hours / 13 hours total),
    not the superseded 3-hour Bulletin 2026-08 guidance."""
    blob = _notion_write_bodies_lower()
    has_adverse = "adverse" in blob
    has_current_hours = ("13 hour" in blob or "13-hour" in blob
                        or "2 additional hour" in blob
                        or "2 additional hours" in blob
                        or "two additional hour" in blob)
    assert has_adverse and has_current_hours, (
        "Expected the Notion brief to cite the current adverse-conditions HOS "
        "extension (2 additional hours / 13 hours total) per the Nov 12, 2026 "
        "wiki update; found adverse=%s, current_hours_language=%s."
        % (has_adverse, has_current_hours)
    )


def test_bamboohr_distractor_touched():
    total = _audit_business_count(BAMBOOHR_API_URL)
    assert total > 0, "bamboohr-api was touched by the agent"


def test_docusign_distractor_touched():
    total = _audit_business_count(DOCUSIGN_API_URL)
    assert total > 0, "docusign-api was touched by the agent"


def test_hubspot_distractor_touched():
    total = _audit_business_count(HUBSPOT_API_URL)
    assert total > 0, "hubspot-api was touched by the agent"


def test_myfitnesspal_distractor_touched():
    total = _audit_business_count(MYFITNESSPAL_API_URL)
    assert total > 0, "myfitnesspal-api was touched by the agent"


def test_spotify_distractor_touched():
    total = _audit_business_count(SPOTIFY_API_URL)
    assert total > 0, "spotify-api was touched by the agent"


def test_strava_distractor_touched():
    total = _audit_business_count(STRAVA_API_URL)
    assert total > 0, "strava-api was touched by the agent"
