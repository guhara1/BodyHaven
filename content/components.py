# 공통 컴포넌트 — 모든 콘텐츠 모듈에서 재사용
# (작성자/검수자 박스, Who·How·Why 블록, FAQ + FAQPage 스키마, 예약 전 체크리스트)
import json
from .site import BRAND, PHONE, AREA_SERVED

AUTHOR = "부천 지역 안내 콘텐츠 담당자"
REVIEWER = "콘텐츠 품질 검수 담당자 / 운영 책임자"


def page(path, title, desc, h1, breadcrumb, body, *,
         hero_lead=None, hero_badge=None, hero_cta=None, hero_stats=None,
         hero_image=None, hero_alt=None, extra_head="", noindex=False):
    """페이지 dict 생성기. build.py의 render_page 계약을 따른다."""
    p = {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body,
    }
    if hero_lead: p["hero_lead"] = hero_lead
    if hero_badge: p["hero_badge"] = hero_badge
    if hero_cta: p["hero_cta"] = hero_cta
    if hero_stats: p["hero_stats"] = hero_stats
    if hero_image: p["hero_image"] = hero_image
    if hero_alt: p["hero_alt"] = hero_alt
    if extra_head: p["extra_head"] = extra_head
    if noindex: p["noindex"] = True
    return p


def who_how_why(who: str, how: str, why: str) -> str:
    """모든 주요 페이지 하단 Who·How·Why 블록 (E-E-A-T 신호)."""
    return f"""
<section class="whw">
<h2>Who · How · Why</h2>
<div class="whw-grid">
  <div class="whw-card"><h3>Who</h3><p>{who}</p></div>
  <div class="whw-card"><h3>How</h3><p>{how}</p></div>
  <div class="whw-card"><h3>Why</h3><p>{why}</p></div>
</div>
<p class="author-box">작성: {AUTHOR} · 검수: {REVIEWER} · 작성 기준은 <a href="/policy/authors/">작성자·검수자 안내</a>에서 확인할 수 있습니다.</p>
</section>"""


def faq_block(items, heading="자주 묻는 질문"):
    """FAQ HTML + FAQPage 스키마 head 문자열을 함께 반환한다.
    items: [(question, answer), ...]"""
    dts = []
    for i, (q, a) in enumerate(items, 1):
        dts.append(f'<dt id="faq-{i}">{q}</dt><dd>{a}</dd>')
    body = (
        f'<section id="faq"><h2>{heading}</h2>'
        f'<dl class="faq-list">{"".join(dts)}</dl></section>'
    )
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }
    head = (
        '<script type="application/ld+json">\n'
        + json.dumps(schema, ensure_ascii=False, indent=2)
        + "\n</script>"
    )
    return body, head


# 기본 예약 전 체크리스트(공통). 페이지별로 앞뒤 항목을 더해 차별화한다.
def checklist(extra_lead=None, items=None) -> str:
    base = items or [
        "방문 주소(동·건물 유형)를 정확히 확인했나요?",
        "원미구·소사구·오정구 중 어느 구인지 확인했나요?",
        "가까운 행정동과 생활권을 확인했나요?",
        "가까운 지하철역과 출입 동선을 확인했나요?",
        "공동현관·엘리베이터 등 건물 출입 방식을 확인했나요?",
        "예약 가능 시간과 야간 가능 여부를 확인했나요?",
        "추가 이동비 발생 여부를 확인했나요?",
        "개인정보 처리 기준을 확인했나요?",
        "불법·선정적 서비스 불가 안내를 확인했나요?",
    ]
    lis = "".join(f"<li>{x}</li>" for x in base)
    lead = f"<p>{extra_lead}</p>" if extra_lead else ""
    return (
        '<section id="checklist"><h2>예약 전 체크리스트</h2>'
        f'{lead}<ul class="checklist">{lis}</ul>'
        '<p>항목별 자세한 기준은 <a href="/check/address/">방문 주소 확인</a>, '
        '<a href="/check/building-access/">건물 출입 방식</a>, '
        '<a href="/check/travel-fee/">추가 이동비 기준</a> 페이지에서 확인하세요.</p>'
        '</section>'
    )


def safety_note() -> str:
    """개인정보·불법 서비스 불가 공통 안내(스팸/YMYL 신뢰 신호)."""
    return (
        '<section id="safety"><h2>개인정보·서비스 운영 기준</h2>'
        '<p>예약 확인과 연락에 필요한 최소한의 정보만 안내하며, 자세한 내용은 '
        '<a href="/policy/privacy/">개인정보 처리방침</a>에서 확인할 수 있습니다. '
        f'{BRAND}는 건전한 방문 관리 서비스만 안내하며, '
        '<a href="/policy/service-policy/">불법·선정적 서비스</a>는 제공하거나 알선하지 않습니다.</p>'
        f'<p>예약·상담 문의: <a href="tel:{PHONE}">{PHONE}</a> (연중무휴 24시간, {AREA_SERVED} 전지역)</p>'
        '</section>'
    )
