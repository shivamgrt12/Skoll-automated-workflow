import json
import os
from urllib.request import Request, urlopen


GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8030")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8033")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8038")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
CONFLUENCE_API_URL = os.environ.get("CONFLUENCE_API_URL", "http://localhost:8045")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8028")

SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8012")
DOORDASH_API_URL = os.environ.get("DOORDASH_API_URL", "http://localhost:8037")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8034")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
TWITTER_API_URL = os.environ.get("TWITTER_API_URL", "http://localhost:8061")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
OPENLIBRARY_API_URL = os.environ.get("OPENLIBRARY_API_URL", "http://localhost:8078")
GOOGLE_CLASSROOM_API_URL = os.environ.get("GOOGLE_CLASSROOM_API_URL", "http://localhost:8002")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    with urlopen(req, timeout=10) as resp:
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


def _endpoint_hits(endpoint_entry):
    if isinstance(endpoint_entry, dict):
        return endpoint_entry.get("count", 0)
    if isinstance(endpoint_entry, int):
        return endpoint_entry
    return 0


def test_gmail_dfg_liaison_thread_pulled():
    """Confirms the agent pulled the DFG liaison, museum, Whitfield, or freelancer correspondence via Gmail messages, threads, or drafts."""
    summary = api_get(GMAIL_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/messages" in k or "/threads" in k or "/drafts" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_outlook_museum_thread_pulled():
    """Confirms the agent pulled the Hamburg Maritime Museum consortium and Whitfield Exchange correspondence via Outlook messages or events."""
    summary = api_get(OUTLOOK_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/messages" in k or "/events" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_google_calendar_deadline_window_pulled():
    """Confirms the agent pulled the DFG submission window, the consortium meeting slot, or the liaison review slot via Google Calendar events or calendar list."""
    summary = api_get(GOOGLE_CALENDAR_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/events" in k or "/calendarList" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_notion_project_hub_pulled():
    """Confirms the agent pulled the master project hub, permit tracker, or field logistics via Notion pages, databases, blocks, or search."""
    summary = api_get(NOTION_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/pages" in k or "/databases" in k or "/blocks" in k or "/search" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_airtable_nf7_catalog_pulled():
    """Confirms the agent pulled the Site NF-7 artifact catalog base or the Coastal Heritage base via Airtable record or metadata endpoints."""
    summary = api_get(AIRTABLE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/v0/" in k or "/bases" in k or "/tables" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_asana_dfg_deliverables_pulled():
    """Confirms the agent pulled the DFG Phase 3 Reporting and EU Horizon deliverable trackers via Asana projects or tasks."""
    summary = api_get(ASANA_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/projects" in k or "/tasks" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_trello_phase4_board_pulled():
    """Confirms the agent pulled the NF-7 Phase 4 Fieldwork Planning board via Trello boards, lists, or cards."""
    summary = api_get(TRELLO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/boards" in k or "/lists" in k or "/cards" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_quickbooks_dfg_ledger_pulled():
    """Confirms the agent pulled the DFG Grant Operating Account and Fieldwork Direct Costs entries via QuickBooks accounts, invoices, purchases, bills, reports, or query endpoints."""
    summary = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/account" in k or "/invoice" in k or "/purchase" in k or "/reports" in k or "/bill" in k or "/query" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_xero_diver_day_subcontract_pulled():
    """Confirms the agent pulled the Johansen Dive Support diver-day subcontract line via Xero invoices, contacts, or accounts."""
    summary = api_get(XERO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/Invoices" in k or "/Contacts" in k or "/Accounts" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_gusto_freelancer_retainers_pulled():
    """Confirms the agent pulled the Cohen Remote Sensing and Park Reconstruction Illustration monthly retainer schedules via Gusto contractors, payrolls, employees, or companies endpoints."""
    summary = api_get(GUSTO_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/contractors" in k or "/payrolls" in k or "/employees" in k or "/companies" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_openweather_husum_window_pulled():
    """Confirms the agent pulled the North Frisian coast historical dive window via OpenWeather weather, forecast, or geocoding endpoints."""
    summary = api_get(OPENWEATHER_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/weather" in k or "/forecast" in k or "/direct" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_google_maps_husum_routing_pulled():
    """Confirms the agent pulled the Husum staging routing via Google Maps place, geocode, directions, or distance-matrix endpoints."""
    summary = api_get(GOOGLE_MAPS_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/place" in k or "/geocode" in k or "/directions" in k or "/distancematrix" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_airbnb_husum_shortlist_pulled():
    """Confirms the agent pulled the Husum base-camp lodging shortlist via Airbnb listings or reservation endpoints."""
    summary = api_get(AIRBNB_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/listings" in k or "/reservations" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_docusign_permit_and_charter_pulled():
    """Confirms the agent pulled the excavation permit application, the Nordkai vessel charter envelope, or the freelancer renewal via DocuSign envelopes or templates."""
    summary = api_get(DOCUSIGN_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/envelopes" in k or "/templates" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_confluence_museum_notes_pulled():
    """Confirms the agent pulled the museum-side conservation notes or the consortium documentation space via Confluence non-audit endpoints."""
    summary = api_get(CONFLUENCE_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        parts = k.split(" ", 1)
        route = parts[1] if len(parts) == 2 else k
        if route.startswith("/audit") or route.startswith("/health") or route.startswith("/admin"):
            continue
        hits += _endpoint_hits(v)
    assert hits > 0


def test_zoom_liaison_review_pulled():
    """Confirms the agent pulled the DFG liaison video review meeting slot via Zoom meetings, users, or recordings endpoints."""
    summary = api_get(ZOOM_API_URL, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    hits = 0
    for k, v in endpoints.items():
        if "/meetings" in k or "/users" in k or "/recordings" in k or "/registrants" in k:
            hits += _endpoint_hits(v)
    assert hits > 0


def test_distractor_apis_touched():
    """Negative test: passes when the forbidden behavior is detected; its negative weight contributes as a penalty. Fires if the agent touched any distractor service outside the DFG Phase 3 report and Phase 4 planning packet scope, covering spotify, youtube, instacart, doordash, yelp, strava, coinbase, plaid, wordpress, twitter, instagram, nasa, openlibrary, google-classroom, or eventbrite."""
    distractors = [
        ("spotify-api", SPOTIFY_API_URL),
        ("youtube-api", YOUTUBE_API_URL),
        ("instacart-api", INSTACART_API_URL),
        ("doordash-api", DOORDASH_API_URL),
        ("yelp-api", YELP_API_URL),
        ("strava-api", STRAVA_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("plaid-api", PLAID_API_URL),
        ("wordpress-api", WORDPRESS_API_URL),
        ("twitter-api", TWITTER_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("nasa-api", NASA_API_URL),
        ("openlibrary-api", OPENLIBRARY_API_URL),
        ("google-classroom-api", GOOGLE_CLASSROOM_API_URL),
        ("eventbrite-api", EVENTBRITE_API_URL),
    ]
    touched = []
    for name, url in distractors:
        summary = api_get(url, "/audit/summary")
        endpoints = summary.get("endpoints", {})
        for k, v in endpoints.items():
            parts = k.split(" ", 1)
            route = parts[1] if len(parts) == 2 else k
            if route.startswith("/audit") or route.startswith("/health") or route.startswith("/admin"):
                continue
            if _endpoint_hits(v) > 0:
                touched.append(name)
                break
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
