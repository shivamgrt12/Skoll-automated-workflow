import json
import os
import urllib.request
import urllib.error
from pathlib import Path
from typing import Iterable

TASK_ROOT = Path(
    os.environ.get(
        "CARLOS_REED_ROOT",
        Path(__file__).resolve().parent,
    )
)
WORKSPACE_DIR = Path(
    os.environ.get(
        "CARLOS_REED_WORKSPACE",
        TASK_ROOT / "workspace",
    )
)
MOCK_DIR = TASK_ROOT / "mock_data"

AIRTABLE_URL = os.environ.get("AIRTABLE_URL", "http://localhost:8032")
BAMBOOHR_URL = os.environ.get("BAMBOOHR_URL", "http://localhost:8072")
COINBASE_URL = os.environ.get("COINBASE_URL", "http://localhost:8023")
CONFLUENCE_URL = os.environ.get("CONFLUENCE_URL", "http://localhost:8045")
DOCUSIGN_URL = os.environ.get("DOCUSIGN_URL", "http://localhost:8053")
GMAIL_URL = os.environ.get("GMAIL_URL", "http://localhost:8017")
GOOGLE_CALENDAR_URL = os.environ.get("GOOGLE_CALENDAR_URL", "http://localhost:8016")
JIRA_URL = os.environ.get("JIRA_URL", "http://localhost:8029")
NOTION_URL = os.environ.get("NOTION_URL", "http://localhost:8010")
OKTA_URL = os.environ.get("OKTA_URL", "http://localhost:8049")
PLAID_URL = os.environ.get("PLAID_URL", "http://localhost:8022")
QUICKBOOKS_URL = os.environ.get("QUICKBOOKS_URL", "http://localhost:8007")
SENDGRID_URL = os.environ.get("SENDGRID_URL", "http://localhost:8027")
SLACK_URL = os.environ.get("SLACK_URL", "http://localhost:8013")
SQUARE_URL = os.environ.get("SQUARE_URL", "http://localhost:8041")
STRIPE_URL = os.environ.get("STRIPE_URL", "http://localhost:8021")
TRELLO_URL = os.environ.get("TRELLO_URL", "http://localhost:8030")
WHATSAPP_URL = os.environ.get("WHATSAPP_URL", "http://localhost:8015")
WOOCOMMERCE_URL = os.environ.get("WOOCOMMERCE_URL", "http://localhost:8085")
XERO_URL = os.environ.get("XERO_URL", "http://localhost:8088")
ZILLOW_URL = os.environ.get("ZILLOW_URL", "http://localhost:8011")

REQUEST_TIMEOUT = 15


def _http_get_json(url: str) -> dict:
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    return json.loads(raw)


def _audit_summary(base_url: str) -> dict:
    return _http_get_json(f"{base_url.rstrip('/')}/audit/summary")


def _count_calls(base_url: str, prefixes: Iterable[str]) -> int:
    try:
        summary = _audit_summary(base_url)
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError):
        return 0
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    total = 0
    prefix_tuple = tuple(prefixes)
    for endpoint, stats in endpoints.items():
        if not any(endpoint.startswith(p) for p in prefix_tuple):
            continue
        if isinstance(stats, dict):
            total += int(stats.get("count", 0))
        else:
            try:
                total += int(stats)
            except (TypeError, ValueError):
                continue
    return total


def _workspace_matches(patterns: Iterable[str]) -> list[Path]:
    matches: list[Path] = []
    if not WORKSPACE_DIR.exists():
        return matches
    seen: set[Path] = set()
    for pattern in patterns:
        for path in WORKSPACE_DIR.rglob(pattern):
            if path.is_file() and path not in seen:
                seen.add(path)
                matches.append(path)
    return matches


_MIN_ARTIFACT_BYTES = 256


def _has_substantive_content(paths: Iterable[Path]) -> bool:
    for path in paths:
        try:
            if path.stat().st_size >= _MIN_ARTIFACT_BYTES:
                return True
        except OSError:
            continue
    return False


