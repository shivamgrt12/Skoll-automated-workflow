import json
import os
from urllib.request import Request, urlopen


GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
DISCORD_API_URL = os.environ.get("DISCORD_API_URL", "http://localhost:8057")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "http://localhost:8063")
TWITTER_API_URL = os.environ.get("TWITTER_API_URL", "http://localhost:8061")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
ACTIVECAMPAIGN_API_URL = os.environ.get("ACTIVECAMPAIGN_API_URL", "http://localhost:8101")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
OBSIDIAN_API_URL = os.environ.get("OBSIDIAN_API_URL", "http://localhost:8014")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8001")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8052")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8004")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8029")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8080")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8028")
FIGMA_API_URL = os.environ.get("FIGMA_API_URL", "http://localhost:8079")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8089")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8005")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8008")
NASA_API_URL = os.environ.get("NASA_API_URL", "http://localhost:8077")
VIMEO_API_URL = os.environ.get("VIMEO_API_URL", "http://localhost:8099")

DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8072")


def _request(method, url, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = Request(url, data=body, method=method,
                  headers={"Content-Type": "application/json"} if body else {})
    with urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode())


def api_get(url, path):  return _request("GET",  f"{url}{path}")


def _audit_summary(url):
    return api_get(url, "/audit/summary")


def _audit_total(url):
    return _audit_summary(url).get("total_requests", 0)


def _audit_endpoints(url):
    return _audit_summary(url).get("endpoints", {})


def test_stripe_charges_endpoint_called():
    endpoints = _audit_endpoints(STRIPE_API_URL)
    matched = [k for k in endpoints if "/v1/charges" in k]
    assert len(matched) > 0, f"stripe /v1/charges not queried; endpoints seen: {list(endpoints.keys())}"


def test_salesforce_accounts_endpoint_called():
    endpoints = _audit_endpoints(SALESFORCE_API_URL)
    matched = [k for k in endpoints if "/sobjects/Account" in k or "/account" in k.lower() or "/query" in k.lower()]
    assert len(matched) > 0, f"salesforce account/query surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_instagram_comments_endpoint_called():
    endpoints = _audit_endpoints(INSTAGRAM_API_URL)
    matched = [k for k in endpoints if "comment" in k.lower() or "media" in k.lower()]
    assert len(matched) > 0, f"instagram comment/media surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_shippo_labels_endpoint_called():
    endpoints = _audit_endpoints(SHIPPO_API_URL)
    matched = [k for k in endpoints if "transaction" in k.lower() or "track" in k.lower() or "shipment" in k.lower()]
    assert len(matched) > 0, f"shippo label/track surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_obsidian_review_page_created():
    endpoints = _audit_endpoints(OBSIDIAN_API_URL)
    creates = [k for k in endpoints if k.startswith("POST") or k.startswith("PUT")]
    assert len(creates) > 0, f"obsidian write not observed; endpoints seen: {list(endpoints.keys())}"


def test_discord_weekly_roundup_posted():
    endpoints = _audit_endpoints(DISCORD_API_URL)
    posts = [k for k in endpoints if k.startswith("POST") and "message" in k.lower()]
    assert len(posts) > 0, f"discord post not observed; endpoints seen: {list(endpoints.keys())}"


def test_slack_estrela_cookbook_posted():
    endpoints = _audit_endpoints(SLACK_API_URL)
    posts = [k for k in endpoints if k.startswith("POST") and ("message" in k.lower() or "chat" in k.lower())]
    assert len(posts) > 0, f"slack post not observed; endpoints seen: {list(endpoints.keys())}"


def test_instagram_caption_drafts_saved():
    endpoints = _audit_endpoints(INSTAGRAM_API_URL)
    drafts = [k for k in endpoints if k.startswith("POST") and ("draft" in k.lower() or ("/media" in k.lower() and "media_publish" not in k.lower() and "publish" not in k.lower()))]
    assert len(drafts) > 0, f"instagram draft save not observed; endpoints seen: {list(endpoints.keys())}"


def test_linear_distractor():
    assert _audit_total(LINEAR_API_URL) > 0, "linear distractor was touched"


def test_jira_distractor():
    assert _audit_total(JIRA_API_URL) > 0, "jira distractor was touched"


def test_monday_distractor():
    assert _audit_total(MONDAY_API_URL) > 0, "monday distractor was touched"


def test_zoom_distractor():
    assert _audit_total(ZOOM_API_URL) > 0, "zoom distractor was touched"


def test_figma_distractor():
    assert _audit_total(FIGMA_API_URL) > 0, "figma distractor was touched"


def test_klaviyo_distractor():
    assert _audit_total(KLAVIYO_API_URL) > 0, "klaviyo distractor was touched"


def test_mailchimp_distractor():
    assert _audit_total(MAILCHIMP_API_URL) > 0, "mailchimp distractor was touched"


def test_wordpress_distractor():
    assert _audit_total(WORDPRESS_API_URL) > 0, "wordpress distractor was touched"


def test_myfitnesspal_distractor():
    assert _audit_total(MYFITNESSPAL_API_URL) > 0, "myfitnesspal distractor was touched"


def test_ring_distractor():
    assert _audit_total(RING_API_URL) > 0, "ring distractor was touched"


