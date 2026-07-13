import json
import os
from urllib.request import Request, urlopen

try:
    import pytest
except ImportError:
    pytest = None

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8060")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8065")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8016")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8075")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8090")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8040")

NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8050")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8004")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8020")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8021")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8006")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8058")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8055")
MICROSOFT_TEAMS_API_URL = os.environ.get("MICROSOFT_TEAMS_API_URL", "http://localhost:8044")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8095")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8082")
VIMEO_API_URL = os.environ.get("VIMEO_API_URL", "http://localhost:8087")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8018")

SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8074")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8093")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8076")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8054")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8048")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8063")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8094")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8092")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8005")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8080")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8081")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8062")


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


def test_quickbooks_invoices_read():
    audit = api_get(QUICKBOOKS_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET") and "invoice" in k.lower()
    )
    assert read_calls > 0, "Agent did not read QuickBooks invoices"


def test_salesforce_accounts_read():
    audit = api_get(SALESFORCE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET") and "account" in k.lower()
    )
    assert read_calls > 0, "Agent did not read Salesforce accounts"


def test_etsy_receipts_read():
    audit = api_get(ETSY_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET") and "receipt" in k.lower()
    )
    assert read_calls > 0, "Agent did not read Etsy receipts"


def test_square_orders_read():
    audit = api_get(SQUARE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET") and ("order" in k.lower() or "payment" in k.lower())
    )
    assert read_calls > 0, "Agent did not read Square orders or payments"


def test_woocommerce_orders_read():
    audit = api_get(WOOCOMMERCE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET") and "order" in k.lower()
    )
    assert read_calls > 0, "Agent did not read WooCommerce orders"


def test_mailchimp_campaigns_read():
    audit = api_get(MAILCHIMP_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    read_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if k.startswith("GET") and ("campaigns" in k.lower() or "lists" in k.lower())
    )
    assert read_calls > 0, "Agent did not read Mailchimp campaigns or lists"


def test_spotify_distractor():
    audit = api_get(SPOTIFY_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Spotify API"


def test_youtube_distractor():
    audit = api_get(YOUTUBE_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant YouTube API"


def test_strava_distractor():
    audit = api_get(STRAVA_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Strava API"


def test_openweather_distractor():
    audit = api_get(OPENWEATHER_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant OpenWeather API"


def test_nasa_distractor():
    audit = api_get(NASA_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant NASA API"


def test_ring_distractor():
    audit = api_get(RING_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Ring API"


def test_zillow_distractor():
    audit = api_get(ZILLOW_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Zillow API"


def test_yelp_distractor():
    audit = api_get(YELP_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Yelp API"


def test_airbnb_distractor():
    audit = api_get(AIRBNB_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Airbnb API"


def test_ticketmaster_distractor():
    audit = api_get(TICKETMASTER_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Ticketmaster API"


def test_tmdb_distractor():
    audit = api_get(TMDB_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant TMDB API"


def test_reddit_distractor():
    audit = api_get(REDDIT_API_URL, "/audit/summary")
    endpoints = audit.get("endpoints", {})
    business_calls = sum(
        v.get("count", 0)
        for k, v in endpoints.items()
        if "audit" not in k.lower()
    )
    assert business_calls > 0, "Agent touched irrelevant Reddit API"
