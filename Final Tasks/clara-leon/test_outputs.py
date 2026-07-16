import json
import os
import re
from urllib.request import Request, urlopen

# URL constants - one line per Required + Distractor API named by the task.
# Defaults mirror each service's canonical port from its service.toml in the harness
# environment, so a run with no env overrides still reaches the right service.
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8000")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8027")
MAILGUN_API_URL = os.environ.get("MAILGUN_API_URL", "http://localhost:8094")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")


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


def _split_key(key):
    parts = key.split(" ", 1)
    if len(parts) != 2:
        return "", ""
    return parts[0].upper(), parts[1]


def _is_business_path(path):
    p = path.lower()
    if p.startswith("/audit"):
        return False
    if p.startswith("/health"):
        return False
    return True


def business_calls(url):
    """Count non-audit, non-health endpoint calls from the audit summary."""
    try:
        summary = api_get(url, "/audit/summary")
    except Exception:
        return 0
    endpoints = summary.get("endpoints", {})
    total = 0
    for key, val in endpoints.items():
        method, path = _split_key(key)
        if not path or not _is_business_path(path):
            continue
        total += val.get("count", 0)
    return total


def write_calls(url, path_substr=None):
    """Count POST/PUT/PATCH/DELETE business calls, optionally filtered by a path substring."""
    try:
        summary = api_get(url, "/audit/summary")
    except Exception:
        return 0
    endpoints = summary.get("endpoints", {})
    total = 0
    mutations = ("POST", "PUT", "PATCH", "DELETE")
    for key, val in endpoints.items():
        method, path = _split_key(key)
        if not path or not _is_business_path(path):
            continue
        if method not in mutations:
            continue
        if path_substr and path_substr.lower() not in path.lower():
            continue
        total += val.get("count", 0)
    return total


def find_audit_requests(url, method=None, path_substr=None):
    """Return audit request entries filtered by method and path substring, excluding audit and health paths."""
    try:
        audit = api_get(url, "/audit/requests")
    except Exception:
        return []
    results = []
    for req in audit.get("requests", []):
        req_path = (req.get("path", "") or "")
        req_method = (req.get("method", "") or "").upper()
        if not _is_business_path(req_path):
            continue
        if method and req_method != method.upper():
            continue
        if path_substr and path_substr.lower() not in req_path.lower():
            continue
        results.append(req)
    return results


def _request_body_text(req):
    body = req.get("request_body", "")
    if body is None:
        return ""
    if isinstance(body, (dict, list)):
        try:
            return json.dumps(body).lower()
        except Exception:
            return str(body).lower()
    return str(body).lower()


WORKSPACE_DIR = os.environ.get("WORKSPACE_DIR", "/workspace")
_TEXT_SUFFIXES = (".md", ".markdown", ".txt", "")


def _workspace_documents():
    """Read every staged text document under the agent's workspace, lower-cased,
    returned as (path, text). The prompt dictates no filenames, so a probe finds a
    deliverable by the derived figures it carries rather than by its name."""
    docs = []
    for root, _dirs, files in os.walk(WORKSPACE_DIR):
        for name in files:
            if os.path.splitext(name)[1].lower() not in _TEXT_SUFFIXES:
                continue
            full = os.path.join(root, name)
            if not file_exists(full):
                continue
            try:
                docs.append((full, read_file(full).lower()))
            except (OSError, UnicodeDecodeError):
                continue
    return docs


def _amount_forms(amount):
    """String forms of a dollar amount so a match survives either thousands style
    (620663.62 or 620,663.62) and, for whole amounts, an omitted cents field."""
    forms = {f"{amount:.2f}", f"{amount:,.2f}"}
    if float(amount) == int(amount):
        forms.add(f"{int(amount):,}")
        forms.add(f"{int(amount)}")
    return forms


def _text_has_amount(text, amount):
    return any(form in text for form in _amount_forms(amount))


def test_behavioral_quickbooks_ledger_reads():
    """The agent must query the household ledger held in QuickBooks."""
    assert business_calls(QUICKBOOKS_API_URL) > 0, "no business calls to quickbooks-api"


