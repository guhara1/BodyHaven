# 부천 메인 페이지 (/)
from .components import page, faq_block, who_how_why

DESC = "부천 출장마사지·홈타이 예약 전 원미구·소사구·오정구, 중동·상동·부천역 생활권을 확인하세요."

_FAQ = [
    ("부천 전 지역 방문이 가능한가요?",
     "실제 방문 주소, 가까운 생활권, 예약 가능 시간, 이동 기준을 확인한 뒤 원미구·소사구·오정구 전 지역으로 안내합니다. 자택·호텔·오피스텔 등 장소별 확인사항이 다르므로 예약 전 확인하는 것이 좋습니다."),
    ("원미구, 소사구, 오정구를 나누어 봐야 하나요?",
     "부천은 3개 구와 37개 행정동 구조이므로 구와 행정동, 생활권을 함께 확인하면 방문 주소와 이동 시간을 더 정확히 안내받을 수 있습니다."),
    ("지하철역 기준으로도 찾을 수 있나요?",
     "1호선·7호선·서해선 역명은 위치 설명에 도움이 됩니다. 다만 실제 방문 가능 여부는 주소와 건물 출입 방식까지 함께 확인해야 합니다."),
    ("소사역이나 부천종합운동장역은 노선별 페이지를 따로 만드나요?",
     "아니요. 환승역도 역명 기준 1개 안내 페이지로 관리해 중복 페이지를 줄입니다. 출구별 페이지도 만들지 않습니다."),
    ("불법·선정적 서비스도 가능한가요?",
     "불법·선정적 서비스는 제공하거나 안내하지 않습니다. 간다GO는 위생·안전 기준 안에서 건전한 방문 관리 서비스만 안내합니다."),
]

_faq_html, _faq_head = faq_block(_FAQ, heading="부천 출장마사지 자주 묻는 질문")

