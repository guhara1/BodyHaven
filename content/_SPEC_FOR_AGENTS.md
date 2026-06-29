# 콘텐츠 모듈 작성 공통 규칙 (부천 출장마사지 · 간다GO)

당신은 정적 사이트의 Python 콘텐츠 모듈 1개를 작성합니다. 아래 규칙을 **반드시** 지키세요.
참고용으로 `content/districts.py`(완성된 구 페이지)와 `content/main.py`를 먼저 읽고 동일한 톤·구조·문장 밀도를 맞추세요.

## 파일 형식
- 파일 첫 줄: `from .components import page, faq_block, who_how_why, checklist, safety_note`
- 모듈 끝에 `PAGES = [...]` 리스트로 모든 페이지 dict을 export (또는 `PAGES.append(...)`).
- 절대 `build.py`나 `__init__.py`를 수정하지 마세요. 당신 파일만 만듭니다.

## page() 시그니처 (components.py)
```python
page(path, title, desc, h1, breadcrumb, body, *,
     hero_lead=None, hero_badge=None, hero_cta=None, hero_stats=None,
     hero_image=None, hero_alt=None, extra_head="", noindex=False)
```
- `path`: 앞 슬래시 없음, 끝 슬래시 있음. 예: `"bucheon/life/songnae/"`
- `desc`: **메타 설명, 한글 80자 이내 (초과 금지)**. 형식 예: `"송내 출장마사지·홈타이 예약 전 송내역, 인천 인접권 생활권을 확인하세요."`
- `h1`: 페이지 제목 (예: `"송내 생활권 출장마사지 안내"`). HTML 가능.
- `hero_lead`: 히어로 1~2문장 소개. 생략 시 desc 사용.
- `hero_badge`: 히어로 뱃지 텍스트 (예: `"송내 생활권 방문 관리 안내"`).
- `hero_alt`: 우측 4:3 이미지 alt. **자연스럽게**, "출장마사지" 단어 반복 금지. 예: `"부천 송내 생활권 방문형 관리 안내 이미지"`
- `breadcrumb`: `[("부천","/bucheon/"), ("생활권","/bucheon/life/songnae/"), ("송내","")]` 형태. 마지막 항목 href는 빈 문자열.
- `extra_head`: FAQ 스키마 head 문자열을 넣는 곳.

## faq_block 사용
```python
faq_html, faq_head = faq_block([(질문, 답변), ...], heading="자주 묻는 질문")
```
- 반환된 `faq_head`를 `extra_head=faq_head`로 전달, `faq_html`을 body 마지막에 삽입.
- 질문 3~5개. 답변은 페이지 고유 내용 기반(본문에 실제로 있는 내용).

## who_how_why / checklist / safety_note
- `who_how_why(who, how, why)` — 모든 색인 페이지 하단 필수.
  - who: "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다." (고정 문구 사용 가능)
  - how/why: 페이지 주제에 맞게 작성.
- `checklist(extra_lead=None)` — 지역/생활권/역/이용장소 페이지에 넣기.
- `safety_note()` — 개인정보·불법 서비스 불가 공통 안내. 지역 계열 페이지에 넣기.

## 본문 분량·품질
- **색인 페이지 본문(태그 제외 글자수) 2,000~2,600자.** 2,000자 미만이면 자동 noindex 되니 반드시 넘기세요.
- 섹션은 `<section><h2>제목</h2><p>...</p></section>` 구조. h2가 3개 이상이면 자동 목차 생성됨.
- 지역명만 바꾼 복제 금지. 각 페이지는 그 지역/주제의 실제 특성(노선·상권·주거·신도시·인접권·차량 이동 등)을 반영해 **서로 다르게** 작성.
- noindex 스텁 페이지는 400~900자로 짧게, `noindex=True` 지정. 상위 구/생활권으로 링크만 정확히 연결.

## 금지 표현 (절대 사용 금지)
최고, 1위, 무조건, 보장, 즉시 가능 보장, 무조건 저렴, 선정적 표현, 불법 서비스 암시, 가짜 후기, 가짜 평점, 과장된 가격 문구, **구체적 가격·요금 숫자(원)**, 키워드 스터핑, 순위 조작 문구.
- 가격/요금은 "예약 시 전화로 확인" 정도로만 안내하고 숫자 금액은 쓰지 않는다.

## 앵커텍스트 규칙
- 올바른 예: "중동·신중동 생활권 안내", "부천역 주변 예약 전 확인", "오피스텔 이용 전 확인", "불법·선정적 서비스 불가 안내"
- 금지 예: "부천 출장마사지 1위", "상동 출장마사지 바로 예약", "최고 홈타이"

