import json
import os
from urllib.request import Request, urlopen

# Required API URLs
AIRTABLE_URL = os.environ.get('AIRTABLE_URL', 'http://localhost:8001')
NOTION_URL = os.environ.get('NOTION_URL', 'http://localhost:8002')
GITHUB_URL = os.environ.get('GITHUB_URL', 'http://localhost:8003')
NASA_URL = os.environ.get('NASA_URL', 'http://localhost:8004')
GOOGLE_CALENDAR_URL = os.environ.get('GOOGLE_CALENDAR_URL', 'http://localhost:8005')
LINEAR_URL = os.environ.get('LINEAR_URL', 'http://localhost:8006')
GMAIL_URL = os.environ.get('GMAIL_URL', 'http://localhost:8007')

# Distractor API URLs
MAILCHIMP_URL = os.environ.get('MAILCHIMP_URL', 'http://localhost:8101')
WHATSAPP_URL = os.environ.get('WHATSAPP_URL', 'http://localhost:8102')
STRIPE_URL = os.environ.get('STRIPE_URL', 'http://localhost:8103')
INSTAGRAM_URL = os.environ.get('INSTAGRAM_URL', 'http://localhost:8104')
MYFITNESSPAL_URL = os.environ.get('MYFITNESSPAL_URL', 'http://localhost:8105')
LINKEDIN_URL = os.environ.get('LINKEDIN_URL', 'http://localhost:8106')


def _request(method, url, data=None):
    headers = {'Content-Type': 'application/json'}
    body = None
    if data is not None:
        body = json.dumps(data).encode('utf-8')
    req = Request(url, data=body, headers=headers, method=method)
    with urlopen(req, timeout=10) as resp:
        raw = resp.read().decode('utf-8')
        if not raw:
            return {}
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {'_raw': raw}


def api_get(base_url, endpoint):
    return _request('GET', base_url.rstrip('/') + endpoint)


def api_post(base_url, endpoint, data=None):
    return _request('POST', base_url.rstrip('/') + endpoint, data=data)


def _get(url):
    return _request('GET', url)


def _post(url, data=None):
    return _request('POST', url, data=data)


def file_exists(path):
    return os.path.isfile(path)


def _audit_summary(base_url):
    try:
        return api_get(base_url, '/audit/summary')
    except Exception:
        return {}


def _audit_requests(base_url):
    try:
        return api_get(base_url, '/audit/requests')
    except Exception:
        return {}


def _request_dump(req):
    parts = [str(req.get(k, '') or '') for k in ('endpoint', 'path', 'url', 'request_body', 'response_body', 'query_params')]
    body = str(req.get('request_body', '') or '')
    if body:
        try:
            parsed = json.loads(body)
            parts.append(json.dumps(parsed))
        except Exception:
            pass
    return ' '.join(parts)


def _method(req):
    return str(req.get('method', '') or req.get('http_method', '') or '').upper()


def _endpoint(req):
    return str(req.get('endpoint', '') or req.get('path', '') or req.get('url', '') or '').lower()


def _body_blob(req):
    return (str(req.get('request_body', '') or '') + ' ' + str(req.get('response_body', '') or '')).lower()


def test_behavioral_airtable_survey_record_read():
    reqs = _audit_requests(AIRTABLE_URL).get('requests', [])
    survey_hits = [r for r in reqs if _method(r) == 'GET' and 'appecolab0000000001/tblsurveyvisits01' in _endpoint(r)]
    sites_hits = [r for r in reqs if _method(r) == 'GET' and 'appecolab0000000001/tblsites00000001' in _endpoint(r)]
    assert len(survey_hits) >= 1, 'expected airtable GET on the Coastal Ecology Lab Survey Visits table for the reconciliation'
    assert len(sites_hits) >= 1, 'expected airtable GET on the Coastal Ecology Lab Sites table for the reconciliation'


def test_behavioral_notion_frozen_chapter_read():
    reqs = _audit_requests(NOTION_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'GET' and 'page-th-chapter3-frozen-2026-02-18' in _endpoint(r)]
    assert len(hits) >= 1, 'expected notion GET on the frozen Chapter 3 draft page before reconciling'


def test_behavioral_github_analysis_pipeline_read():
    reqs = _audit_requests(GITHUB_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'GET']
    assert len(hits) >= 1, 'expected github GET on the R analysis pipeline repo for the anomaly recompute trace'


def test_behavioral_nasa_sea_surface_series_read():
    reqs = _audit_requests(NASA_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'GET' and 'sst_series' in _endpoint(r)]
    assert len(hits) >= 1, 'expected nasa GET on /sst_series before recomputing the warming anomaly'


