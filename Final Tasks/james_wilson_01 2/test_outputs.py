import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

# Service URL constants
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8001")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8004")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8050")
BIGCOMMERCE_API_URL = os.environ.get("BIGCOMMERCE_API_URL", "http://localhost:8051")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8052")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8053")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8054")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8055")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8056")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8057")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8058")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8059")
SHIPPO_API_URL = os.environ.get("SHIPPO_API_URL", "http://localhost:8060")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8061")
CONTENTFUL_API_URL = os.environ.get("CONTENTFUL_API_URL", "http://localhost:8062")
WEBFLOW_API_URL = os.environ.get("WEBFLOW_API_URL", "http://localhost:8063")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8064")
ALGOLIA_API_URL = os.environ.get("ALGOLIA_API_URL", "http://localhost:8065")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8066")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8067")
ACTIVECAMPAIGN_API_URL = os.environ.get("ACTIVECAMPAIGN_API_URL", "http://localhost:8068")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8069")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8070")
FEDEX_API_URL = os.environ.get("FEDEX_API_URL", "http://localhost:8071")
UPS_API_URL = os.environ.get("UPS_API_URL", "http://localhost:8072")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8073")


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


def _summary_endpoints(base_url):
    data = api_get(base_url, "/audit/summary")
    if isinstance(data, dict):
        return data.get("endpoints", {})
    return {}


def _count_calls(base_url, methods):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        method, path = parts[0].upper(), parts[1]
        if path.startswith("/audit") or path == "/health":
            continue
        if methods is None or method in methods:
            count = info.get("count", 0) if isinstance(info, dict) else 0
            total += int(count)
    return total


def business_calls(base_url):
    return _count_calls(base_url, None)


def read_calls(base_url):
    return _count_calls(base_url, {"GET"})


def write_calls(base_url):
    return _count_calls(base_url, {"POST", "PUT", "PATCH", "DELETE"})


def test_square_inventory_read():
    assert read_calls(SQUARE_API_URL) > 0, "no read calls recorded against square-api"


def test_quickbooks_books_read():
    assert read_calls(QUICKBOOKS_API_URL) > 0, "no read calls recorded against quickbooks-api"


def test_etsy_listings_read():
    assert read_calls(ETSY_API_URL) > 0, "no read calls recorded against etsy-api"


def test_amazon_catalog_read():
    assert read_calls(AMAZON_SELLER_API_URL) > 0, "no read calls recorded against amazon-seller-api"


def test_woocommerce_products_read():
    assert read_calls(WOOCOMMERCE_API_URL) > 0, "no read calls recorded against woocommerce-api"


def test_bigcommerce_wholesale_read():
    assert read_calls(BIGCOMMERCE_API_URL) > 0, "no read calls recorded against bigcommerce-api"


def test_stripe_charges_read():
    assert read_calls(STRIPE_API_URL) > 0, "no read calls recorded against stripe-api"


def test_paypal_captures_read():
    assert read_calls(PAYPAL_API_URL) > 0, "no read calls recorded against paypal-api"


def test_plaid_transactions_read():
    assert read_calls(PLAID_API_URL) > 0, "no read calls recorded against plaid-api"


def test_monday_board_read():
    assert read_calls(MONDAY_API_URL) > 0, "no read calls recorded against monday-api"


def test_linear_roadmap_read():
    assert read_calls(LINEAR_API_URL) > 0, "no read calls recorded against linear-api"


def test_trello_pipeline_read():
    assert read_calls(TRELLO_API_URL) > 0, "no read calls recorded against trello-api"


def test_airtable_base_read():
    assert read_calls(AIRTABLE_API_URL) > 0, "no read calls recorded against airtable-api"


def test_gusto_payroll_read():
    assert read_calls(GUSTO_API_URL) > 0, "no read calls recorded against gusto-api"


def test_storefront_live_writes():
    live = (write_calls(ETSY_API_URL) + write_calls(AMAZON_SELLER_API_URL)
            + write_calls(WOOCOMMERCE_API_URL) + write_calls(BIGCOMMERCE_API_URL))
    assert live == 0, f"Storefront live writes detected across etsy/amazon/woocommerce/bigcommerce: {live}"


def test_distractor_apis_touched():
    distractors = [
        ("shippo-api", SHIPPO_API_URL),
        ("xero-api", XERO_API_URL),
        ("contentful-api", CONTENTFUL_API_URL),
        ("webflow-api", WEBFLOW_API_URL),
        ("wordpress-api", WORDPRESS_API_URL),
        ("algolia-api", ALGOLIA_API_URL),
        ("mailchimp-api", MAILCHIMP_API_URL),
        ("klaviyo-api", KLAVIYO_API_URL),
        ("activecampaign-api", ACTIVECAMPAIGN_API_URL),
        ("sendgrid-api", SENDGRID_API_URL),
        ("typeform-api", TYPEFORM_API_URL),
        ("fedex-api", FEDEX_API_URL),
        ("ups-api", UPS_API_URL),
        ("eventbrite-api", EVENTBRITE_API_URL),
    ]
    touched = [name for name, url in distractors if business_calls(url) > 0]
    assert len(touched) == 0, f"Distractor APIs touched: {sorted(touched)}"