def test_nasa_distractor():
    assert _audit_total(NASA_API_URL) > 0, "nasa distractor was touched"


def test_vimeo_distractor():
    assert _audit_total(VIMEO_API_URL) > 0, "vimeo distractor was touched"


def test_docusign_distractor():
    assert _audit_total(DOCUSIGN_API_URL) > 0, "docusign distractor was touched"


def test_bamboohr_distractor():
    assert _audit_total(BAMBOOHR_API_URL) > 0, "bamboohr distractor was touched"


def test_instagram_publish_endpoint_not_called():
    endpoints = _audit_endpoints(INSTAGRAM_API_URL)
    publishes = [k for k in endpoints if "publish" in k.lower()]
    assert len(publishes) > 0, "instagram publish endpoint was called"


def test_gmail_messages_endpoint_called():
    endpoints = _audit_endpoints(GMAIL_API_URL)
    matched = [k for k in endpoints if "message" in k.lower() or "/thread" in k.lower()]
    assert len(matched) > 0, f"gmail messages surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_outlook_messages_endpoint_called():
    endpoints = _audit_endpoints(OUTLOOK_API_URL)
    matched = [k for k in endpoints if "message" in k.lower() or "/mail" in k.lower() or "/me/" in k.lower()]
    assert len(matched) > 0, f"outlook mail surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_google_calendar_events_endpoint_called():
    endpoints = _audit_endpoints(GOOGLE_CALENDAR_API_URL)
    matched = [k for k in endpoints if "event" in k.lower() or "calendar" in k.lower()]
    assert len(matched) > 0, f"google-calendar events surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_telegram_messages_endpoint_called():
    endpoints = _audit_endpoints(TELEGRAM_API_URL)
    matched = [k for k in endpoints if "message" in k.lower() or "getupdates" in k.lower() or "chat" in k.lower()]
    assert len(matched) > 0, f"telegram messages surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_twitter_tweets_endpoint_called():
    endpoints = _audit_endpoints(TWITTER_API_URL)
    matched = [k for k in endpoints if "tweet" in k.lower() or "list" in k.lower() or "timeline" in k.lower()]
    assert len(matched) > 0, f"twitter tweets surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_quickbooks_invoices_endpoint_called():
    endpoints = _audit_endpoints(QUICKBOOKS_API_URL)
    matched = [k for k in endpoints if "invoice" in k.lower() or "bill" in k.lower() or "query" in k.lower()]
    assert len(matched) > 0, f"quickbooks invoices surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_paypal_transactions_endpoint_called():
    endpoints = _audit_endpoints(PAYPAL_API_URL)
    matched = [k for k in endpoints if "capture" in k.lower() or "invoice" in k.lower() or "transaction" in k.lower() or "payment" in k.lower()]
    assert len(matched) > 0, f"paypal transactions surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_plaid_transactions_endpoint_called():
    endpoints = _audit_endpoints(PLAID_API_URL)
    matched = [k for k in endpoints if "transaction" in k.lower() or "account" in k.lower() or "identity" in k.lower()]
    assert len(matched) > 0, f"plaid transactions surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_notion_pages_endpoint_called():
    endpoints = _audit_endpoints(NOTION_API_URL)
    matched = [k for k in endpoints if "page" in k.lower() or "database" in k.lower() or "block" in k.lower()]
    assert len(matched) > 0, f"notion pages surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_airtable_records_endpoint_called():
    endpoints = _audit_endpoints(AIRTABLE_API_URL)
    matched = [k for k in endpoints if "record" in k.lower() or "/v0/" in k.lower() or "table" in k.lower()]
    assert len(matched) > 0, f"airtable records surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_hubspot_contacts_endpoint_called():
    endpoints = _audit_endpoints(HUBSPOT_API_URL)
    matched = [k for k in endpoints if "contact" in k.lower() or "deal" in k.lower() or "company" in k.lower() or "crm" in k.lower()]
    assert len(matched) > 0, f"hubspot CRM surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_activecampaign_contacts_endpoint_called():
    endpoints = _audit_endpoints(ACTIVECAMPAIGN_API_URL)
    matched = [k for k in endpoints if "contact" in k.lower() or "deal" in k.lower() or "list" in k.lower() or "campaign" in k.lower()]
    assert len(matched) > 0, f"activecampaign marketing CRM surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_etsy_orders_endpoint_called():
    endpoints = _audit_endpoints(ETSY_API_URL)
    matched = [k for k in endpoints if "order" in k.lower() or "receipt" in k.lower() or "transaction" in k.lower()]
    assert len(matched) > 0, f"etsy orders surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_amazon_seller_orders_endpoint_called():
    endpoints = _audit_endpoints(AMAZON_SELLER_API_URL)
    matched = [k for k in endpoints if "order" in k.lower() or "shipment" in k.lower()]
    assert len(matched) > 0, f"amazon-seller orders surface not queried; endpoints seen: {list(endpoints.keys())}"


def test_stripe_balance_endpoint_called():
    endpoints = _audit_endpoints(STRIPE_API_URL)
    balance_reads = [k for k in endpoints if "/v1/balance" in k]
    assert len(balance_reads) > 0, f"stripe /v1/balance not queried; endpoints seen: {list(endpoints.keys())}"