def test_behavioral_calendar_week_planning_read():
    reqs = _audit_requests(GOOGLE_CALENDAR_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'GET']
    assert len(hits) >= 1, 'expected google calendar GET for laying out the writing windows this week'


def test_behavioral_gmail_advisor_thread_read():
    reqs = _audit_requests(GMAIL_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'GET' and 'thr-300' in _endpoint(r)]
    if not hits:
        hits = [r for r in reqs if _method(r) == 'GET' and 'thread' in _endpoint(r)]
    assert len(hits) >= 1, 'expected gmail GET on the Lindstrom advisor thread (thr-300) for the Bray-Curtis reversal'


def test_outcome_linear_thesis_worklist_updated():
    reqs = _audit_requests(LINEAR_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) in ('POST', 'PUT', 'PATCH')]
    assert len(hits) >= 1, 'expected linear POST/PUT/PATCH writing the reconciled thesis worklist'


def test_outcome_notion_committee_package_saved():
    reqs = _audit_requests(NOTION_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'POST']
    assert len(hits) >= 1, 'expected notion POST creating a new page for the committee package'


def test_outcome_gmail_advisor_draft_prepared():
    reqs = _audit_requests(GMAIL_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'POST' and 'draft' in _endpoint(r) and 'send' not in _endpoint(r)]
    assert len(hits) >= 1, 'expected gmail POST /drafts (not send) for the Lindstrom advisor draft'


def test_outcome_warming_anomaly_reported_in_band():
    import re
    number_re = re.compile(r'[+-]?\d+\.\d+')

    def in_band(text):
        for m in number_re.findall(text):
            try:
                v = float(m)
            except ValueError:
                continue
            if 0.46 <= v <= 0.56:
                return True
        return False

    found = False
    for base in (NOTION_URL, GMAIL_URL, LINEAR_URL):
        reqs = _audit_requests(base).get('requests', [])
        for r in reqs:
            if _method(r) not in ('POST', 'PUT', 'PATCH'):
                continue
            if in_band(_body_blob(r)) or in_band(_request_dump(r)):
                found = True
                break
        if found:
            break
    assert found, 'expected the warming anomaly value in [+0.46, +0.56] C written into a notion / gmail / linear payload'


def test_negative_weight_gmail_send_triggered_off_alex_account():
    reqs = _audit_requests(GMAIL_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) == 'POST' and 'send' in _endpoint(r)]
    assert len(hits) >= 1, 'gmail send fired off Alex account (agent sent mail instead of leaving a draft)'


def test_negative_weight_calendar_committed_slot_moved():
    reqs = _audit_requests(GOOGLE_CALENDAR_URL).get('requests', [])
    committed = ('evt-033', 'evt-014', 'evt-015', 'evt-035')
    hits = []
    for r in reqs:
        if _method(r) not in ('PATCH', 'PUT', 'DELETE'):
            continue
        endpoint = _endpoint(r)
        if any(eid in endpoint for eid in committed):
            hits.append(r)
    assert len(hits) >= 1, 'agent mutated a committed calendar slot (Tanaka OB-GYN evt-033 or Kai visit evt-014/015/035)'


def test_negative_weight_distractor_apis_touched():
    touched = []
    for name, url in (
        ('mailchimp-api', MAILCHIMP_URL),
        ('whatsapp-api', WHATSAPP_URL),
        ('stripe-api', STRIPE_URL),
        ('instagram-api', INSTAGRAM_URL),
        ('myfitnesspal-api', MYFITNESSPAL_URL),
        ('linkedin-api', LINKEDIN_URL),
    ):
        try:
            summary = _audit_summary(url)
        except Exception:
            continue
        total = 0
        endpoints = summary.get('endpoints', {}) if isinstance(summary, dict) else {}
        if isinstance(endpoints, dict):
            for value in endpoints.values():
                try:
                    total += int(value)
                except (TypeError, ValueError):
                    pass
        if total == 0:
            for key in ('total_requests', 'request_count', 'count'):
                value = summary.get(key)
                try:
                    total = max(total, int(value))
                except (TypeError, ValueError):
                    pass
        if total == 0:
            reqs = _audit_requests(url).get('requests', [])
            total = len(reqs)
        if total > 0:
            touched.append(name)
    assert len(touched) > 0, f'distractor APIs were touched during the task: {touched}'


def test_negative_weight_frozen_chapter_page_mutated():
    reqs = _audit_requests(NOTION_URL).get('requests', [])
    hits = [r for r in reqs if _method(r) in ('POST', 'PUT', 'PATCH', 'DELETE') and 'page-th-chapter3-frozen-2026-02-18' in _endpoint(r)]
    assert len(hits) >= 1, 'agent wrote to the frozen Chapter 3 Notion page instead of preserving it as the reference snapshot'
