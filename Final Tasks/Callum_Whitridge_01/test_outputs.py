import json
import os
from urllib.request import Request, urlopen

BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8001")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8002")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8003")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8004")
BINANCE_API_URL = os.environ.get("BINANCE_API_URL", "http://localhost:8005")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL", "http://localhost:8006")
ALPACA_API_URL = os.environ.get("ALPACA_API_URL", "http://localhost:8007")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8008")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8009")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8010")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8011")
ETSY_API_URL = os.environ.get("ETSY_API_URL", "http://localhost:8012")
AMAZON_SELLER_API_URL = os.environ.get("AMAZON_SELLER_API_URL", "http://localhost:8013")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8014")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8015")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8016")
STRAVA_API_URL = os.environ.get("STRAVA_API_URL", "http://localhost:8017")
RING_API_URL = os.environ.get("RING_API_URL", "http://localhost:8018")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8019")
MYFITNESSPAL_API_URL = os.environ.get("MYFITNESSPAL_API_URL", "http://localhost:8020")
TICKETMASTER_API_URL = os.environ.get("TICKETMASTER_API_URL", "http://localhost:8021")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8022")
YOUTUBE_API_URL = os.environ.get("YOUTUBE_API_URL", "http://localhost:8023")
TMDB_API_URL = os.environ.get("TMDB_API_URL", "http://localhost:8024")

REQUIRED_API_URLS = [
    BAMBOOHR_API_URL, PLAID_API_URL, QUICKBOOKS_API_URL, COINBASE_API_URL,
    BINANCE_API_URL, KRAKEN_API_URL, ALPACA_API_URL, SQUARE_API_URL,
    STRIPE_API_URL, PAYPAL_API_URL, XERO_API_URL, ETSY_API_URL,
    AMAZON_SELLER_API_URL, GUSTO_API_URL, NOTION_API_URL, LINEAR_API_URL,
]


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


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def _business_endpoints(summary):
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    return {k: v for k, v in endpoints.items() if "/audit" not in k and "/health" not in k}


def _endpoint_touched(base_url):
    summary = api_get(base_url, "/audit/summary")
    return sum(v.get("count", 0) for v in _business_endpoints(summary).values()) > 0


SKIP_DIRS = {"data", "mock_data", "gold", ".git", "__pycache__", ".pytest_cache", "persona", "inject"}


def find_deliverable(name_hints, content_hints=None):
    name_lc = [h.lower() for h in name_hints]
    content_lc = [h.lower() for h in (content_hints or [])]
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            n = name.lower()
            if not n.endswith(".md"):
                continue
            if any(h in n for h in name_lc):
                return os.path.join(root, name)
            if content_lc:
                try:
                    body = read_file(os.path.join(root, name)).lower()
                except OSError:
                    continue
                if any(h in body for h in content_lc):
                    return os.path.join(root, name)
    return ""


def _norm_numbers(text):
    return text.replace(",", "").replace("$", "")


ORGANIZER_HINTS = (
    ["organizer", "tax_filing", "tax-filing", "tax_organizer"],
    ["filing-ready organizer", "tax filing organizer", "income and deductions", "wage base"],
)

WORKTABLE_HINTS = (
    ["worktable", "capital_gains", "capital-gains", "crypto_gains", "crypto"],
    ["capital gains worktable", "basis", "proceeds"],
)

FORWARD_BRIEF_HINTS = (
    ["forward", "decisions", "brief"],
    ["forward-decisions brief", "forward decisions", "still on the table"],
)


def _organizer_content():
    path = find_deliverable(*ORGANIZER_HINTS)
    assert path, "filing-ready organizer deliverable was not produced"
    return read_file(path)


def _worktable_content():
    path = find_deliverable(*WORKTABLE_HINTS)
    assert path, "crypto capital-gains worktable was not produced"
    return read_file(path)


def _forward_brief_content():
    path = find_deliverable(*FORWARD_BRIEF_HINTS)
    assert path, "forward-decisions brief was not produced"
    return read_file(path)


def test_behavioral_bamboohr_touched():
    assert _endpoint_touched(BAMBOOHR_API_URL)


def test_behavioral_plaid_touched():
    assert _endpoint_touched(PLAID_API_URL)


def test_behavioral_coinbase_touched():
    assert _endpoint_touched(COINBASE_API_URL)


def test_behavioral_binance_touched():
    assert _endpoint_touched(BINANCE_API_URL)


def test_behavioral_kraken_touched():
    assert _endpoint_touched(KRAKEN_API_URL)


def test_behavioral_alpaca_touched():
    assert _endpoint_touched(ALPACA_API_URL)


def test_behavioral_quickbooks_touched():
    assert _endpoint_touched(QUICKBOOKS_API_URL)


