# 부천 출장마사지 — 간다GO

경기도 부천시 전지역(원미구·소사구·오정구) 방문형 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.

- **상호**: 간다GO
- **전화예약**: 0508-202-4719
- **문의(텔레그램)**: 웹사이트 제작문의 · 제휴문의 (푸터 오렌지 버튼)

## 구조

정적 HTML 사이트입니다. `build.py` + `content/` 의 페이지 정의로 정적 HTML을 생성하며, 어떤 호스팅(Cloudflare Pages, GitHub Pages, 일반 웹서버)에서든 저장소 루트를 그대로 서빙할 수 있습니다.

```
build.py                 # 빌드 스크립트 (히어로·스키마·sitemap·robots 자동 생성)
content/
  site.py                # 상호·전화·도메인·상단 메뉴(NAV)·텔레그램
  components.py          # 공통 컴포넌트: page(), faq_block(), who_how_why(), checklist(), safety_note()
  __init__.py            # PAGES 조립
  root.py                # 루트(/) → /bucheon/ 리다이렉트
  main.py                # 부천 메인 (/bucheon/)
  districts.py           # 구별: 원미구·소사구·오정구
  life_areas.py          # 생활권 페이지
  stations.py            # 지하철역(역세권) 페이지
  admin_wonmi.py         # 원미구 행정동
  admin_sosa.py          # 소사구 행정동
  admin_ojeong.py        # 오정구 행정동
  use_cases.py           # 이용 장소 (자택·호텔·오피스텔·역세권·야간·신도시·인접권·외곽)
  checks.py              # 예약 전 확인사항
  policies.py            # 운영 기준 (개인정보·서비스 기준·콘텐츠 기준·작성자·사이트맵)
assets/
  style.css              # 프리미엄 팔레트(옵시디언+샴페인 골드) + 오렌지 액션 + Pretendard
  nav.js                 # 모바일 네비게이션
  favicon.svg
  img/                   # 히어로 4:3 이미지 (요청 시 추가)
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 index/noindex 리포트가 출력됩니다.

## 디자인

- **프리미엄 팔레트로 토큰 교체**: 기존 다크 네이비 → **옵시디언(#07070b) + 샴페인 골드(#c9a55c)**. 헤딩·브랜드·하이라인은 골드, **CTA·전화·푸터 버튼은 오렌지(#FF6B35)** 유지.
- **컴포넌트 오버레이**: 히어로 노이즈/그라데이션 오버레이, 글래스 카드, 골드 헤어라인 보더, 카드 상단 골드 슬라이드, Who·How·Why 카드.
- **모든 페이지 히어로 우측 4:3 이미지**: 두 컬럼 히어로. 이미지가 없으면 골드 플레이스홀더가 표시됩니다.
- **Pretendard** 본문 + Noto Serif KR 헤딩.

## 히어로 이미지 추가 방법 (4:3)

이미지는 `assets/img/` 에 넣고, 각 페이지 정의에서 `hero_image="/assets/img/파일명.jpg"` 와 `hero_alt="..."` 를 지정하면 됩니다 (4:3 비율 권장, 800×600 이상). 지정 전에는 플레이스홀더가 자동 노출됩니다. `assets/og-image.png`(1200×630)를 추가하면 공유 미리보기 이미지가 적용됩니다.

## SEO 운영 원칙 (Google 가이드라인 반영)

- **E-E-A-T / Who·How·Why**: 모든 주요 페이지 하단에 작성자·검수자 박스와 Who·How·Why 블록.
- **본문 2,000자 미만 자동 noindex**: 사이트 단위 품질 저하(도움되는 콘텐츠 시스템) 방지. 번호동 등 중복 위험 행정동은 DB 보관 + noindex 스텁.
- **환승역 1개 URL**: 소사역·부천종합운동장역도 노선별/출구별로 나누지 않음. 도어웨이 페이지 금지.
- **구조화 데이터**: Organization, WebPage(+primaryImageOfPage), BreadcrumbList, FAQPage, ImageObject(선호 썸네일) 자동 주입. 매장 없음 → LocalBusiness 미사용, 후기/평점 스키마 미사용.
- **내부링크**: 부천 메인 → 구 → 행정동 → 생활권 → 역세권 → 이용 장소 → 예약 전 확인 으로 상호 연결. 앵커텍스트는 키워드 나열이 아닌 지역·기능 설명형.
- **선호 이미지 지정**: og:image + schema.org ImageObject 동시 사용.

## 배포 전 할 일

1. `content/site.py` 의 `BASE_URL` 을 실제 도메인으로 변경
2. `assets/img/` 에 히어로 4:3 이미지, `assets/og-image.png` 추가 후 페이지별 `hero_image` 지정
3. `python3 build.py` 재실행
4. Google Search Console 에 `sitemap.xml` 제출
