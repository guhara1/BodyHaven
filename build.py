#!/usr/bin/env python3
"""부천 출장마사지(간다GO) — 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
  - 모든 페이지 상단에 우측 4:3 이미지를 가진 히어로 배너를 출력
  - 페이지별 WebPage / BreadcrumbList / Organization / (이미지 보유 시) ImageObject 스키마 자동 주입
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, NAV, PHONE, PHONE_DISPLAY,
                          AREA_SERVED, TELEGRAM, SITE_TAGLINE, DEFAULT_OG_IMAGE)

ROOT = os.path.dirname(os.path.abspath(__file__))
# Cloudflare Pages / GitHub Pages가 저장소 루트를 그대로 배포하므로
# 빌드 결과물을 저장소 루트에 직접 출력한다.
PUBLIC_DIR = ROOT
MIN_INDEX_CHARS = 2000


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자)."""
    text = re.sub(r"<[^>]+>", " ", body_html)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append('<li><a href="/bucheon/">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def _ld(obj: dict) -> str:
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )


def make_org_schema() -> dict:
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": base + "/#organization",
        "name": BRAND,
        "url": base + "/bucheon/",
        "logo": base + "/assets/apple-touch-icon.png",
        "image": base + DEFAULT_OG_IMAGE,
        "telephone": PHONE,
        "areaServed": {"@type": "AdministrativeArea", "name": AREA_SERVED},
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE,
            "contactType": "reservations",
            "availableLanguage": ["ko"],
            "areaServed": "KR",
        },
        "sameAs": [TELEGRAM],
    }


def make_breadcrumb_schema(crumbs) -> dict:
    base = BASE_URL.rstrip("/")
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": base + "/bucheon/",
    }]
    rest = crumbs[1:] if crumbs and crumbs[0][1] in ("/", "/bucheon/") else crumbs
    for i, (label, href) in enumerate(rest, start=2):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = base + href
        items.append(entry)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def make_webpage_schema(title: str, desc: str, canonical: str, image: str) -> dict:
    base = BASE_URL.rstrip("/")
    obj = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ko",
        "isPartOf": {"@id": base + "/#organization"},
        "publisher": {"@id": base + "/#organization"},
    }
    if image:
        obj["primaryImageOfPage"] = {"@type": "ImageObject", "url": base + image}
    return obj


