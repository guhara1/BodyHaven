# 부천 구별 페이지 — 원미구·소사구·오정구
from .components import page, faq_block, who_how_why, checklist, safety_note

PAGES = []

# ───────── 원미구 ─────────
_wonmi_faq, _wonmi_head = faq_block([
    ("원미구는 어떤 생활권으로 나뉘나요?",
     "중동·신중동 상권, 상동·부천시청 신도시권, 부천역·심곡 원도심권, 춘의·부천종합운동장 환승권, 역곡 서울 인접권으로 크게 나뉩니다."),
    ("원미구에서 오피스텔·숙소 이용이 많은 곳은 어디인가요?",
     "중동·신중동·상동 일대는 오피스텔과 상업시설이 밀집해 있어 방문 전 공동현관과 관리 규정을 함께 확인하는 것이 좋습니다."),
    ("원미구는 어느 지하철 노선을 끼고 있나요?",
     "7호선(신중동·부천시청·상동·춘의·부천종합운동장)과 1호선(부천역·중동역) 생활권이 함께 지나 역세권 기준 확인이 중요합니다."),
])
PAGES.append(page(
    path="wonmi-gu/",
    title="원미구 출장마사지｜중동·상동·신중동 생활권 안내",
    desc="원미구 출장마사지·홈타이 예약 전 중동, 상동, 신중동, 부천역 생활권을 확인하세요.",
    h1="원미구 출장마사지 · 중동·상동·신중동 생활권 안내",
    hero_badge="원미구 방문 관리 안내",
    hero_lead="부천의 중심 상권과 신도시, 7호선 생활권이 함께 있는 원미구의 행정동·생활권·역세권 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 중동 상동 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/"), ("구별 안내", "/wonmi-gu/"), ("원미구", "")],
    extra_head=_wonmi_head,
    body=f"""
<section><h2>원미구 지역 개요</h2>
<p>부천 원미구는 부천시의 중심 상권과 행정·신도시 기능이 모여 있는 지역입니다. 중동·신중동의 상업지구와 오피스텔, 상동신도시의 주거·상권, 부천역·심곡의 원도심, 그리고 춘의·부천종합운동장의 환승 교통이 한 구 안에서 성격을 달리하며 이어집니다. 같은 원미구라도 중동과 부천역, 상동과 춘의는 건물 형태와 이동 동선이 크게 다르기 때문에 예약 전에 자신의 위치를 행정동·생활권 단위로 좁혀 확인하는 것이 정확합니다.</p>
<p>원미구는 7호선(신중동역·부천시청역·상동역·춘의역·부천종합운동장역)과 1호선(부천역·중동역) 생활권이 함께 지나, 같은 동이라도 가까운 역과 출입 동선이 다를 수 있습니다. 방문형 관리를 예약할 때는 구 이름만이 아니라 가까운 역과 건물 출입 방식까지 함께 확인하면 이동 시간과 방문 주소 안내가 한결 수월해집니다.</p></section>

<section><h2>대표 행정동</h2>
<p>원미구의 대표 행정동과 생활권은 다음과 같이 연결됩니다.</p>
<ul>
<li><a href="/wonmi-gu/jung-dong/">중동</a> — 신중동 상권·오피스텔 중심 생활권</li>
<li><a href="/wonmi-gu/sang-dong/">상동</a> — 상동신도시·부천시청 인접 생활권</li>
<li><a href="/wonmi-gu/chunui-dong/">춘의동</a> — 춘의·부천종합운동장 환승 생활권</li>
<li><a href="/wonmi-gu/simgok-1-dong/">심곡1동</a> · <a href="/wonmi-gu/simgok-2-dong/">심곡2동</a> — 부천역 원도심 생활권</li>
<li><a href="/wonmi-gu/yeokgok-1-dong/">역곡1동</a> · <a href="/wonmi-gu/yeokgok-2-dong/">역곡2동</a> — 서울 구로·온수 인접 생활권</li>
</ul></section>

<section><h2>대표 생활권</h2>
<p>원미구는 아래 생활권으로 묶어 보면 위치를 빠르게 좁힐 수 있습니다.</p>
<ul>
<li><a href="/life/jungdong-sinjungdong/">중동·신중동 생활권</a> — 7호선·상권·오피스텔 중심</li>
<li><a href="/life/sangdong-bucheon-cityhall/">상동·부천시청 생활권</a> — 신도시·상권·부평 인접권</li>
<li><a href="/life/bucheon-station-simgok/">부천역·심곡 생활권</a> — 원도심·1호선·상권</li>
<li><a href="/life/chunui-bucheon-stadium/">춘의·부천종합운동장 생활권</a> — 환승·차량 이동 중심</li>
</ul></section>

<section><h2>가까운 지하철역</h2>
<p>원미구 예약 시 자주 기준이 되는 역은 다음과 같습니다. 역세권 페이지에서 인접 행정동과 출입 동선을 확인하세요.</p>
<ul>
<li><a href="/station/sinjungdong-station/">신중동역</a> · <a href="/station/bucheon-cityhall-station/">부천시청역</a> · <a href="/station/sangdong-station/">상동역</a> (7호선)</li>
<li><a href="/station/bucheon-station/">부천역</a> · <a href="/station/jungdong-station/">중동역</a> (1호선)</li>
<li><a href="/station/chunui-station/">춘의역</a> · <a href="/station/bucheon-stadium-station/">부천종합운동장역</a> (7호선·서해선 환승 성격)</li>
</ul></section>

<section><h2>이용 장소별 기준</h2>
<p>중동·신중동·상동은 오피스텔과 상업시설이 많아 <a href="/use/officetel/">오피스텔 이용</a> 시 공동현관·엘리베이터·관리 규정을 먼저 확인해야 합니다. 부천역·심곡 원도심은 다세대·상가 건물이 섞여 있어 <a href="/use/home/">자택 이용</a> 시 정확한 동·호수와 건물 출입 방식 확인이 중요합니다. 출장·여행으로 방문하는 경우 <a href="/use/hotel/">호텔·숙소 이용</a> 정책과 객실 출입 가능 여부를, 늦은 시간 예약은 <a href="/use/night/">야간 예약</a> 기준을 함께 확인하세요.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>원미구 역곡 일대는 서울 구로·온수와 가깝고, 상동·부천시청 일대는 인천 부평과 인접합니다. 행정구역상 부천이라도 실제 이동은 서울·인천 경계를 끼는 경우가 있으므로, 경계 인접 지역은 <a href="/check/travel-fee/">추가 이동비 기준</a>과 <a href="/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("원미구는 같은 구 안에서도 상권·신도시·원도심 성격이 달라 아래 항목을 먼저 확인하면 예약이 정확합니다.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구의 행정동, 생활권, 지하철역, 이용 장소별 확인사항을 부천시 행정구역 기준으로 정리했습니다.",
  "원미구에서 방문형 서비스를 찾는 사용자가 자신의 생활권과 이용 장소를 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p>인접 구 안내도 함께 확인하세요 — <a href="/sosa-gu/">소사구 안내</a> · <a href="/ojeong-gu/">오정구 안내</a> · <a href="/">부천 전체 안내</a></p></section>

{_wonmi_faq}
"""
))