def test_behavioral_xero_ledger_reads():
    """The agent must query the second household ledger held in Xero."""
    assert business_calls(XERO_API_URL) > 0, "no business calls to xero-api"


def test_behavioral_plaid_data_read():
    """The agent must pull the live account feed for the balance sweep."""
    assert business_calls(PLAID_API_URL) > 0, "no business calls to plaid-api"


def test_behavioral_alpaca_positions_read():
    """The agent must pull brokerage positions to walk the portfolio holdings."""
    assert business_calls(ALPACA_API_URL) > 0, "no business calls to alpaca-api"


def test_behavioral_salesforce_shared_folder_read():
    """The agent must pull the advisor's shared review summary from Salesforce."""
    assert business_calls(SALESFORCE_API_URL) > 0, "no business calls to salesforce-api"


def test_behavioral_paypal_orders_read():
    """The agent must pull PayPal records to reconcile the charitable giving audit."""
    assert business_calls(PAYPAL_API_URL) > 0, "no business calls to paypal-api"


def test_behavioral_stripe_charges_read():
    """The agent must pull Stripe records to reconcile the charitable giving audit."""
    assert business_calls(STRIPE_API_URL) > 0, "no business calls to stripe-api"


def test_behavioral_amazon_seller_orders_read():
    """The agent must pull the resale channel orders to tally year-to-date income."""
    assert business_calls(AMAZON_SELLER_API_URL) > 0, "no business calls to amazon-seller-api"


def test_behavioral_docusign_envelopes_read():
    """The agent must pull the electronic signing queue for the estate item filter."""
    assert business_calls(DOCUSIGN_API_URL) > 0, "no business calls to docusign-api"


def test_behavioral_zillow_properties_read():
    """The agent must pull the current condo market estimate for the net worth statement."""
    assert business_calls(ZILLOW_API_URL) > 0, "no business calls to zillow-api"


def test_behavioral_google_calendar_read():
    """The agent must confirm the upcoming quarterly sit-down on the calendar."""
    assert business_calls(GOOGLE_CALENDAR_API_URL) > 0, "no business calls to google-calendar-api"


def test_behavioral_gmail_draft_created():
    """The agent must create a Gmail draft carrying the pre-meeting note to Sheila."""
    draft_writes = 0
    try:
        summary = api_get(GMAIL_API_URL, "/audit/summary")
    except Exception:
        summary = {}
    endpoints = summary.get("endpoints", {})
    for key, val in endpoints.items():
        method, path = _split_key(key)
        if not path or not _is_business_path(path):
            continue
        if method != "POST":
            continue
        low = path.lower()
        if "draft" not in low:
            continue
        if "send" in low:
            continue
        draft_writes += val.get("count", 0)
    assert draft_writes > 0, "no gmail draft creation observed on the drafts endpoint"


def test_behavioral_notion_page_created():
    """The agent must create a Notion page for the private working papers."""
    page_writes = 0
    try:
        summary = api_get(NOTION_API_URL, "/audit/summary")
    except Exception:
        summary = {}
    endpoints = summary.get("endpoints", {})
    for key, val in endpoints.items():
        method, path = _split_key(key)
        if not path or not _is_business_path(path):
            continue
        if method != "POST":
            continue
        low = path.lower()
        if "/page" not in low:
            continue
        page_writes += val.get("count", 0)
    assert page_writes > 0, "no notion page creation observed on the pages endpoint"


def test_outcome_gmail_draft_addresses_sheila():
    """The pre-meeting note draft body must address Sheila by name."""
    drafts = find_audit_requests(GMAIL_API_URL, method="POST", path_substr="draft")
    drafts = [d for d in drafts if "send" not in (d.get("path", "") or "").lower()]
    hits = 0
    for d in drafts:
        body = _request_body_text(d)
        if "sheila" in body:
            hits += 1
    assert hits > 0, "no gmail draft body addresses Sheila"