PAGE = page(
    path="",
    title="부천 출장마사지｜원미·소사·오정 생활권 홈타이 지역 안내",
    desc=DESC,
    h1='부천 출장마사지<br><span class="hero-accent">구별·생활권·지하철역별 안내</span>',
    hero_badge="부천시 전지역 방문 관리 · 24시간 상담",
    hero_lead="원미구·소사구·오정구와 중동, 상동, 부천역, 신중동, 송내, 역곡, 소사, 원종 등 부천 주요 생활권·지하철역별 예약 전 확인사항을 안내합니다.",
    hero_cta=[
        ("구별 안내 보기", "#districts", "btn-primary"),
        ("생활권 보기", "#life", "btn-secondary"),
        ("지하철역 보기", "#stations", "btn-secondary"),
        ("예약 전 확인", "/check/address/", "btn-secondary"),
    ],
    hero_stats=[("3", "구별 안내"), ("37", "행정동"), ("12", "지하철역"), ("24H", "상담 가능")],
    hero_image=None,
    hero_alt="부천 원미·소사·오정 생활권 방문형 관리 안내 이미지",
    breadcrumb=[],
    extra_head=_faq_head,
    body=f"""
<section id="criteria">
<h2>부천은 구·동·역세권을 함께 봐야 합니다</h2>
<p>부천시는 면적이 크지 않지만 서울과 인천 사이에 자리해 1호선·7호선·서해선 생활권이 함께 연결되는 지역입니다. 행정구역은 <a href="/wonmi-gu/">원미구</a>, <a href="/sosa-gu/">소사구</a>, <a href="/ojeong-gu/">오정구</a> 3개 구로 운영되지만, 실제 이용자는 구 이름보다 중동, 상동, 부천역, 송내, 역곡, 소사, 원종 같은 생활권 이름으로 위치를 찾는 경우가 많습니다.</p>
<p>그래서 부천에서 방문형 관리를 예약하기 전에는 자신의 위치가 어느 구의 어느 행정동·생활권에 해당하는지, 가까운 지하철역이 어디인지를 함께 확인하는 것이 가장 정확합니다. 부천은 환승역과 노선이 겹치는 구간이 있어 출구별·노선별로 페이지를 나누면 정보가 오히려 흩어지므로, 이 사이트는 역명 기준 한 개의 안내 페이지로 정리했습니다.</p>
</section>

<section id="districts">
<h2>부천 3개 구 안내</h2>
<div class="card-grid">
  <a href="/wonmi-gu/" class="card"><h3>원미구</h3><p>중동·상동·신중동·춘의·부천종합운동장·역곡 생활권 중심</p><span class="card-arrow">→</span></a>
  <a href="/sosa-gu/" class="card"><h3>소사구</h3><p>부천역·심곡본·소사본·송내·범박·옥길·괴안 생활권 중심</p><span class="card-arrow">→</span></a>
  <a href="/ojeong-gu/" class="card"><h3>오정구</h3><p>원종·고강·오정·신흥·성곡·까치울 생활권과 차량 이동 기준</p><span class="card-arrow">→</span></a>
</div>
</section>

<section id="life">
<h2>부천 주요 생활권</h2>
<p>지역과 역을 연결한 생활권 기준으로 확인하면 방문 주소와 이동 시간을 더 정확히 안내받을 수 있습니다.</p>
<div class="card-grid">
  <a href="/life/bucheon-station-simgok/" class="card"><h3>부천역·심곡</h3><p>원도심·1호선·상권 중심</p></a>
  <a href="/life/jungdong-sinjungdong/" class="card"><h3>중동·신중동</h3><p>7호선·상권·오피스텔 중심</p></a>
  <a href="/life/sangdong-bucheon-cityhall/" class="card"><h3>상동·부천시청</h3><p>신도시·상권·부평 인접권</p></a>
  <a href="/life/songnae/" class="card"><h3>송내</h3><p>1호선·인천 인접권·주거지</p></a>
  <a href="/life/yeokgok/" class="card"><h3>역곡</h3><p>서울 구로·온수 인접권</p></a>
  <a href="/life/sosa-sosabon/" class="card"><h3>소사·소사본</h3><p>1호선·서해선 환승 생활권</p></a>
  <a href="/life/wonjong-gogang/" class="card"><h3>원종·고강</h3><p>서해선·서울 강서 인접권</p></a>
  <a href="/life/ojeong-sinheung/" class="card"><h3>오정·신흥</h3><p>산업·주거 혼합 생활권</p></a>
</div>
</section>

<section id="stations">
<h2>부천 지하철역 기준으로 찾기</h2>
<p>1호선·7호선·서해선 주요 역별 인접 지역과 예약 기준을 안내합니다. 환승역도 역명 기준 한 개 페이지로 관리합니다.</p>
<div class="card-grid">
  <a href="/station/bucheon-station/" class="card"><h3>부천역</h3><p>심곡·원미 1호선 상권</p></a>
  <a href="/station/jungdong-station/" class="card"><h3>중동역</h3><p>중동·1호선 생활권</p></a>
  <a href="/station/sinjungdong-station/" class="card"><h3>신중동역</h3><p>중동·신중동 7호선 상권</p></a>
  <a href="/station/bucheon-cityhall-station/" class="card"><h3>부천시청역</h3><p>상동·중동 7호선 중심</p></a>
  <a href="/station/sangdong-station/" class="card"><h3>상동역</h3><p>상동신도시·부평 인접</p></a>
  <a href="/station/songnae-station/" class="card"><h3>송내역</h3><p>송내·1호선 인천 인접</p></a>
  <a href="/station/yeokgok-station/" class="card"><h3>역곡역</h3><p>역곡·1호선 서울 인접</p></a>
  <a href="/station/sosa-station/" class="card"><h3>소사역</h3><p>소사·1호선·서해선 환승</p></a>
</div>
</section>

<section id="use">
<h2>이용 장소에 따라 확인할 내용이 다릅니다</h2>
<div class="card-grid">
  <a href="/use/home/" class="card"><h3>자택 이용</h3><p>주소·공동현관·주차 확인</p></a>
  <a href="/use/hotel/" class="card"><h3>호텔·숙소</h3><p>객실 출입·숙소 정책 확인</p></a>
  <a href="/use/officetel/" class="card"><h3>오피스텔</h3><p>관리 규정·방문 시간 확인</p></a>
  <a href="/use/station-area/" class="card"><h3>역세권</h3><p>역 출입 동선·건물 확인</p></a>
  <a href="/use/night/" class="card"><h3>야간 예약</h3><p>야간 가능 시간·동선 확인</p></a>
  <a href="/use/adjacent-area/" class="card"><h3>서울·인천 인접권</h3><p>이동 기준 사전 확인</p></a>
</div>
</section>

<section id="check">
<h2>예약 전 확인해야 할 내용</h2>
<p>부천은 구·행정동·생활권·지하철역이 촘촘하게 얽혀 있어, 같은 동이라도 건물 유형과 이동 동선이 다를 수 있습니다. 예약을 진행하기 전에 아래 항목을 먼저 확인하면 방문 주소와 이동 시간 안내가 훨씬 정확해집니다.</p>
<ul>
<li><a href="/check/address/">방문 주소 확인</a> — 동·건물 유형과 정확한 주소</li>
<li><a href="/check/building-access/">건물 출입 방식</a> — 공동현관·엘리베이터·경비 확인</li>
<li><a href="/check/time/">예약 가능 시간</a>과 <a href="/use/night/">야간 예약</a> 가능 여부</li>
<li><a href="/check/travel-fee/">추가 이동비 기준</a> — 서울·인천 인접권·외곽 이동 여부</li>
<li><a href="/check/privacy/">개인정보 처리 기준</a>과 <a href="/check/service-policy/">불법·선정적 서비스 불가 안내</a></li>
</ul>
<p>부천 외곽이나 서울·인천 경계 인접 지역은 이동 기준이 달라질 수 있으므로 <a href="/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 함께 확인하세요.</p>
</section>

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "부천시 행정구역(원미구·소사구·오정구), 주요 행정동, 생활권, 지하철역, 이용 장소별 예약 전 확인사항을 기준으로 구성했습니다.",
  "부천에서 방문형 서비스를 찾는 사용자가 자신의 지역과 이용 장소를 안전하게 확인할 수 있도록 돕기 위해 작성했습니다.")}

{_faq_html}
"""
)