# ───────── 소사구 ─────────
_sosa_faq, _sosa_head = faq_block([
    ("소사구는 어떤 생활권으로 나뉘나요?",
     "부천역·심곡본 상권, 소사·소사본 환승권, 송내 1호선 주거·상권, 범박·옥길 주거권, 괴안·역곡 서울 인접권으로 나뉩니다."),
    ("소사역은 노선별로 페이지가 다른가요?",
     "아니요. 소사역은 1호선·서해선 환승 성격이 있어도 역명 기준 한 개 페이지로 관리합니다."),
    ("범박·옥길은 무엇을 먼저 확인해야 하나요?",
     "주거지·아파트 단지 중심이라 단지명·동호수와 차량 이동 기준, 공동현관 출입 방식을 먼저 확인하는 것이 좋습니다."),
])
PAGES.append(page(
    path="sosa-gu/",
    title="소사구 출장마사지｜부천역·송내·소사 생활권 안내",
    desc="소사구 출장마사지·홈타이 예약 전 부천역, 소사, 송내, 범박, 옥길 생활권을 확인하세요.",
    h1="소사구 출장마사지 · 부천역·송내·소사 생활권 안내",
    hero_badge="소사구 방문 관리 안내",
    hero_lead="1호선 생활권과 서울·인천 이동권, 부천역·송내 상권, 범박·옥길 주거지가 함께 있는 소사구의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 소사구 부천역 송내 소사 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/"), ("구별 안내", "/wonmi-gu/"), ("소사구", "")],
    extra_head=_sosa_head,
    body=f"""
<section><h2>소사구 지역 개요</h2>
<p>부천 소사구는 1호선을 축으로 한 생활권과 서울·인천을 잇는 이동권이 함께 있는 지역입니다. 부천역·심곡본의 상권, 소사역을 낀 소사·소사본의 환승 생활권, 송내역 일대의 주거·상권, 그리고 범박동·옥길동의 아파트 주거지가 성격을 달리하며 이어집니다. 같은 소사구라도 부천역 상권과 범박·옥길 주거지는 건물 형태와 이동 동선이 크게 달라, 예약 전에 행정동·생활권 단위로 위치를 좁혀 확인하는 것이 정확합니다.</p>
<p>소사구는 1호선(부천역·소사역·송내역·역곡3동 인접)과 서해선(소사역) 생활권이 함께 지나며, 서울 구로·온수와 인천 부평 양쪽에 인접한 구간이 많습니다. 그래서 방문 주소가 부천이라도 실제 이동은 경계를 끼는 경우가 있으므로, 가까운 역과 이동 기준을 함께 확인하면 예약이 한결 수월합니다.</p></section>

<section><h2>대표 행정동</h2>
<ul>
<li><a href="/sosa-gu/simgokbon-dong/">심곡본동</a> · <a href="/sosa-gu/simgokbon-1-dong/">심곡본1동</a> — 부천역 상권 생활권</li>
<li><a href="/sosa-gu/sosabon-dong/">소사본동</a> · <a href="/sosa-gu/sosabon-1-dong/">소사본1동</a> — 소사역 환승 생활권</li>
<li><a href="/sosa-gu/songnae-1-dong/">송내1동</a> · <a href="/sosa-gu/songnae-2-dong/">송내2동</a> — 송내역 주거·상권</li>
<li><a href="/sosa-gu/beombak-dong/">범박동</a> · <a href="/sosa-gu/okgil-dong/">옥길동</a> — 아파트 주거 생활권</li>
<li><a href="/sosa-gu/goean-dong/">괴안동</a> · <a href="/sosa-gu/yeokgok-3-dong/">역곡3동</a> — 서울 인접 생활권</li>
</ul></section>

<section><h2>대표 생활권</h2>
<ul>
<li><a href="/life/bucheon-station-simgok/">부천역·심곡 생활권</a> — 원도심·1호선·상권</li>
<li><a href="/life/sosa-sosabon/">소사·소사본 생활권</a> — 1호선·서해선 환승</li>
<li><a href="/life/songnae/">송내 생활권</a> — 1호선·인천 인접·주거지</li>
<li><a href="/life/beombak-okgil/">범박·옥길 생활권</a> — 주거·차량 이동 중심</li>
</ul></section>

<section><h2>가까운 지하철역</h2>
<ul>
<li><a href="/station/bucheon-station/">부천역</a> · <a href="/station/songnae-station/">송내역</a> · <a href="/station/yeokgok-station/">역곡역</a> (1호선)</li>
<li><a href="/station/sosa-station/">소사역</a> (1호선·서해선 환승, 역명 기준 1개 페이지)</li>
</ul></section>

<section><h2>이용 장소별 기준</h2>
<p>부천역·송내는 상권·역세권 중심이라 <a href="/use/station-area/">역세권 이용</a> 시 건물명과 출입 동선을 먼저 확인하는 것이 좋습니다. 범박·옥길은 아파트 단지 위주여서 <a href="/use/home/">자택 이용</a> 시 단지명·동호수와 공동현관 방식, 그리고 <a href="/use/outer-area/">외곽 지역 이용</a> 기준에 따른 차량 이동을 함께 확인해야 합니다. 송내·역곡 일대는 서울·인천과 가까워 <a href="/use/adjacent-area/">서울·인천 인접권 이용</a> 안내도 참고하세요.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>소사구는 역곡3동·괴안동이 서울 구로·온수와, 송내 일대가 인천 부평과 인접합니다. 경계 인접 지역은 <a href="/check/travel-fee/">추가 이동비 기준</a>을 예약 전에 확인하면 이동 안내가 명확해집니다.</p></section>

{checklist("소사구는 상권·환승·주거지 성격이 한 구 안에서 나뉘므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "소사구의 행정동, 생활권, 지하철역, 이용 장소별 확인사항을 부천시 행정구역 기준으로 정리했습니다.",
  "소사구에서 방문형 서비스를 찾는 사용자가 자신의 생활권과 이동 기준을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/wonmi-gu/">원미구 안내</a> · <a href="/ojeong-gu/">오정구 안내</a> · <a href="/">부천 전체 안내</a></p></section>

{_sosa_faq}
"""
))