def test_outcome_gmail_draft_has_agenda_content():
    """The pre-meeting note draft must carry a real agenda: a list structure naming several
    of the workstreams Clara prepared, not merely a stray digit or hyphen."""
    drafts = find_audit_requests(GMAIL_API_URL, method="POST", path_substr="draft")
    drafts = [d for d in drafts if "send" not in (d.get("path", "") or "").lower()]
    topics = ("portfolio", "allocation", "withdrawal", "giving", "charitable",
              "resale", "estate", "signing", "net worth", "reconcil")
    hits = 0
    for d in drafts:
        body = _request_body_text(d)
        listish = len(re.findall(r"(?:^|\n|\\n)\s*(?:[-*•]|\d[.)])\s+\S", body)) >= 3
        covered = sum(1 for t in topics if t in body)
        if listish and covered >= 3:
            hits += 1
    assert hits > 0, "no gmail draft body carries an itemised agenda naming at least three review topics"


def test_outcome_gmail_draft_requests_summary_check():
    """The pre-meeting note draft body must ask Sheila to reconcile the shared summary against the live feed."""
    drafts = find_audit_requests(GMAIL_API_URL, method="POST", path_substr="draft")
    drafts = [d for d in drafts if "send" not in (d.get("path", "") or "").lower()]
    hits = 0
    for d in drafts:
        body = _request_body_text(d)
        has_ask = ("confirm" in body) or ("verify" in body) or ("reconcile" in body) or ("check" in body)
        has_ref = ("summary" in body) or ("figure" in body) or ("live" in body)
        if has_ask and has_ref:
            hits += 1
    assert hits > 0, "no gmail draft body carries the pre-call reconciliation ask"


def test_outcome_notion_workspace_has_substantive_content():
    """The private working papers page must carry a substantive body that records which source
    was leaned on, not merely a page envelope padded to length."""
    pages = find_audit_requests(NOTION_API_URL, method="POST", path_substr="/page")
    markers = ("source", "feed", "receipt", "ledger", "summary", "live", "confirm", "set aside")
    hits = 0
    for p in pages:
        body = _request_body_text(p)
        prose = re.sub(r"[\{\}\[\]\":,]", " ", body)
        if len(prose) >= 400 and sum(1 for m in markers if m in body) >= 3:
            hits += 1
    assert hits > 0, "no notion page carries a substantive sourced working-papers body"


def test_outcome_reconciliation_brief_resolves_ledger_drift():
    """A staged workspace document must resolve the cross-book drift: the checking
    sub-ledger for mask 2119 read against the live feed (8,520.55 live current vs
    8,120.55 in the books) and the recurring line carried under both the Utilities
    and the Telecom classifications."""
    for _path, text in _workspace_documents():
        live = _text_has_amount(text, 8520.55)
        booked = _text_has_amount(text, 8120.55)
        both_tags = ("utilities" in text) and ("telecom" in text)
        if live and booked and both_tags:
            return
    assert False, "no workspace document resolves the checking drift and the utilities/telecom reclassification"


def test_outcome_portfolio_picture_defends_live_total():
    """A staged workspace document must defend the live portfolio total, name the
    stale advisor summary set aside, and walk at least twelve of the fifteen
    holdings one at a time."""
    tickers = ("bnd", "unh", "hd", "tsla", "cvx", "qcom", "abbv", "xlf",
               "bac", "pypl", "ddog", "vxus", "bil", "sgov", "voo")
    for _path, text in _workspace_documents():
        live_total = _text_has_amount(text, 620663.62)
        set_aside = _text_has_amount(text, 618400.00)
        walked = sum(1 for t in tickers if re.search(r"\b" + re.escape(t) + r"\b", text))
        if live_total and set_aside and walked >= 12:
            return
    assert False, "no workspace document defends the live portfolio total against the set-aside summary across at least twelve holdings"


def test_outcome_net_worth_statement_totals_the_household():
    """A staged workspace document must total the household net worth from its
    components, so a statement that drops the Fidelity IRA fails the arithmetic."""
    components = (620663.62, 8420.55, 48000.00, 142058.19, 342500.00)
    for _path, text in _workspace_documents():
        total = _text_has_amount(text, 1161642.36)
        present = sum(1 for c in components if _text_has_amount(text, c))
        if total and present >= 4:
            return
    assert False, "no workspace document totals the household net worth from at least four of its five components"