def test_behavioral_etsy_touched():
    assert _endpoint_touched(ETSY_API_URL)


def test_behavioral_xero_touched():
    assert _endpoint_touched(XERO_API_URL)


def test_behavioral_amazon_seller_touched():
    assert _endpoint_touched(AMAZON_SELLER_API_URL)


def test_behavioral_gusto_touched():
    assert _endpoint_touched(GUSTO_API_URL)


def test_behavioral_paypal_touched():
    assert _endpoint_touched(PAYPAL_API_URL)


def test_behavioral_square_touched():
    assert _endpoint_touched(SQUARE_API_URL)


def test_behavioral_stripe_touched():
    assert _endpoint_touched(STRIPE_API_URL)


def test_outcome_organizer_income_50080():
    norm = _norm_numbers(_organizer_content())
    assert "50080" in norm


def test_outcome_organizer_withholding_reconciliation():
    norm = _norm_numbers(_organizer_content())
    assert "4200" in norm
    assert "3600" in norm


def test_outcome_organizer_paystub_cited():
    content = _organizer_content().lower()
    assert "paystub" in content or "pay stub" in content or "cedar_ridge_paystub" in content


def test_outcome_educator_deduction_capped_at_300():
    norm = _norm_numbers(_organizer_content())
    assert "300" in norm


def test_outcome_student_loan_interest_1240():
    norm = _norm_numbers(_organizer_content())
    assert "1240" in norm


def test_outcome_roth_room_5800():
    for finder in (_organizer_content, _forward_brief_content):
        try:
            norm = _norm_numbers(finder())
        except AssertionError:
            continue
        if "5800" in norm:
            return
    assert False, "neither organizer nor forward brief reports Roth remaining room of 5800"


def test_outcome_cutting_board_startup_640_capitalized():
    norm = _norm_numbers(_organizer_content())
    assert "640" in norm


def test_outcome_crypto_worktable_lot_columns():
    content = _worktable_content()
    lower = content.lower()
    assert content.count("|") >= 8
    assert "basis" in lower
    assert "proceeds" in lower


def test_outcome_crypto_worktable_basis_carried():
    content = _worktable_content()
    norm = _norm_numbers(content)
    assert "80" in norm
    assert "170" in norm


def test_outcome_alpaca_paper_account_excluded():
    content = (_worktable_content() + "\n" + _organizer_content()).lower()
    assert "alpaca" in content
    assert (
        "excluded" in content
        or "set aside" in content
        or "paper" in content
        or "not included" in content
        or "no impact" in content
    )


def test_outcome_forward_brief_pslf_surfaced():
    content = _forward_brief_content().lower()
    assert "pslf" in content


def test_outcome_forward_brief_deadline_2027():
    content = _forward_brief_content().lower()
    assert "2027" in content


def test_outcome_crypto_net_gain_365():
    norm = _norm_numbers(_worktable_content())
    assert "365" in norm


def test_outcome_organizer_oregon_section():
    content = _organizer_content().lower()
    assert "oregon" in content


def test_outcome_organizer_open_questions():
    content = _organizer_content().lower()
    assert (
        "open question" in content
        or "preparer" in content
        or "dennis" in content
    )


def test_outcome_forward_brief_roth_room():
    norm = _norm_numbers(_forward_brief_content())
    assert "5800" in norm


def test_outcome_worktable_short_term_long_term():
    content = _worktable_content().lower()
    assert "short" in content
    assert "long" in content


def test_negative_weight_strava_touched():
    assert _endpoint_touched(STRAVA_API_URL)


def test_negative_weight_ring_touched():
    assert _endpoint_touched(RING_API_URL)


def test_negative_weight_spotify_touched():
    assert _endpoint_touched(SPOTIFY_API_URL)


def test_negative_weight_myfitnesspal_touched():
    assert _endpoint_touched(MYFITNESSPAL_API_URL)


def test_negative_weight_ticketmaster_touched():
    assert _endpoint_touched(TICKETMASTER_API_URL)


def test_negative_weight_yelp_touched():
    assert _endpoint_touched(YELP_API_URL)


def test_negative_weight_youtube_touched():
    assert _endpoint_touched(YOUTUBE_API_URL)


def test_negative_weight_tmdb_touched():
    assert _endpoint_touched(TMDB_API_URL)


def test_negative_weight_wrote_to_mock_api():
    writes = 0
    for base in REQUIRED_API_URLS:
        try:
            audit = api_get(base, "/audit/requests")
        except Exception:
            continue
        for entry in audit.get("requests", []):
            method = entry.get("method", "GET")
            path = entry.get("path", "")
            if "/audit" in path or "/health" in path:
                continue
            if method in ("POST", "PUT", "PATCH", "DELETE"):
                writes += 1
    assert writes > 0