## 내부링크 URL 맵 (정확히 이 경로로 링크)
구: `/bucheon/` (부천 홈), `/bucheon/wonmi-gu/`, `/bucheon/sosa-gu/`, `/bucheon/ojeong-gu/`

생활권 `/bucheon/life/<slug>/`:
bucheon-station-simgok(부천역·심곡), jungdong-sinjungdong(중동·신중동), sangdong-bucheon-cityhall(상동·부천시청), songnae(송내), yeokgok(역곡), sosa-sosabon(소사·소사본), beombak-okgil(범박·옥길), chunui-bucheon-stadium(춘의·부천종합운동장), kkachiwool-seonggok(까치울·성곡), wonjong-gogang(원종·고강), ojeong-sinheung(오정·신흥), jungdong-newtown(중동신도시), sangdong-newtown(상동신도시), seoul-adjacent(서울 인접권), incheon-adjacent(인천 인접권)

지하철역 `/bucheon/station/<slug>/`:
bucheon-station(부천역), jungdong-station(중동역), sinjungdong-station(신중동역), bucheon-cityhall-station(부천시청역), sangdong-station(상동역), songnae-station(송내역), yeokgok-station(역곡역), sosa-station(소사역·1·서해선 환승), bucheon-stadium-station(부천종합운동장역·7·서해선 환승), chunui-station(춘의역), kkachiwool-station(까치울역), wonjong-station(원종역)

이용 장소 `/bucheon/use/<slug>/`:
home(자택), hotel(호텔·숙소), officetel(오피스텔), station-area(역세권), night(야간), newtown(신도시), adjacent-area(서울·인천 인접권), outer-area(외곽)

예약 전 확인 `/bucheon/check/<slug>/`:
address(방문 주소), building-access(건물 출입 방식), travel-fee(추가 이동비), time(예약 가능 시간), change-policy(예약 변경), privacy(개인정보 처리 기준), service-policy(불법·선정적 서비스 불가), customer-notice(고객 유의사항)

운영 기준 `/bucheon/policy/<slug>/`:
privacy(개인정보 처리방침), service-policy(불법·선정적 서비스 불가 안내), content-standard(콘텐츠 작성 기준), authors(작성자·검수자 안내), sitemap(사이트맵)

행정동 `/bucheon/<gu>/<dong>/`:
- 원미구(wonmi-gu): jung-dong(중동), sang-dong(상동), chunui-dong(춘의동), simgok-1-dong, simgok-2-dong, yeokgok-1-dong, yeokgok-2-dong
- 소사구(sosa-gu): simgokbon-dong, sosabon-dong, songnae-1-dong, songnae-2-dong, beombak-dong, okgil-dong, goean-dong, yeokgok-3-dong
- 오정구(ojeong-gu): wonjong-1-dong, wonjong-2-dong, gogangbon-dong, gogang-1-dong, ojeong-dong, sinheung-dong, seonggok-dong

## 배경 지식 (정확히 반영)
- 부천 = 원미구·소사구·오정구 3개 구. 1호선·7호선·서해선이 지남.
- 원미구: 중동·신중동(7호선·상권·오피스텔), 상동·부천시청(신도시·부평 인접), 부천역·심곡(원도심·1호선), 춘의·부천종합운동장(환승), 역곡(서울 구로·온수 인접).
- 소사구: 부천역·심곡본(상권), 소사·소사본(1·서해선 환승), 송내(1호선·인천 부평 인접·주거), 범박·옥길(아파트 주거·차량 이동), 괴안·역곡3동(서울 인접).
- 오정구: 원종(서해선), 고강(서울 강서·김포공항 인접), 오정·신흥(산업·주거 혼합), 성곡·까치울(녹지·주거).
- 환승역(소사역·부천종합운동장역)도 노선별/출구별로 나누지 않고 역명 기준 1개 페이지.
- 실제 오프라인 매장 없음 → LocalBusiness 스키마 쓰지 않음(이미 build.py가 처리). 후기/평점 스키마 쓰지 않음.

## 빌드 검증
작성 후 `python3 build.py`를 실행해 당신 페이지들의 글자수가 2,000자 이상(index)으로 나오는지 확인하고, Python 에러가 없게 하세요. (단, __init__.py에 아직 등록 전이면 import 에러가 날 수 있으니, 문법 확인은 `python3 -c "import ast; ast.parse(open('content/<파일>.py').read())"`로 하세요.)