def test_outcome_charitable_giving_ytd_reconciles_channels():
    """A staged workspace document must reconcile giving across the three channels:
    the reconciled year-to-date total (3,760.00), at least two channel subtotals,
    and the Parish charity drive flagged by name."""
    subtotals = (1650.00, 1725.00, 385.00)
    for _path, text in _workspace_documents():
        reconciled = _text_has_amount(text, 3760.00)
        channels = sum(1 for s in subtotals if _text_has_amount(text, s))
        flagged = "parish" in text
        if reconciled and channels >= 2 and flagged:
            return
    assert False, "no workspace document reconciles the three giving channels and flags the parish charity drive"


def test_outcome_resale_income_ytd_reports_net_after_returns():
    """A staged workspace document must report the resale stream's year-to-date
    gross (27,625.77), refunds (873.75), and net (26,752.02) together."""
    for _path, text in _workspace_documents():
        gross = _text_has_amount(text, 27625.77)
        refunds = _text_has_amount(text, 873.75)
        net = _text_has_amount(text, 26752.02)
        if gross and refunds and net:
            return
    assert False, "no workspace document reports resale gross, refunds, and net year-to-date"


def test_outcome_estate_signing_queue_names_pending_items():
    """A staged workspace document must name the estate or healthcare envelopes
    still pending in the signing queue, so nothing is first heard about from Sheila."""
    items = ("trust", "healthcare", "beneficiary", "proxy", "estate")
    for _path, text in _workspace_documents():
        pending = any(m in text for m in ("pending", "awaiting", "signature", "signing", "docusign", "sent"))
        named = sum(1 for k in items if k in text)
        if pending and named >= 2:
            return
    assert False, "no workspace document names the pending estate or healthcare envelopes in the signing queue"


def test_negative_weight_distractor_apis_touched():
    """Fires when the agent reaches a crypto tracker, an outbound send service, or an
    unrelated business system - the boundary this reconciliation must stay inside."""
    distractor_registry = [
        ("coinbase-api", COINBASE_API_URL),
        ("binance-api", BINANCE_API_URL),
        ("kraken-api", KRAKEN_API_URL),
        ("sendgrid-api", SENDGRID_API_URL),
        ("mailgun-api", MAILGUN_API_URL),
        ("hubspot-api", HUBSPOT_API_URL),
        ("airtable-api", AIRTABLE_API_URL),
    ]
    touched = []
    for name, url in distractor_registry:
        if business_calls(url) > 0:
            touched.append(name)
    assert len(touched) > 0, "no distractor API was touched"


def test_negative_weight_gmail_send_endpoint_called():
    """Fires when the Gmail send endpoint is hit - the note to Sheila is a draft for
    Clara to review, never dispatched."""
    send_calls = 0
    try:
        summary = api_get(GMAIL_API_URL, "/audit/summary")
    except Exception:
        summary = {}
    endpoints = summary.get("endpoints", {})
    for key, val in endpoints.items():
        method, path = _split_key(key)
        if not path or not _is_business_path(path):
            continue
        if method != "POST":
            continue
        low = path.lower()
        if "send" not in low:
            continue
        send_calls += val.get("count", 0)
    assert send_calls > 0, "the gmail send endpoint was not called"


def test_negative_weight_quickbooks_write_endpoint_called():
    """Fires on any write to the QuickBooks books - the primary ledger stays read-only
    for this pass and the correction lives on paper in the brief."""
    writes = write_calls(QUICKBOOKS_API_URL)
    assert writes > 0, "no write endpoint was called on quickbooks-api"


def test_negative_weight_xero_write_endpoint_called():
    """Fires on any write to Xero - the cross-check ledger is only compared against
    QuickBooks, never edited."""
    writes = write_calls(XERO_API_URL)
    assert writes > 0, "no write endpoint was called on xero-api"