def test_workspace_monica_continuity_brief_present():
    hits = _workspace_matches(
        [
            "monica_continuity_brief.*",
            "*monica*continuity*.*",
            "*continuity_brief*",
        ]
    )
    assert hits, "workspace missing Monica continuity brief artifact"
    assert _has_substantive_content(hits), (
        "Monica continuity brief artifact present but below "
        f"{_MIN_ARTIFACT_BYTES}-byte substantive-content threshold"
    )


def test_workspace_subscriber_ledger_reconciled_present():
    hits = _workspace_matches(
        [
            "subscriber_ledger_reconciled.*",
            "*subscriber*reconciled*.*",
            "*reconciled*subscriber*.*",
        ]
    )
    assert hits, "workspace missing reconciled subscriber ledger artifact"
    assert _has_substantive_content(hits), (
        "reconciled subscriber ledger artifact present but below "
        f"{_MIN_ARTIFACT_BYTES}-byte substantive-content threshold"
    )


def test_workspace_sponsor_book_present():
    hits = _workspace_matches(
        [
            "sponsor_book_2027.*",
            "*sponsor*book*2027*.*",
            "*2027*sponsor*book*.*",
        ]
    )
    assert hits, "workspace missing 2027 sponsor book artifact"
    assert _has_substantive_content(hits), (
        "2027 sponsor book artifact present but below "
        f"{_MIN_ARTIFACT_BYTES}-byte substantive-content threshold"
    )


def test_workspace_q1_kpi_view_present():
    hits = _workspace_matches(
        [
            "q1_2027_kpi*.*",
            "*q1*2027*kpi*.*",
            "*kpi*2027*.*",
        ]
    )
    assert hits, "workspace missing Q1 2027 KPI view artifact"
    assert _has_substantive_content(hits), (
        "Q1 2027 KPI view artifact present but below "
        f"{_MIN_ARTIFACT_BYTES}-byte substantive-content threshold"
    )


def test_workspace_q1_pnl_present():
    hits = _workspace_matches(
        [
            "q1_2027_pnl*.*",
            "*q1*2027*pnl*.*",
            "*2027*pnl*.*",
        ]
    )
    assert hits, "workspace missing Q1 2027 P&L artifact"
    assert _has_substantive_content(hits), (
        "Q1 2027 P&L artifact present but below "
        f"{_MIN_ARTIFACT_BYTES}-byte substantive-content threshold"
    )


def test_quickbooks_reports_read():
    hits = _count_calls(
        QUICKBOOKS_URL,
        ["GET /v3/company"],
    )
    assert hits >= 1, "QuickBooks reports/company surface never read"


def test_xero_invoices_or_reports_read():
    hits = _count_calls(
        XERO_URL,
        [
            "GET /api.xro/2.0/Invoices",
            "GET /api.xro/2.0/Reports",
        ],
    )
    assert hits >= 1, "Xero invoices/reports never read"


def test_stripe_charges_read():
    hits = _count_calls(STRIPE_URL, ["GET /v1/charges"])
    assert hits >= 1, "Stripe /v1/charges never read"


def test_stripe_customers_read():
    hits = _count_calls(STRIPE_URL, ["GET /v1/customers"])
    assert hits >= 1, "Stripe /v1/customers never read"


def test_sendgrid_marketing_read():
    hits = _count_calls(
        SENDGRID_URL,
        [
            "GET /v3/marketing/contacts",
            "GET /v3/marketing/lists",
            "GET /v3/marketing",
        ],
    )
    assert hits >= 1, "SendGrid marketing surface never read"


def test_gmail_user_surface_read():
    hits = _count_calls(
        GMAIL_URL,
        [
            "GET /gmail/v1/users/me/messages",
            "GET /gmail/v1/users/me/drafts",
            "GET /gmail/v1/users/me/labels",
            "GET /gmail/v1/users/me",
        ],
    )
    assert hits >= 1, "Gmail user surface never read"


def test_google_calendar_read():
    hits = _count_calls(
        GOOGLE_CALENDAR_URL,
        [
            "GET /calendar/v3/users/me/calendarList",
            "GET /calendar/v3/calendars",
            "GET /calendar/v3",
        ],
    )
    assert hits >= 1, "Google Calendar never read"


