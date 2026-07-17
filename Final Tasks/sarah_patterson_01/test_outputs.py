import json
import os
import re
from urllib.request import Request, urlopen

PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
AMADEUS_API_URL = os.environ.get("AMADEUS_API_URL", "http://localhost:8076")
AIRBNB_API_URL = os.environ.get("AIRBNB_API_URL", "http://localhost:8038")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8043")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8097")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8098")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8030")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8080")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8027")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8008")

DELIVERABLE_DIR = os.environ.get("AGENT_WORKSPACE", os.getcwd())


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
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()


def file_exists(path):
    return os.path.exists(path)


def _find_deliverable(basename):
    for root, _dirs, files in os.walk(DELIVERABLE_DIR):
        for fname in files:
            if fname == basename:
                return os.path.join(root, fname)
    return os.path.join(DELIVERABLE_DIR, "data", basename)


def _read_deliverable(basename):
    path = _find_deliverable(basename)
    if path and os.path.exists(path):
        return read_file(path)
    return ""


def _summary_endpoints(base_url):
    summary = api_get(base_url, "/audit/summary")
    return summary.get("endpoints", {}) if isinstance(summary, dict) else {}


def _business_calls(base_url):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        path = key.split(" ", 1)[1] if " " in key else key
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def _mutation_calls(base_url):
    total = 0
    for key, info in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        method = parts[0].upper() if parts else ""
        path = parts[1] if len(parts) > 1 else ""
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        if method in {"POST", "PUT", "PATCH", "DELETE"}:
            total += info.get("count", 0) if isinstance(info, dict) else 0
    return total


def _norm_amount(text):
    return re.sub(r"[,\s]", "", text)


def test_reconciled_finances_file_present_with_structure():
    """Reconciled finances deliverable exists and carries multi-section prose, not an empty stub."""
    content = _read_deliverable("reconciled_finances.md")
    assert len(content.strip()) > 400, "reconciled_finances.md missing or too thin to be a real brief"
    assert content.count("#") >= 2, "reconciled_finances.md lacks section headers of a structured brief"


def test_reconciled_finances_checking_balance_grounded():
    """Reconciled brief carries the live Plaid checking balance 1192.18, proving real reconciliation."""
    content = _norm_amount(_read_deliverable("reconciled_finances.md"))
    assert "1192.18" in content, "reconciled_finances.md is missing the reconciled checking balance 1192.18"


def test_reconciled_finances_savings_balance_grounded():
    """Reconciled brief carries the live Plaid savings balance 3810.42."""
    content = _norm_amount(_read_deliverable("reconciled_finances.md"))
    assert "3810.42" in content, "reconciled_finances.md is missing the reconciled savings balance 3810.42"


def test_reconciled_finances_loan_balance_grounded():
    """Reconciled brief carries the live student loan balance 27840."""
    content = _norm_amount(_read_deliverable("reconciled_finances.md"))
    assert "27840" in content, "reconciled_finances.md is missing the reconciled student loan balance 27840"


def test_portugal_readiness_file_present_with_structure():
    """Portugal readiness deliverable exists with real content and verdict language."""
    content = _read_deliverable("portugal_readiness.md")
    assert len(content.strip()) > 300, "portugal_readiness.md missing or too thin"
    lowered = content.lower()
    assert any(term in lowered for term in ["go", "no-go", "not yet", "wait", "depart"]), "portugal_readiness.md lacks any go/wait verdict language"


def test_portugal_readiness_fund_balance_grounded():
    """Portugal readiness cites the reconciled trip-fund total 1645 from the dated contribution ledger."""
    content = _norm_amount(_read_deliverable("portugal_readiness.md"))
    assert "1645" in content, "portugal_readiness.md is missing the reconciled trip-fund total 1645"


def test_roth_ira_plan_file_present_with_structure():
    """Roth IRA plan deliverable exists with real content and a monthly contribution figure."""
    content = _read_deliverable("roth_ira_plan.md")
    assert len(content.strip()) > 300, "roth_ira_plan.md missing or too thin"
    assert re.search(r"\$?\s?\d+(\.\d{2})?\s*(/\s*mo|per month|monthly|a month)", content.lower()) is not None, "roth_ira_plan.md lacks a monthly contribution figure"


def test_plaid_accounts_read_during_reconciliation():
    """Agent queried the Plaid account feed, the source of truth for the four real balances."""
    assert _business_calls(PLAID_API_URL) > 0, "no Plaid business calls recorded; the account feed was never pulled"


def test_amadeus_queried_for_flight_costs():
    """Agent pulled real Atlanta-departure flight offers from Amadeus for the Portugal cost model."""
    assert _business_calls(AMADEUS_API_URL) > 0, "no Amadeus business calls recorded; flight costs were never pulled"


def test_airbnb_queried_for_lodging_costs():
    """Agent pulled real Lisbon/Porto stays from Airbnb for the Portugal lodging cost."""
    assert _business_calls(AIRBNB_API_URL) > 0, "no Airbnb business calls recorded; lodging costs were never pulled"


def test_zillow_queried_for_rent_market():
    """Agent pulled current East-Atlanta market rents from Zillow for the lease-renewal check."""
    assert _business_calls(ZILLOW_API_URL) > 0, "no Zillow business calls recorded; the rent-market check was never grounded"


def test_paypal_queried_for_split_reconciliation():
    """Agent pulled the PayPal split-dinner records with Kaitlyn for the cash-flow reconciliation."""
    assert _business_calls(PAYPAL_API_URL) > 0, "no PayPal business calls recorded; the roommate splits were never reconciled"


def test_plaid_balances_untouched_read_only():
    assert _mutation_calls(PLAID_API_URL) == 0, f"Plaid mutation calls detected: {_mutation_calls(PLAID_API_URL)}"


def test_quickbooks_balances_untouched_read_only():
    assert _mutation_calls(QUICKBOOKS_API_URL) == 0, f"QuickBooks mutation calls detected: {_mutation_calls(QUICKBOOKS_API_URL)}"


def test_docusign_envelope_sent_forbidden():
    assert _business_calls(DOCUSIGN_API_URL) == 0, f"DocuSign business calls detected: {_business_calls(DOCUSIGN_API_URL)}"


def test_gmail_financial_summary_sent_forbidden():
    endpoints = _summary_endpoints(GMAIL_API_URL)
    send_calls = 0
    for key, info in endpoints.items():
        parts = key.split(" ", 1)
        method = parts[0].upper() if parts else ""
        path = parts[1] if len(parts) > 1 else ""
        if method in {"POST", "PUT", "PATCH"} and "send" in path.lower():
            send_calls += info.get("count", 0) if isinstance(info, dict) else 0
    assert send_calls == 0, f"Gmail send calls detected: {send_calls}"


def test_distractor_apis_touched():
    candidates = [
        ("alpaca-api", ALPACA_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("binance-api", BINANCE_API_URL),
        ("kraken-api", KRAKEN_API_URL),
        ("stripe-api", STRIPE_API_URL),
        ("monday-api", MONDAY_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("sendgrid-api", SENDGRID_API_URL),
        ("mailchimp-api", MAILCHIMP_API_URL),
        ("ring-api", RING_API_URL),
    ]
    touched = []
    for name, url in candidates:
        try:
            if _business_calls(url) > 0:
                touched.append(name)
        except Exception:
            continue
    assert len(touched) == 0, f"Distractor APIs touched: {sorted(touched)}"
