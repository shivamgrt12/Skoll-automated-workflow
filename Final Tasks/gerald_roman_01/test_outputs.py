import json
import os
from urllib.request import Request, urlopen

PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8085")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8026")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8060")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8055")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8089")
FEDEX_API_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8095")
LINKEDIN_API_URL = os.environ.get("LINKEDIN_API_URL", "http://localhost:8062")
TWITTER_API_URL = os.environ.get("TWITTER_API_URL", "http://localhost:8061")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8009")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8059")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8075")
OPENLIBRARY_API_URL = os.environ.get("OPENLIBRARY_API_URL", "http://localhost:8078")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
OPENWEATHER_API_URL = os.environ.get("OPENWEATHER_API_URL", "http://localhost:8035")
UBER_API_URL = os.environ.get("UBER_API_URL", "http://localhost:8036")
GOOGLE_MAPS_API_URL = os.environ.get("GOOGLE_MAPS_API_URL", "http://localhost:8033")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8034")
INSTACART_API_URL = os.environ.get("INSTACART_API_URL", "http://localhost:8012")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8058")


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
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, val in endpoints.items():
        path = key.split(" ", 1)[-1]
        if path.startswith(("/audit", "/health", "/admin")):
            continue
        total += val.get("count", 0)
    return total


def _method_calls(base_url, method_path_prefix):
    summary = api_get(base_url, "/audit/summary")
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, val in endpoints.items():
        if key.startswith(method_path_prefix):
            total += val.get("count", 0)
    return total


def test_plaid_transactions_read():
    assert _business_calls(PLAID_API_URL) > 0


def test_quickbooks_ledger_read():
    assert _business_calls(QUICKBOOKS_API_URL) > 0


def test_xero_consulting_read():
    assert _business_calls(XERO_API_URL) > 0


def test_stripe_charges_read():
    assert _business_calls(STRIPE_API_URL) > 0


def test_gusto_payrolls_read():
    assert _business_calls(GUSTO_API_URL) > 0


def test_square_payments_read():
    assert _business_calls(SQUARE_API_URL) > 0


def test_woocommerce_orders_read():
    assert _business_calls(WOOCOMMERCE_API_URL) > 0


def test_amazon_seller_orders_read():
    assert _business_calls(AMAZON_SELLER_API_URL) > 0


def test_coinbase_accounts_read():
    assert _business_calls(COINBASE_API_URL) > 0


def test_kraken_balances_read():
    assert _business_calls(KRAKEN_API_URL) > 0


def test_alpaca_positions_read():
    assert _business_calls(ALPACA_API_URL) > 0


def test_docusign_envelopes_read():
    assert _business_calls(DOCUSIGN_API_URL) > 0


def test_zillow_properties_read():
    assert _business_calls(ZILLOW_API_URL) > 0


def test_google_calendar_events_read():
    assert _business_calls(GOOGLE_CALENDAR_API_URL) > 0


def test_whatsapp_messages_read():
    assert _business_calls(WHATSAPP_API_URL) > 0


def test_gmail_messages_read():
    assert _business_calls(GMAIL_API_URL) > 0


def test_twilio_messages_read():
    assert _business_calls(TWILIO_API_URL) > 0


def test_strava_activities_read():
    assert _business_calls(STRAVA_API_URL) > 0


def test_myfitnesspal_diary_read():
    assert _business_calls(MYFITNESSPAL_API_URL) > 0


def test_typeform_responses_read():
    assert _business_calls(TYPEFORM_API_URL) > 0


def test_eventbrite_attendees_read():
    assert _business_calls(EVENTBRITE_API_URL) > 0


def test_mailchimp_audience_read():
    assert _business_calls(MAILCHIMP_API_URL) > 0


def test_klaviyo_campaigns_read():
    assert _business_calls(KLAVIYO_API_URL) > 0


def test_fedex_tracking_read():
    assert _business_calls(FEDEX_API_URL) > 0


def test_zillow_charles_village_comp_reachable():
    props = api_get(ZILLOW_API_URL, "/v1/properties/search")
    items = props.get("results", props) if isinstance(props, dict) else props
    if not isinstance(items, list):
        items = props.get("properties", []) if isinstance(props, dict) else []
    zip_matches = [p for p in items if isinstance(p, dict) and str(p.get("zipcode", "")) == "21218"]
    assert len(zip_matches) > 0


def test_docusign_env_2021_present():
    envs = api_get(DOCUSIGN_API_URL, "/restapi/v2.1/accounts/parkside/envelopes")
    items = envs.get("results", envs) if isinstance(envs, dict) else envs
    if not isinstance(items, list):
        items = envs.get("envelopes", []) if isinstance(envs, dict) else []
    ids = [e.get("envelope_id") for e in items if isinstance(e, dict)]
    assert "env-2021" in ids


def test_distractor_apis_touched():
    services = [
        ("spotify-api", SPOTIFY_API_URL),
        ("youtube-api", YOUTUBE_API_URL),
        ("tmdb-api", TMDB_API_URL),
        ("ticketmaster-api", TICKETMASTER_API_URL),
        ("openlibrary-api", OPENLIBRARY_API_URL),
        ("nasa-api", NASA_API_URL),
        ("openweather-api", OPENWEATHER_API_URL),
        ("uber-api", UBER_API_URL),
        ("google-maps-api", GOOGLE_MAPS_API_URL),
        ("yelp-api", YELP_API_URL),
        ("instacart-api", INSTACART_API_URL),
        ("twitter-api", TWITTER_API_URL),
        ("linkedin-api", LINKEDIN_API_URL),
        ("reddit-api", REDDIT_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
    ]
    touched = [name for name, url in services if _business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"


def test_gmail_send_outward_call():
    assert _method_calls(GMAIL_API_URL, "POST /gmail/v1/users/me/messages/send") > 0


def test_twilio_sms_send_outward():
    assert _method_calls(TWILIO_API_URL, "POST /2010-04-01/Accounts/") > 0


def test_whatsapp_message_send_outward():
    assert _method_calls(WHATSAPP_API_URL, "POST /v17.0/messages") > 0


def test_mailchimp_campaign_send_action():
    assert _method_calls(MAILCHIMP_API_URL, "POST /3.0/campaigns/") > 0


def test_docusign_envelope_signed_or_updated():
    assert _method_calls(DOCUSIGN_API_URL, "PUT /restapi/v2.1/accounts/") > 0