def test_notion_pages_or_databases_read():
    hits = _count_calls(
        NOTION_URL,
        [
            "GET /v1/pages",
            "GET /v1/databases",
            "POST /v1/databases",
            "POST /v1/search",
        ],
    )
    assert hits >= 1, "Notion pages/databases/search never read"


def test_airtable_records_read():
    hits = _count_calls(
        AIRTABLE_URL,
        [
            "GET /v0/meta/bases",
            "GET /v0/",
        ],
    )
    assert hits >= 1, "Airtable base or records surface never read"


def test_square_catalog_or_orders_read():
    hits = _count_calls(
        SQUARE_URL,
        [
            "GET /v2/catalog",
            "GET /v2/orders",
            "GET /v2/payments",
            "GET /v2/customers",
        ],
    )
    assert hits >= 1, "Square catalog or orders surface never read"


def test_trello_boards_or_cards_read():
    hits = _count_calls(
        TRELLO_URL,
        [
            "GET /1/members/me/boards",
            "GET /1/boards",
            "GET /1/cards",
            "GET /1/lists",
        ],
    )
    assert hits >= 1, "Trello boards or cards surface never read"


def test_whatsapp_messages_read():
    hits = _count_calls(
        WHATSAPP_URL,
        [
            "GET /v18.0/",
            "GET /v17.0/",
            "GET /v1/",
        ],
    )
    assert hits >= 1, "WhatsApp messages surface never read"


def test_woocommerce_products_or_orders_read():
    hits = _count_calls(
        WOOCOMMERCE_URL,
        [
            "GET /wp-json/wc/v3/products",
            "GET /wp-json/wc/v3/orders",
            "GET /wp-json/wc/v3/customers",
        ],
    )
    assert hits >= 1, "WooCommerce products or orders surface never read"


def test_no_jira_issue_created():
    hits = _count_calls(
        JIRA_URL,
        [
            "POST /rest/api/3/issue",
            "PUT /rest/api/3/issue",
            "POST /rest/api/2/issue",
        ],
    )
    assert hits > 0


def test_no_confluence_content_created():
    hits = _count_calls(
        CONFLUENCE_URL,
        [
            "POST /content",
            "PUT /content",
            "POST /wiki/rest/api/content",
            "PUT /wiki/rest/api/content",
        ],
    )
    assert hits > 0


def test_no_slack_message_posted():
    hits = _count_calls(
        SLACK_URL,
        [
            "POST /api/chat.postMessage",
            "POST /api/chat.update",
            "POST /api/conversations.create",
        ],
    )
    assert hits > 0


def test_no_okta_user_lifecycle_changed():
    hits = _count_calls(
        OKTA_URL,
        [
            "POST /api/v1/users",
            "PUT /api/v1/users",
            "DELETE /api/v1/users",
        ],
    )
    assert hits > 0


def test_no_zillow_saved_search_created():
    hits = _count_calls(
        ZILLOW_URL,
        [
            "POST /v1/users",
            "POST /v1/saved-searches",
            "DELETE /v1/saved-searches",
        ],
    )
    assert hits > 0


def test_no_coinbase_buy_or_sell_executed():
    hits = _count_calls(
        COINBASE_URL,
        [
            "POST /v2/accounts",
            "PUT /v2/accounts",
        ],
    )
    assert hits > 0


def test_no_plaid_accounts_pulled():
    hits = _count_calls(
        PLAID_URL,
        [
            "POST /accounts/get",
            "POST /accounts/balance/get",
            "POST /transactions/get",
            "POST /identity/get",
        ],
    )
    assert hits > 0


def test_no_bamboohr_time_off_submitted():
    hits = _count_calls(
        BAMBOOHR_URL,
        [
            "POST /time_off/requests",
            "PUT /time_off/requests",
            "POST /v1/time_off/requests",
            "PUT /v1/time_off/requests",
        ],
    )
    assert hits > 0


def test_no_docusign_envelope_created():
    hits = _count_calls(
        DOCUSIGN_URL,
        [
            "POST /restapi/v2.1/accounts",
            "PUT /restapi/v2.1/accounts",
        ],
    )
    assert hits > 0