def make_image_schema(image: str, alt: str, canonical: str) -> dict:
    """선호 썸네일 지정 — schema.org ImageObject (og:image와 함께 사용)."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "ImageObject",
        "contentUrl": base + image,
        "url": base + image,
        "caption": alt,
        "representativeOfPage": True,
        "width": 800,
        "height": 600,
    }


# 4:3 히어로 이미지가 아직 없을 때 쓰는 인라인 SVG 플레이스홀더(요청 시 실제 이미지로 교체).
def _placeholder_svg(label: str) -> str:
    safe = html.escape(label)
    return (
        '<div class="hero-figure hero-figure--placeholder" role="img" '
        f'aria-label="{safe} 대표 이미지 준비 중">'
        '<span class="hero-figure-mark">간다GO</span>'
        f'<span class="hero-figure-caption">{safe}</span>'
        '</div>'
    )


def render_hero(page) -> str:
    h1 = page["h1"]
    badge = page.get("hero_badge", SITE_TAGLINE)
    lead = page.get("hero_lead") or page["desc"]
    ctas = page.get("hero_cta") or []
    stats = page.get("hero_stats") or []
    image = page.get("hero_image")
    alt = page.get("hero_alt") or (re.sub(r"<[^>]+>", "", h1) + " 안내 이미지")

    cta_html = ""
    if ctas:
        btns = "".join(
            f'<a href="{href}" class="btn {cls}">{label}</a>'
            for label, href, cls in (
                (c[0], c[1], c[2] if len(c) > 2 else "btn-secondary") for c in ctas
            )
        )
        cta_html = f'<div class="hero-cta">{btns}</div>'

    stats_html = ""
    if stats:
        cells = "".join(
            f'<div class="stat"><div class="stat-number">{n}</div>'
            f'<div class="stat-label">{l}</div></div>'
            for n, l in stats
        )
        stats_html = f'<div class="hero-stats">{cells}</div>'

    if image:
        figure = (
            '<figure class="hero-figure">'
            f'<img src="{image}" alt="{html.escape(alt)}" width="800" height="600" '
            'loading="eager" decoding="async">'
            '</figure>'
        )
    else:
        clean = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h1)).strip()
        figure = _placeholder_svg(clean)

    return (
        '<section class="hero">'
        '<div class="hero-overlay" aria-hidden="true"></div>'
        '<div class="hero-inner container">'
        '<div class="hero-content">'
        f'<div class="hero-badge">{badge}</div>'
        f'<h1 class="hero-title">{h1}</h1>'
        f'<p class="hero-lead">{lead}</p>'
        f'{cta_html}'
        '</div>'
        '<div class="hero-media">'
        f'{figure}'
        '</div>'
        '</div>'
        f'{stats_html}'
        '</section>'
    )


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    image = page.get("hero_image")
    alt = page.get("hero_alt") or (re.sub(r"<[^>]+>", "", page["h1"]) + " 안내 이미지")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE_URL.rstrip("/") + "/" + path
    og_image = BASE_URL.rstrip("/") + (image or DEFAULT_OG_IMAGE)

    hero_html = render_hero(page)

    body, toc_items = inject_toc(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    # 스키마 자동 주입.
    blocks = [
        make_org_schema(),
        make_webpage_schema(title, desc, canonical, image),
    ]
    if crumbs:
        blocks.append(make_breadcrumb_schema(crumbs))
    if image:
        blocks.append(make_image_schema(image, alt, canonical))
    auto_schema = "".join(_ld(b) for b in blocks)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg?v=1">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v=1">
<meta name="theme-color" content="#0a0a0f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<link rel="stylesheet" href="/assets/style.css">
{auto_schema}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="/bucheon/"><span class="brand-mark">G</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> {SITE_TAGLINE} <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">예약전화</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{hero_html}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {body}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">부천시 전지역(원미구·소사구·오정구) 방문형 관리 서비스 안내 사이트입니다. 모든 안내는 위생·안전 기준과 건전한 관리 범위 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">전화예약</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 경기도 부천시 전지역</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="지역 안내">
      <p class="footer-title">지역 안내</p>
      <ul>
        <li><a href="/bucheon/">부천 홈</a></li>
        <li><a href="/bucheon/wonmi-gu/">원미구 안내</a></li>
        <li><a href="/bucheon/sosa-gu/">소사구 안내</a></li>
        <li><a href="/bucheon/ojeong-gu/">오정구 안내</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/bucheon/life/jungdong-sinjungdong/">생활권 안내</a></li>
        <li><a href="/bucheon/station/bucheon-station/">지하철역 안내</a></li>
        <li><a href="/bucheon/use/home/">이용 장소 안내</a></li>
        <li><a href="/bucheon/check/address/">예약 전 확인</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="운영 기준">
      <p class="footer-title">운영 기준</p>
      <ul>
        <li><a href="/bucheon/policy/privacy/">개인정보 처리방침</a></li>
        <li><a href="/bucheon/policy/service-policy/">불법·선정적 서비스 불가 안내</a></li>
        <li><a href="/bucheon/policy/authors/">작성자·검수자 안내</a></li>
        <li><a href="/bucheon/policy/sitemap/">사이트맵</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
      <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법·선정적 요청에는 어떤 경우에도 응하지 않습니다.</p>
      <div class="footer-actions">
        <a class="btn-telegram" href="{TELEGRAM}" target="_blank" rel="noopener nofollow" title="웹사이트 제작문의">📱 웹사이트 제작문의</a>
        <a class="btn-partnership" href="{TELEGRAM}" target="_blank" rel="noopener nofollow" title="제휴문의">🤝 제휴문의</a>
      </div>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">예약 전화</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


def build() -> None:
    report = []
    sitemap_urls = []

    os.makedirs(PUBLIC_DIR, exist_ok=True)
    seen = set()

    for page in PAGES:
        path = page["path"]
        if path in seen:
            raise SystemExit(f"중복 경로: {path}")
        seen.add(path)
        out_dir = os.path.join(PUBLIC_DIR, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        if not noindex:
            sitemap_urls.append(BASE_URL.rstrip("/") + "/" + path)
        report.append((path or "/", chars, "noindex" if noindex else "index"))

    urls = "\n".join(f"  <url><loc>{u}</loc></url>" for u in sitemap_urls)
    with open(os.path.join(PUBLIC_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )

    with open(os.path.join(PUBLIC_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {BASE_URL.rstrip('/')}/sitemap.xml\n"
        )

    open(os.path.join(PUBLIC_DIR, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS")
    for p, c, r in sorted(report):
        flag = "" if (r == "noindex" or MIN_INDEX_CHARS <= c <= 2600) else "  <-- 글자수 확인"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r}{flag}")
    idx = sum(1 for _, _, r in report if r == "index")
    print(f"\n{len(report)} pages built, {idx} indexed ({len(report)-idx} noindex).")


if __name__ == "__main__":
    build()