# ───────── 오정구 ─────────
_ojeong_faq, _ojeong_head = faq_block([
    ("오정구는 어떤 생활권으로 나뉘나요?",
     "원종·고강 서해선·서울 강서 인접권, 오정·신흥 산업·주거 혼합권, 성곡·까치울 녹지·주거권으로 나뉩니다."),
    ("오정구는 차량 이동 확인이 왜 중요한가요?",
     "지하철역이 상대적으로 적고 서해선·7호선 접근권과 외곽 구간이 섞여 있어 방문 주소에 따라 차량 이동 기준을 함께 확인하는 것이 좋습니다."),
    ("오정구에서 가까운 지하철역은 어디인가요?",
     "원종역(서해선), 까치울역·부천종합운동장역(7호선) 생활권이 가까우며, 역과 거리가 있는 지역은 이동 기준을 미리 확인하세요."),
])
PAGES.append(page(
    path="ojeong-gu/",
    title="오정구 출장마사지｜원종·고강·오정 생활권 안내",
    desc="오정구 출장마사지·홈타이 예약 전 원종, 고강, 오정, 신흥, 성곡 생활권을 확인하세요.",
    h1="오정구 출장마사지 · 원종·고강·오정 생활권 안내",
    hero_badge="오정구 방문 관리 안내",
    hero_lead="서해선·7호선 접근권과 차량 이동 기준이 함께 필요한 오정구의 행정동·생활권·역세권 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 오정구 원종 고강 오정 생활권 이동 기준 안내 이미지",
    breadcrumb=[("부천", "/"), ("구별 안내", "/wonmi-gu/"), ("오정구", "")],
    extra_head=_ojeong_head,
    body=f"""
<section><h2>오정구 지역 개요</h2>
<p>부천 오정구는 서해선·7호선 접근권과 차량 이동 기준이 함께 필요한 지역입니다. 서해선 원종역을 낀 원종 생활권, 서울 강서·김포공항과 가까운 고강 생활권, 산업과 주거가 섞인 오정·신흥 생활권, 녹지와 주거가 어우러진 성곡·까치울 생활권이 성격을 달리하며 이어집니다. 오정구는 다른 두 구에 비해 지하철역이 적어, 같은 구 안에서도 역과의 거리와 차량 이동 동선을 함께 보는 것이 예약 시 특히 중요합니다.</p>
<p>고강 일대는 서울 강서구·김포공항과 인접해 이동 동선이 서울 쪽으로 이어지는 경우가 있고, 원종은 서해선을 통한 접근이 편리합니다. 방문 주소가 오정구라도 실제 이동 경로는 인접 지역을 끼는 경우가 있으므로, 가까운 역과 차량 이동 기준을 함께 확인하면 방문 안내가 정확해집니다.</p></section>

<section><h2>대표 행정동</h2>
<ul>
<li><a href="/ojeong-gu/wonjong-1-dong/">원종1동</a> · <a href="/ojeong-gu/wonjong-2-dong/">원종2동</a> — 서해선 원종 생활권</li>
<li><a href="/ojeong-gu/gogangbon-dong/">고강본동</a> · <a href="/ojeong-gu/gogang-1-dong/">고강1동</a> — 서울 강서 인접 생활권</li>
<li><a href="/ojeong-gu/ojeong-dong/">오정동</a> · <a href="/ojeong-gu/sinheung-dong/">신흥동</a> — 산업·주거 혼합 생활권</li>
<li><a href="/ojeong-gu/seonggok-dong/">성곡동</a> — 녹지·주거 생활권</li>
</ul></section>

<section><h2>대표 생활권</h2>
<ul>
<li><a href="/life/wonjong-gogang/">원종·고강 생활권</a> — 서해선·서울 강서 인접·차량 이동</li>
<li><a href="/life/ojeong-sinheung/">오정·신흥 생활권</a> — 산업·주거 혼합</li>
<li><a href="/life/kkachiwool-seonggok/">까치울·성곡 생활권</a> — 녹지·주거 중심</li>
</ul></section>

<section><h2>가까운 지하철역</h2>
<ul>
<li><a href="/station/wonjong-station/">원종역</a> (서해선)</li>
<li><a href="/station/kkachiwool-station/">까치울역</a> · <a href="/station/bucheon-stadium-station/">부천종합운동장역</a> (7호선)</li>
</ul></section>

<section><h2>이용 장소별 기준</h2>
<p>오정구는 역과 거리가 있는 지역이 많아 <a href="/use/outer-area/">외곽 지역 이용</a> 기준과 차량 이동 안내가 중요합니다. 아파트·주택 방문은 <a href="/use/home/">자택 이용</a> 시 단지명·동호수와 공동현관 방식을, 산업·주거 혼합 지역은 건물 유형과 출입 동선을 먼저 확인하세요. 고강·원종 일대는 서울 강서와 가까워 <a href="/use/adjacent-area/">서울·인천 인접권 이용</a> 안내도 함께 확인하면 좋습니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>고강본동·고강1동은 서울 강서구·김포공항 방면과 인접해 이동 경로가 서울 쪽으로 이어질 수 있습니다. 경계·외곽 인접 지역은 <a href="/check/travel-fee/">추가 이동비 기준</a>을 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("오정구는 역과의 거리와 차량 이동이 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "오정구의 행정동, 생활권, 지하철역, 차량 이동 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "오정구에서 방문형 서비스를 찾는 사용자가 자신의 생활권과 이동 기준을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/wonmi-gu/">원미구 안내</a> · <a href="/sosa-gu/">소사구 안내</a> · <a href="/">부천 전체 안내</a></p></section>

{_ojeong_faq}
"""
))
