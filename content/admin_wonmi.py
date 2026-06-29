# 부천 원미구 행정동 페이지 — FULL 7 + STUB 12
from .components import page, faq_block, who_how_why, checklist, safety_note

PAGES = []

# ════════════════════════════ FULL 페이지 ════════════════════════════

# ───────── 1. 중동 (jung-dong) ─────────
_jung_faq, _jung_head = faq_block([
    ("중동은 어느 역과 생활권을 기준으로 봐야 하나요?",
     "중동은 7호선 신중동역 상권과 1호선 중동역 생활권이 함께 닿는 지역이라, 예약 전에 자신이 신중동 상권 쪽인지 중동역 쪽인지 가까운 역을 먼저 좁혀 확인하는 것이 정확합니다."),
    ("중동에서 오피스텔 방문은 무엇을 먼저 확인하나요?",
     "신중동역 일대는 오피스텔과 상업시설이 밀집해 있어 공동현관 비밀번호, 엘리베이터 카드 사용 여부, 방문객 출입 규정을 예약 전에 함께 확인하는 것이 좋습니다."),
    ("중동은 야간 예약도 확인이 필요한가요?",
     "상권 중심이라 늦은 시간 이용 문의가 많은 편이며, 야간 예약은 예약 가능 시간과 건물 출입 방식을 미리 확인해두면 방문 안내가 수월합니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/jung-dong/",
    title="중동 출장마사지｜신중동 상권·오피스텔 생활권 안내",
    desc="중동 출장마사지·홈타이 예약 전 신중동 상권, 오피스텔, 7호선 역세권 기준을 확인하세요.",
    h1="중동(원미구) 방문 관리 안내 · 신중동 상권·오피스텔 생활권",
    hero_badge="중동 행정동 방문 관리 안내",
    hero_lead="7호선 신중동역 상권과 오피스텔이 밀집한 원미구 중동의 행정동·역세권·이용 장소별 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 중동 신중동 상권 오피스텔 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("중동", "")],
    extra_head=_jung_head,
    body=f"""
<section><h2>중동 행정동 위치 설명</h2>
<p>중동은 부천 원미구의 중심 상권을 끼고 있는 행정동입니다. 7호선 신중동역을 중심으로 백화점·대형 상업시설과 오피스텔, 업무용 빌딩이 밀집해 있어 부천 안에서도 유동인구와 건물 밀도가 가장 높은 축에 듭니다. 같은 중동이라도 신중동역 상권 쪽과 1호선 중동역 쪽은 건물 형태와 이동 동선이 다르므로, 예약 전에 자신의 위치를 가까운 역 단위로 좁혀 확인하면 방문 주소 안내가 한결 정확해집니다.</p>
<p>중동은 도로망이 정비되어 차량 접근은 편리하지만, 상업지구 특성상 건물마다 주차·출입 규정이 다릅니다. 오피스텔과 상가가 혼재한 구역이 많아 공동현관 방식과 엘리베이터 이용 규정이 건물별로 다를 수 있습니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>중동은 행정구역상 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속합니다. 원미구는 중동·신중동 상권, 상동신도시, 부천역·심곡 원도심, 춘의·부천종합운동장 환승권이 한 구 안에서 성격을 달리하며 이어지는 지역으로, 중동은 그중 상권·업무 기능이 가장 집중된 축에 해당합니다. 부천 전체의 생활권·역세권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 함께 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>중동은 <a href="/bucheon/life/jungdong-sinjungdong/">중동·신중동 생활권</a>의 핵심에 해당하며, 7호선·상권·오피스텔 중심으로 묶입니다. 신도시 주거·상권이 이어지는 <a href="/bucheon/life/jungdong-newtown/">중동신도시 생활권</a>과도 가까워, 단지형 주거와 상업시설이 만나는 경계 구간에서는 두 생활권 안내를 함께 보는 것이 위치를 좁히는 데 도움이 됩니다.</p></section>

<section><h2>가까운 지하철역</h2>
<p>중동 예약 시 기준이 되는 역은 7호선 <a href="/bucheon/station/sinjungdong-station/">신중동역</a>과 1호선 <a href="/bucheon/station/jungdong-station/">중동역</a>입니다. 상권 중심부는 신중동역, 주거·생활 구간 일부는 중동역이 가깝습니다. 7호선 <a href="/bucheon/station/bucheon-cityhall-station/">부천시청역</a> 방면과도 이어지므로, 역세권 페이지에서 출구별 인접 행정동과 출입 동선을 확인하면 이동 시간을 가늠하기 쉽습니다.</p></section>

<section><h2>인접 행정동</h2>
<p>중동은 신도시·상권으로 이어지는 <a href="/bucheon/wonmi-gu/sang-dong/">상동</a>, 7호선 환승권으로 이어지는 <a href="/bucheon/wonmi-gu/chunui-dong/">춘의동</a>, 원도심 상권인 <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a>·<a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a>과 인접합니다. 경계 구간은 같은 도로를 사이에 두고 행정동이 갈리는 경우가 있으므로, 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>중동은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 비중이 높아 공동현관·엘리베이터·관리 규정을 먼저 확인해야 합니다. 일반 주거지 방문은 <a href="/bucheon/use/home/">자택 이용</a> 시 정확한 동·호수와 건물 출입 방식을, 출장·여행으로 머무는 경우 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책과 객실 출입 가능 여부를 확인하세요.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>신중동역·중동역 일대는 상업시설과 오피스텔이 밀집한 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 같은 역세권이라도 건물명과 출구가 다르면 진입 동선이 달라지므로, 예약 시 건물명과 가까운 출구를 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>중동은 원미구 중심부에 있어 서울·인천 경계와 직접 맞닿지는 않지만, 상동·부천시청 방면을 거쳐 인천 부평권으로 이동 동선이 이어질 수 있습니다. 경계 인접 구간 방문은 <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("중동은 상권·오피스텔 밀집 지역이라 건물 출입 방식이 특히 중요합니다. 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 중동의 위치, 가까운 역세권, 생활권, 이용 장소별 확인사항을 부천시 행정구역 기준으로 정리했습니다.",
  "중동에서 방문형 서비스를 찾는 사용자가 신중동 상권·오피스텔 환경에 맞춰 위치와 출입 방식을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/sang-dong/">상동</a> · <a href="/bucheon/wonmi-gu/chunui-dong/">춘의동</a> · <a href="/bucheon/life/jungdong-sinjungdong/">중동·신중동 생활권</a> · <a href="/bucheon/station/sinjungdong-station/">신중동역 주변</a> · <a href="/bucheon/check/building-access/">건물 출입 방식 확인</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_jung_faq}
"""
))

# ───────── 2. 상동 (sang-dong) ─────────
_sang_faq, _sang_head = faq_block([
    ("상동은 어떤 성격의 지역인가요?",
     "상동은 상동신도시의 계획형 주거·상업지구가 중심이며, 7호선 상동역·부천시청역 생활권과 인천 부평 인접권이 함께 닿는 지역입니다."),
    ("상동에서 자택 방문은 무엇을 확인하나요?",
     "단지형 아파트가 많아 단지명과 동·호수, 공동현관 출입 방식, 방문 차량 주차 가능 여부를 예약 전에 함께 확인하는 것이 좋습니다."),
    ("상동은 인천 이동도 확인이 필요한가요?",
     "상동은 인천 부평권과 가까워 방문 주소에 따라 경계를 끼는 경우가 있으므로, 인접권 이용과 추가 이동비 기준을 미리 확인하면 안내가 명확해집니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/sang-dong/",
    title="상동 출장마사지｜상동신도시·부천시청·부평 인접 안내",
    desc="상동 출장마사지·홈타이 예약 전 상동신도시, 부천시청역, 부평 인접 기준을 확인하세요.",
    h1="상동(원미구) 방문 관리 안내 · 상동신도시·부천시청 생활권",
    hero_badge="상동 행정동 방문 관리 안내",
    hero_lead="상동신도시 주거·상권과 7호선 상동역·부천시청역, 인천 부평 인접권이 함께 닿는 원미구 상동의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 상동 상동신도시 부천시청 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("상동", "")],
    extra_head=_sang_head,
    body=f"""
<section><h2>상동 행정동 위치 설명</h2>
<p>상동은 부천 원미구 동쪽에 자리한 계획형 신도시 행정동입니다. 상동신도시의 정비된 아파트 단지와 대형 상업시설, 7호선 상동역·부천시청역 생활권이 함께 있어 주거와 상권이 균형 있게 어우러진 지역입니다. 단지마다 출입 체계가 정해져 있어 도로변 상가와 단지 내부의 방문 동선이 뚜렷이 구분되며, 예약 전에 단지명과 가까운 역을 함께 좁혀 확인하면 방문 주소 안내가 정확해집니다.</p>
<p>상동은 부천시청이 가까운 행정 중심이기도 하며, 인천 부평구와 경계를 맞대고 있어 동쪽 구간은 인천 생활권과 이어집니다. 같은 상동이라도 부천시청역 방면과 부평 경계 방면은 이동 동선이 다를 수 있어, 방문 주소가 어느 쪽인지 먼저 확인하는 것이 좋습니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>상동은 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 원미구의 신도시·행정 기능을 대표하는 축입니다. 원미구는 중동·신중동 상권과 상동신도시, 부천역·심곡 원도심이 함께 있는 구로, 상동은 그중 계획형 주거·상권이 가장 잘 정비된 지역에 해당합니다. 부천 전체 구·생활권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>상동은 <a href="/bucheon/life/sangdong-bucheon-cityhall/">상동·부천시청 생활권</a>의 중심이며, 신도시·상권·부평 인접권으로 묶입니다. 계획형 주거 단지가 이어지는 <a href="/bucheon/life/sangdong-newtown/">상동신도시 생활권</a>과도 직접 맞닿아, 단지 위치에 따라 두 생활권 안내를 함께 보면 위치를 좁히기 쉽습니다. 인천 방면은 <a href="/bucheon/life/incheon-adjacent/">인천 인접권 생활권</a>도 참고하세요.</p></section>

<section><h2>가까운 지하철역</h2>
<p>상동 예약 시 기준이 되는 역은 7호선 <a href="/bucheon/station/sangdong-station/">상동역</a>과 <a href="/bucheon/station/bucheon-cityhall-station/">부천시청역</a>입니다. 신도시 상권은 상동역, 행정·업무 구간은 부천시청역이 가깝습니다. 7호선 <a href="/bucheon/station/sinjungdong-station/">신중동역</a> 방면과도 이어지므로 역세권 페이지에서 출구별 인접 동선을 확인하면 이동이 수월합니다.</p></section>

<section><h2>인접 행정동</h2>
<p>상동은 상권·업무권으로 이어지는 <a href="/bucheon/wonmi-gu/jung-dong/">중동</a>, 7호선 환승권인 <a href="/bucheon/wonmi-gu/chunui-dong/">춘의동</a>과 인접하며, 동쪽으로는 인천 부평구와 경계를 맞댑니다. 원도심 방면인 <a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a>과도 생활권이 이어지므로, 경계 구간은 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>상동은 단지형 아파트가 많아 <a href="/bucheon/use/home/">자택 이용</a> 시 단지명·동호수와 공동현관 방식 확인이 가장 중요합니다. 상업지구의 오피스텔은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 시 관리 규정을, 출장·여행 방문은 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책과 객실 출입 가능 여부를 함께 확인하세요. 계획형 신도시 특성상 <a href="/bucheon/use/newtown/">신도시 이용</a> 기준도 참고하면 좋습니다.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>상동역·부천시청역 일대는 단지와 상업시설이 함께 있는 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 단지 내부는 정문·후문 위치에 따라 진입 동선이 달라지므로, 예약 시 단지명과 가까운 출입구를 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>상동은 인천 부평구와 직접 맞닿아 동쪽 구간은 인천 생활권으로 이동이 이어질 수 있습니다. 경계 인접 구간 방문은 <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("상동은 신도시 단지와 부평 경계가 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 상동의 위치, 신도시 단지, 가까운 역세권, 인천 인접 이동 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "상동에서 방문형 서비스를 찾는 사용자가 단지 출입과 부평 인접 이동 기준을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/jung-dong/">중동</a> · <a href="/bucheon/wonmi-gu/chunui-dong/">춘의동</a> · <a href="/bucheon/life/sangdong-bucheon-cityhall/">상동·부천시청 생활권</a> · <a href="/bucheon/station/sangdong-station/">상동역 주변</a> · <a href="/bucheon/use/newtown/">신도시 이용 확인</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_sang_faq}
"""
))

# ───────── 3. 춘의동 (chunui-dong) ─────────
_chunui_faq, _chunui_head = faq_block([
    ("춘의동은 어떤 교통 특성이 있나요?",
     "춘의동은 7호선 춘의역과 부천종합운동장역 환승 생활권을 끼고 있어, 지하철 접근과 차량 이동을 함께 고려해 방문 동선을 잡는 것이 좋습니다."),
    ("춘의동은 차량 이동 확인이 왜 중요한가요?",
     "부천종합운동장과 녹지·시설 구간이 섞여 있어 역과 거리가 있는 주소가 있으므로, 방문 주소에 따라 차량 이동 기준을 미리 확인하면 안내가 정확해집니다."),
    ("춘의동에서 가까운 역은 어디인가요?",
     "7호선 춘의역과 부천종합운동장역이 가까우며, 두 역 모두 환승 성격이 있어 출구·방면에 따라 진입 동선이 달라질 수 있습니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/chunui-dong/",
    title="춘의동 출장마사지｜춘의역·부천종합운동장 환승 안내",
    desc="춘의동 출장마사지·홈타이 예약 전 춘의역, 부천종합운동장역 환승·차량 이동 기준을 확인하세요.",
    h1="춘의동(원미구) 방문 관리 안내 · 춘의역·부천종합운동장 환승 생활권",
    hero_badge="춘의동 행정동 방문 관리 안내",
    hero_lead="7호선 춘의역·부천종합운동장역 환승 생활권과 차량 이동이 함께 필요한 원미구 춘의동의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 춘의동 춘의역 부천종합운동장 환승 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("춘의동", "")],
    extra_head=_chunui_head,
    body=f"""
<section><h2>춘의동 행정동 위치 설명</h2>
<p>춘의동은 부천 원미구 북쪽에 자리한 교통 환승 성격의 행정동입니다. 7호선 춘의역과 부천종합운동장역을 끼고 있어 환승·이동 기능이 강하며, 부천종합운동장과 녹지·체육 시설, 일반 주거가 함께 섞여 있습니다. 같은 춘의동이라도 역세권 주거 구간과 운동장·시설 구간은 이동 동선이 크게 다르므로, 예약 전에 가까운 역과 차량 이동 기준을 함께 좁혀 확인하는 것이 정확합니다.</p>
<p>역세권에 가까운 주소는 지하철 접근이 편리하지만, 시설·녹지 구간은 역과 거리가 있어 차량 이동을 고려해야 합니다. 부천종합운동장 일대는 행사·경기 일정에 따라 도로 혼잡이 생길 수 있어 방문 시간대에 따라 이동 시간을 여유 있게 보는 것이 좋습니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>춘의동은 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 원미구의 7호선 환승 교통을 대표하는 축입니다. 원미구는 중동·신중동 상권과 상동신도시, 춘의·부천종합운동장 환승권이 함께 있는 구로, 춘의동은 그중 환승·차량 이동 성격이 가장 뚜렷한 지역에 해당합니다. 부천 전체 구·생활권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>춘의동은 <a href="/bucheon/life/chunui-bucheon-stadium/">춘의·부천종합운동장 생활권</a>의 중심이며, 환승·차량 이동 중심으로 묶입니다. 상권·업무권인 <a href="/bucheon/life/jungdong-sinjungdong/">중동·신중동 생활권</a>과도 7호선으로 이어지고, 북서쪽 녹지·주거권인 <a href="/bucheon/life/kkachiwool-seonggok/">까치울·성곡 생활권</a>과도 가까워 경계 구간은 생활권 안내를 함께 보면 위치를 좁히기 쉽습니다.</p></section>

<section><h2>가까운 지하철역</h2>
<p>춘의동 예약 시 기준이 되는 역은 7호선 <a href="/bucheon/station/chunui-station/">춘의역</a>과 <a href="/bucheon/station/bucheon-stadium-station/">부천종합운동장역</a>입니다. 두 역 모두 환승 성격이 있어 출구·방면에 따라 진입 동선이 달라집니다. 인접한 <a href="/bucheon/station/kkachiwool-station/">까치울역</a> 방면과도 이어지므로, 역세권 페이지에서 가까운 출구와 차량 진입 동선을 함께 확인하면 좋습니다.</p></section>

<section><h2>인접 행정동</h2>
<p>춘의동은 상권권인 <a href="/bucheon/wonmi-gu/jung-dong/">중동</a>, 신도시권인 <a href="/bucheon/wonmi-gu/sang-dong/">상동</a>, 원도심 상권인 <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a>과 인접하며, 북서쪽으로는 오정구 녹지·주거권과 이어집니다. 시설·녹지 경계 구간은 행정동이 갈리는 지점이 있으므로, 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>춘의동은 일반 주거지 방문이 많아 <a href="/bucheon/use/home/">자택 이용</a> 시 정확한 동·호수와 건물 출입 방식 확인이 중요합니다. 역세권 인근 오피스텔은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 시 관리 규정을, 행사·출장 방문은 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책을 확인하세요. 역과 거리가 있는 주소는 <a href="/bucheon/use/outer-area/">외곽 지역 이용</a> 기준에 따른 차량 이동도 함께 확인하면 좋습니다.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>춘의역·부천종합운동장역 일대는 환승 성격이 강한 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 환승역은 출구가 많고 운동장 행사 시 동선이 달라질 수 있으므로, 예약 시 가까운 출구와 건물명을 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>춘의동 자체는 서울·인천 경계와 직접 맞닿지 않지만, 7호선·도로망을 통해 인접 구와 서울 방면으로 동선이 이어질 수 있습니다. 경계·외곽 인접 구간 방문은 <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("춘의동은 환승역 접근과 차량 이동이 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 춘의동의 위치, 환승 역세권, 생활권, 차량 이동 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "춘의동에서 방문형 서비스를 찾는 사용자가 환승역 접근과 차량 이동 기준을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/jung-dong/">중동</a> · <a href="/bucheon/wonmi-gu/sang-dong/">상동</a> · <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a> · <a href="/bucheon/life/chunui-bucheon-stadium/">춘의·부천종합운동장 생활권</a> · <a href="/bucheon/station/bucheon-stadium-station/">부천종합운동장역 주변</a> · <a href="/bucheon/check/travel-fee/">추가 이동비 확인</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_chunui_faq}
"""
))

# ───────── 4. 심곡1동 (simgok-1-dong) ─────────
_simgok1_faq, _simgok1_head = faq_block([
    ("심곡1동은 어떤 성격의 지역인가요?",
     "심곡1동은 1호선 부천역 북측 원도심 상권을 끼고 있어 상가·다세대 건물이 밀집한 지역입니다. 골목 단위 주소가 많아 정확한 건물 확인이 중요합니다."),
    ("심곡1동에서 방문 주소는 무엇을 먼저 확인하나요?",
     "원도심 특성상 비슷한 번지와 골목이 많아, 건물명·동호수와 가까운 큰길 또는 출구를 함께 알려주면 방문 안내가 정확해집니다."),
    ("심곡1동에서 가까운 역은 어디인가요?",
     "1호선 부천역이 가장 가깝습니다. 부천역은 출구가 많고 상권이 넓어 가까운 출구를 함께 확인하면 이동이 수월합니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/simgok-1-dong/",
    title="심곡1동 출장마사지｜부천역 원도심 상권 생활권 안내",
    desc="심곡1동 출장마사지·홈타이 예약 전 부천역 원도심 상권과 건물 출입 기준을 확인하세요.",
    h1="심곡1동(원미구) 방문 관리 안내 · 부천역 원도심 상권 생활권",
    hero_badge="심곡1동 행정동 방문 관리 안내",
    hero_lead="1호선 부천역 북측 원도심 상권을 끼고 상가·다세대가 밀집한 원미구 심곡1동의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 심곡1동 부천역 원도심 상권 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("심곡1동", "")],
    extra_head=_simgok1_head,
    body=f"""
<section><h2>심곡1동 행정동 위치 설명</h2>
<p>심곡1동은 부천 원미구의 1호선 부천역 북측에 자리한 원도심 행정동입니다. 부천역 상권을 끼고 상가와 다세대·다가구 건물이 촘촘하게 밀집해 있어, 부천 안에서도 오래된 도심 특유의 골목 구조가 잘 남아 있는 지역입니다. 같은 심곡1동이라도 큰길가 상가와 골목 안 주거지는 진입 동선이 크게 다르므로, 예약 전에 건물명과 가까운 큰길·출구를 함께 좁혀 확인하면 방문 주소 안내가 정확해집니다.</p>
<p>원도심 특성상 비슷한 번지와 골목이 많고 일방통행·좁은 도로가 섞여 있어 차량 진입 동선을 미리 가늠하는 것이 좋습니다. 상가와 주거 건물이 한 골목에 섞여 있어 건물 유형과 출입 방식을 함께 확인하면 수월합니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>심곡1동은 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 원미구의 부천역 원도심 상권을 대표하는 축입니다. 원미구는 중동·신중동 상권과 상동신도시, 부천역·심곡 원도심이 함께 있는 구로, 심곡1동은 그중 1호선 부천역 상권 기능이 집중된 지역에 해당합니다. 부천 전체 구·생활권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>심곡1동은 <a href="/bucheon/life/bucheon-station-simgok/">부천역·심곡 생활권</a>의 중심이며, 원도심·1호선·상권으로 묶입니다. 상권·업무권인 <a href="/bucheon/life/jungdong-sinjungdong/">중동·신중동 생활권</a>과도 이어지므로, 부천역과 신중동 상권 사이 경계 구간은 두 생활권 안내를 함께 보면 위치를 좁히기 쉽습니다.</p></section>

<section><h2>가까운 지하철역</h2>
<p>심곡1동 예약 시 기준이 되는 역은 1호선 <a href="/bucheon/station/bucheon-station/">부천역</a>입니다. 부천역은 출구가 많고 상권이 넓게 퍼져 있어, 가까운 출구를 함께 확인하면 진입 동선이 명확해집니다. 1호선 <a href="/bucheon/station/jungdong-station/">중동역</a> 방면과도 이어지므로 역세권 페이지에서 출구별 인접 동선을 확인하세요.</p></section>

<section><h2>인접 행정동</h2>
<p>심곡1동은 같은 원도심권인 <a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a>, 상권권인 <a href="/bucheon/wonmi-gu/jung-dong/">중동</a>, 환승권인 <a href="/bucheon/wonmi-gu/chunui-dong/">춘의동</a>과 인접합니다. 부천역을 사이에 두고 소사구 심곡본동 방면과도 생활권이 이어지므로, 경계 구간은 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>심곡1동은 다세대·다가구 주거가 많아 <a href="/bucheon/use/home/">자택 이용</a> 시 정확한 동·호수와 건물 출입 방식 확인이 가장 중요합니다. 상가 건물 내 사무공간은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 기준을, 부천역 인근 숙소 방문은 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책을 함께 확인하세요.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>부천역 일대는 출구가 많고 상권이 넓은 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 같은 부천역이라도 출구가 다르면 골목 진입 동선이 완전히 달라지므로, 예약 시 가까운 출구와 건물명, 큰길 이름을 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>심곡1동은 부천 중앙에 가까워 서울·인천 경계와 직접 맞닿지 않지만, 1호선을 통해 서울 구로·온수 방면과 인천 부평 방면 양쪽으로 이동 동선이 이어질 수 있습니다. 경계 인접 구간 방문은 <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("심곡1동은 원도심 골목과 부천역 출구가 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 심곡1동의 위치, 부천역 역세권, 원도심 상권, 건물 출입 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "심곡1동에서 방문형 서비스를 찾는 사용자가 원도심 골목 환경과 부천역 출구 동선을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a> · <a href="/bucheon/wonmi-gu/jung-dong/">중동</a> · <a href="/bucheon/wonmi-gu/chunui-dong/">춘의동</a> · <a href="/bucheon/life/bucheon-station-simgok/">부천역·심곡 생활권</a> · <a href="/bucheon/station/bucheon-station/">부천역 주변</a> · <a href="/bucheon/check/address/">방문 주소 확인</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_simgok1_faq}
"""
))

# ───────── 5. 심곡2동 (simgok-2-dong) ─────────
_simgok2_faq, _simgok2_head = faq_block([
    ("심곡2동은 심곡1동과 무엇이 다른가요?",
     "심곡2동도 부천역 원도심권에 속하지만 상가와 주거가 더 고르게 섞인 생활권으로, 다세대 주거 비중이 높아 자택 방문 시 정확한 건물 확인이 특히 중요합니다."),
    ("심곡2동에서 자택 방문은 무엇을 확인하나요?",
     "다세대·다가구가 많아 건물명·동호수와 공동현관 방식, 가까운 큰길을 함께 알려주면 골목이 많은 구간에서도 방문 안내가 정확해집니다."),
    ("심곡2동에서 가까운 역은 어디인가요?",
     "1호선 부천역이 가깝고, 일부 구간은 중동역 방면과도 이어집니다. 가까운 출구와 큰길을 함께 확인하면 이동이 수월합니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/simgok-2-dong/",
    title="심곡2동 출장마사지｜부천역 원도심 주거·상가 안내",
    desc="심곡2동 출장마사지·홈타이 예약 전 부천역 원도심 주거·상가와 건물 출입 기준을 확인하세요.",
    h1="심곡2동(원미구) 방문 관리 안내 · 부천역 원도심 주거·상가 생활권",
    hero_badge="심곡2동 행정동 방문 관리 안내",
    hero_lead="1호선 부천역 원도심권에서 주거와 상가가 고르게 섞인 원미구 심곡2동의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 심곡2동 부천역 원도심 주거 상가 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("심곡2동", "")],
    extra_head=_simgok2_head,
    body=f"""
<section><h2>심곡2동 행정동 위치 설명</h2>
<p>심곡2동은 부천 원미구의 1호선 부천역 원도심권에 자리한 행정동으로, 상가와 다세대 주거가 고르게 섞여 있는 생활권입니다. 부천역 상권과 직접 이어지면서도 주거 비중이 높아, 큰길가 상가와 골목 안 주거지가 한 동 안에 공존합니다. 같은 심곡2동이라도 부천역에 가까운 상권 구간과 안쪽 주거 구간은 진입 동선이 다르므로, 예약 전에 건물명과 가까운 큰길을 함께 좁혀 확인하면 방문 주소 안내가 정확해집니다.</p>
<p>원도심 주거지 특성상 비슷한 번지와 좁은 골목이 많고 다세대·다가구 건물이 밀집해 있어 정확한 동·호수 확인이 중요합니다. 차량 진입이 어려운 골목이 섞여 있어 인근 큰길과 주차 가능 위치를 미리 가늠해두면 좋습니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>심곡2동은 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 부천역 원도심의 주거·생활 기능을 대표하는 축입니다. 원미구는 부천역·심곡 원도심과 중동·신중동 상권, 상동신도시가 함께 있는 구로, 심곡2동은 그중 원도심 주거지 성격이 뚜렷한 지역에 해당합니다. 부천 전체 구·생활권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>심곡2동은 <a href="/bucheon/life/bucheon-station-simgok/">부천역·심곡 생활권</a>에 속하며, 원도심·1호선·주거 중심으로 묶입니다. 상권·업무권인 <a href="/bucheon/life/jungdong-sinjungdong/">중동·신중동 생활권</a>과도 이어지므로, 부천역과 중동 상권 사이 경계 구간은 두 생활권 안내를 함께 보면 위치를 좁히기 쉽습니다.</p></section>

<section><h2>가까운 지하철역</h2>
<p>심곡2동 예약 시 기준이 되는 역은 1호선 <a href="/bucheon/station/bucheon-station/">부천역</a>입니다. 동 일부 구간은 1호선 <a href="/bucheon/station/jungdong-station/">중동역</a> 방면과도 이어집니다. 부천역은 출구가 많아 가까운 출구와 큰길을 함께 확인하면 골목 진입 동선이 명확해지므로, 역세권 페이지에서 출구별 인접 동선을 확인하세요.</p></section>

<section><h2>인접 행정동</h2>
<p>심곡2동은 같은 원도심권인 <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a>, 상권권인 <a href="/bucheon/wonmi-gu/jung-dong/">중동</a>, 신도시권인 <a href="/bucheon/wonmi-gu/sang-dong/">상동</a>과 인접합니다. 부천역을 사이에 두고 소사구 심곡본동 방면과도 생활권이 이어지므로, 경계 구간은 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>심곡2동은 다세대·다가구 주거가 많아 <a href="/bucheon/use/home/">자택 이용</a> 시 정확한 동·호수와 공동현관 출입 방식 확인이 가장 중요합니다. 상가 내 사무공간은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 기준을, 부천역 인근 숙소 방문은 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책을 함께 확인하세요.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>부천역 일대는 상권과 주거가 함께 있는 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 같은 부천역이라도 출구와 큰길이 다르면 골목 진입 동선이 달라지므로, 예약 시 가까운 출구와 건물명, 큰길 이름을 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>심곡2동은 부천 중앙에 가까워 서울·인천 경계와 직접 맞닿지 않지만, 1호선을 통해 서울 구로·온수 방면과 인천 부평 방면 양쪽으로 이동 동선이 이어질 수 있습니다. 경계 인접 구간 방문은 <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("심곡2동은 원도심 주거 골목과 부천역 출구가 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 심곡2동의 위치, 부천역 역세권, 원도심 주거·상가, 건물 출입 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "심곡2동에서 방문형 서비스를 찾는 사용자가 원도심 주거 골목 환경과 부천역 출구 동선을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a> · <a href="/bucheon/wonmi-gu/jung-dong/">중동</a> · <a href="/bucheon/wonmi-gu/sang-dong/">상동</a> · <a href="/bucheon/life/bucheon-station-simgok/">부천역·심곡 생활권</a> · <a href="/bucheon/station/bucheon-station/">부천역 주변</a> · <a href="/bucheon/check/building-access/">건물 출입 방식 확인</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_simgok2_faq}
"""
))

# ───────── 6. 역곡1동 (yeokgok-1-dong) ─────────
_yeokgok1_faq, _yeokgok1_head = faq_block([
    ("역곡1동은 어떤 성격의 지역인가요?",
     "역곡1동은 1호선 역곡역을 끼고 있어 상권과 주거가 함께 있으며, 서울 구로·온수와 가까워 경계 인접 이동을 함께 고려하는 지역입니다."),
    ("역곡1동은 서울 이동도 확인이 필요한가요?",
     "역곡역은 서울 온수역과 한 정거장 거리라, 방문 주소에 따라 서울 경계를 끼는 경우가 있으므로 인접권 이용과 추가 이동비 기준을 미리 확인하면 좋습니다."),
    ("역곡1동에서 가까운 역은 어디인가요?",
     "1호선 역곡역이 가장 가깝습니다. 역 양측으로 상권과 주거가 나뉘어 가까운 출구를 함께 확인하면 진입 동선이 명확해집니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/yeokgok-1-dong/",
    title="역곡1동 출장마사지｜역곡역·서울 구로·온수 인접 안내",
    desc="역곡1동 출장마사지·홈타이 예약 전 역곡역과 서울 구로·온수 인접 이동 기준을 확인하세요.",
    h1="역곡1동(원미구) 방문 관리 안내 · 역곡역·서울 인접 생활권",
    hero_badge="역곡1동 행정동 방문 관리 안내",
    hero_lead="1호선 역곡역 상권·주거와 서울 구로·온수 인접권이 함께 닿는 원미구 역곡1동의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 역곡1동 역곡역 서울 구로 온수 인접 생활권 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("역곡1동", "")],
    extra_head=_yeokgok1_head,
    body=f"""
<section><h2>역곡1동 행정동 위치 설명</h2>
<p>역곡1동은 부천 원미구 동쪽 끝에 자리한 행정동으로, 1호선 역곡역을 끼고 상권과 주거가 함께 있는 지역입니다. 역곡역 일대는 대학가·상가와 다세대·아파트 주거가 어우러져 유동인구가 꾸준하며, 서울 구로구·온수 방면과 가까워 부천과 서울의 경계 생활권 성격을 띱니다. 같은 역곡1동이라도 역 상권 쪽과 주거 골목 쪽은 진입 동선이 다르므로, 예약 전에 가까운 출구와 건물명을 함께 좁혀 확인하면 방문 주소 안내가 정확해집니다.</p>
<p>역곡역은 서울 온수역과 한 정거장 거리에 있어 행정구역상 부천이라도 실제 이동 동선이 서울 경계를 끼는 경우가 있습니다. 안쪽 주거 골목은 좁은 도로가 섞여 있어 인근 큰길과 주차 가능 위치를 미리 가늠해두면 좋습니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>역곡1동은 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 원미구의 서울 인접 생활권을 대표하는 축입니다. 원미구는 중동·신중동 상권과 상동신도시, 역곡 서울 인접권이 함께 있는 구로, 역곡1동은 그중 1호선 역곡역과 서울 경계 기능이 뚜렷한 지역에 해당합니다. 부천 전체 구·생활권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>역곡1동은 <a href="/bucheon/life/yeokgok/">역곡 생활권</a>의 중심이며, 1호선·상권·서울 인접권으로 묶입니다. 서울 구로·온수 방면은 <a href="/bucheon/life/seoul-adjacent/">서울 인접권 생활권</a>과 직접 이어지므로, 경계 구간 방문은 두 생활권 안내를 함께 보면 이동 기준을 좁히기 쉽습니다.</p></section>

<section><h2>가까운 지하철역</h2>
<p>역곡1동 예약 시 기준이 되는 역은 1호선 <a href="/bucheon/station/yeokgok-station/">역곡역</a>입니다. 역 양측으로 상권과 주거가 나뉘어 출구에 따라 진입 동선이 달라집니다. 1호선 <a href="/bucheon/station/sosa-station/">소사역</a> 방면과도 이어지므로, 역세권 페이지에서 출구별 인접 동선을 확인하면 이동이 수월합니다.</p></section>

<section><h2>인접 행정동</h2>
<p>역곡1동은 같은 역곡 생활권인 <a href="/bucheon/wonmi-gu/yeokgok-2-dong/">역곡2동</a>과 직접 인접하며, 원도심 상권권인 <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a>·<a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a>과 이어집니다. 동쪽으로는 서울 구로구·온수 방면, 남쪽으로는 소사구 역곡3동과 생활권이 맞닿으므로, 경계 구간은 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>역곡1동은 다세대·아파트 주거가 섞여 있어 <a href="/bucheon/use/home/">자택 이용</a> 시 정확한 동·호수와 건물 출입 방식 확인이 중요합니다. 역세권 상가 내 사무공간은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 기준을, 출장·여행 방문은 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책을 함께 확인하세요.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>역곡역 일대는 상권과 주거가 양측으로 나뉜 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 출구에 따라 부천 쪽과 서울 경계 쪽 동선이 갈리므로, 예약 시 가까운 출구와 건물명을 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>역곡1동은 서울 구로·온수와 한 정거장 거리로 가장 인접한 구간 중 하나입니다. 방문 주소가 서울 경계에 가까우면 실제 이동 동선이 서울 쪽으로 이어질 수 있으므로, <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("역곡1동은 역곡역 출구와 서울 경계 인접이 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 역곡1동의 위치, 역곡역 역세권, 서울 인접 생활권, 이동 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "역곡1동에서 방문형 서비스를 찾는 사용자가 역곡역 출구와 서울 경계 이동 기준을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/yeokgok-2-dong/">역곡2동</a> · <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a> · <a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a> · <a href="/bucheon/life/yeokgok/">역곡 생활권</a> · <a href="/bucheon/station/yeokgok-station/">역곡역 주변</a> · <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_yeokgok1_faq}
"""
))

# ───────── 7. 역곡2동 (yeokgok-2-dong) ─────────
_yeokgok2_faq, _yeokgok2_head = faq_block([
    ("역곡2동은 역곡1동과 무엇이 다른가요?",
     "역곡2동은 역곡역 생활권 안에서도 아파트·다세대 주거 비중이 더 높은 주거 중심 구간입니다. 자택 방문 시 단지명과 동호수 확인이 특히 중요합니다."),
    ("역곡2동은 서울 이동도 확인이 필요한가요?",
     "역곡역을 통해 서울 온수·구로와 가까워, 방문 주소에 따라 경계 인접 이동을 함께 고려하면 안내가 명확해집니다."),
    ("역곡2동에서 자택 방문은 무엇을 확인하나요?",
     "아파트 단지와 다세대가 섞여 있어 단지명·동호수와 공동현관 출입 방식, 가까운 큰길을 함께 알려주면 방문 안내가 정확해집니다."),
])
PAGES.append(page(
    path="bucheon/wonmi-gu/yeokgok-2-dong/",
    title="역곡2동 출장마사지｜역곡역 주거 생활권·서울 인접 안내",
    desc="역곡2동 출장마사지·홈타이 예약 전 역곡역 주거 생활권과 서울 인접 이동 기준을 확인하세요.",
    h1="역곡2동(원미구) 방문 관리 안내 · 역곡역 주거 생활권·서울 인접",
    hero_badge="역곡2동 행정동 방문 관리 안내",
    hero_lead="1호선 역곡역 주거 생활권에서 아파트·다세대가 어우러지고 서울 인접권이 닿는 원미구 역곡2동의 예약 전 확인사항을 안내합니다.",
    hero_alt="부천 원미구 역곡2동 역곡역 주거 생활권 서울 인접 방문형 관리 안내 이미지",
    breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), ("역곡2동", "")],
    extra_head=_yeokgok2_head,
    body=f"""
<section><h2>역곡2동 행정동 위치 설명</h2>
<p>역곡2동은 부천 원미구 동쪽에 자리한 주거 중심 행정동으로, 1호선 역곡역 생활권 안에서도 아파트와 다세대 주거 비중이 높은 지역입니다. 역곡역 상권과 이어지면서도 주거 환경이 안정적으로 형성되어 있어, 거주 인구의 생활 동선이 뚜렷합니다. 같은 역곡2동이라도 역에 가까운 구간과 안쪽 주거 단지는 진입 동선이 다르므로, 예약 전에 단지명과 가까운 큰길을 함께 좁혀 확인하면 방문 주소 안내가 정확해집니다.</p>
<p>역곡2동은 서울 구로·온수 방면과 가까워 행정구역상 부천이라도 실제 이동이 서울 경계를 끼는 경우가 있습니다. 아파트 단지는 정문·후문 위치에 따라 진입 동선이 달라지므로 단지명과 출입구를 미리 확인해두면 좋습니다.</p></section>

<section><h2>상위 구 연결</h2>
<p>역곡2동은 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 원미구의 서울 인접 주거 생활권을 대표하는 축입니다. 원미구는 중동·신중동 상권과 상동신도시, 역곡 서울 인접권이 함께 있는 구로, 역곡2동은 그중 역곡역 주거 기능이 뚜렷한 지역에 해당합니다. 부천 전체 구·생활권 구분은 <a href="/bucheon/">부천 전체 안내</a>에서 확인할 수 있습니다.</p></section>

<section><h2>가까운 생활권</h2>
<p>역곡2동은 <a href="/bucheon/life/yeokgok/">역곡 생활권</a>에 속하며, 1호선·주거·서울 인접권으로 묶입니다. 서울 구로·온수 방면은 <a href="/bucheon/life/seoul-adjacent/">서울 인접권 생활권</a>과 이어지므로, 경계 구간 방문은 두 생활권 안내를 함께 보면 이동 기준을 좁히기 쉽습니다.</p></section>

<section><h2>가까운 지하철역</h2>
<p>역곡2동 예약 시 기준이 되는 역은 1호선 <a href="/bucheon/station/yeokgok-station/">역곡역</a>입니다. 주거 구간이 넓어 단지 위치에 따라 역까지 거리가 다르므로, 가까운 출구와 큰길을 함께 확인하면 진입 동선이 명확해집니다. 1호선 <a href="/bucheon/station/sosa-station/">소사역</a> 방면과도 이어지므로 역세권 페이지에서 출구별 인접 동선을 확인하세요.</p></section>

<section><h2>인접 행정동</h2>
<p>역곡2동은 같은 역곡 생활권인 <a href="/bucheon/wonmi-gu/yeokgok-1-dong/">역곡1동</a>과 직접 인접하며, 원도심 상권권인 <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a>·<a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a>과 이어집니다. 남쪽으로는 소사구 역곡3동, 동쪽으로는 서울 구로구·온수 방면과 생활권이 맞닿으므로, 경계 구간은 방문 주소의 행정동을 정확히 확인하는 것이 좋습니다.</p></section>

<section><h2>자택·오피스텔·호텔 이용 기준</h2>
<p>역곡2동은 아파트·다세대 주거가 많아 <a href="/bucheon/use/home/">자택 이용</a> 시 단지명·동호수와 공동현관 출입 방식 확인이 가장 중요합니다. 역세권 상가 내 사무공간은 <a href="/bucheon/use/officetel/">오피스텔 이용</a> 기준을, 출장·여행 방문은 <a href="/bucheon/use/hotel/">호텔·숙소 이용</a> 정책을 함께 확인하세요.</p></section>

<section><h2>역세권 접근 기준</h2>
<p>역곡역 일대는 주거 단지가 넓게 퍼진 <a href="/bucheon/use/station-area/">역세권 이용</a> 구간입니다. 같은 역곡역이라도 단지와 출구가 다르면 진입 동선이 달라지므로, 예약 시 단지명과 가까운 출구·큰길을 함께 알려주면 방문 안내가 정확해집니다.</p></section>

<section><h2>서울·인천 인접 이동 기준</h2>
<p>역곡2동은 서울 구로·온수와 가까운 경계 생활권에 속합니다. 방문 주소가 서울 경계에 가까우면 실제 이동 동선이 서울 쪽으로 이어질 수 있으므로, <a href="/bucheon/check/travel-fee/">추가 이동비 기준</a>과 <a href="/bucheon/use/adjacent-area/">서울·인천 인접권 이용</a> 안내를 예약 전에 확인하는 것이 좋습니다.</p></section>

{checklist("역곡2동은 주거 단지 출입과 서울 경계 인접이 변수이므로 아래 항목을 먼저 확인하세요.")}

{safety_note()}

{who_how_why(
  "이 페이지는 부천 지역 방문형 관리 서비스 안내 콘텐츠 담당자가 작성하고 운영 책임자가 검수합니다.",
  "원미구 역곡2동의 위치, 역곡역 역세권, 주거 생활권, 서울 인접 이동 기준을 부천시 행정구역 기준으로 정리했습니다.",
  "역곡2동에서 방문형 서비스를 찾는 사용자가 주거 단지 출입과 서울 경계 이동 기준을 안전하게 확인하도록 돕기 위해 작성했습니다.")}

<section><h2>관련 지역 보기</h2>
<p><a href="/bucheon/wonmi-gu/">원미구 안내</a> · <a href="/bucheon/wonmi-gu/yeokgok-1-dong/">역곡1동</a> · <a href="/bucheon/wonmi-gu/simgok-1-dong/">심곡1동</a> · <a href="/bucheon/wonmi-gu/simgok-2-dong/">심곡2동</a> · <a href="/bucheon/life/yeokgok/">역곡 생활권</a> · <a href="/bucheon/station/yeokgok-station/">역곡역 주변</a> · <a href="/bucheon/use/home/">자택 이용 확인</a> · <a href="/bucheon/">부천 전체 안내</a></p></section>

{_yeokgok2_faq}
"""
))

# ════════════════════════════ STUB 페이지 (noindex) ════════════════════════════

def _stub(path, dong_name, gu_label, life_url, life_label, rep_dong_url, rep_dong_label, intro):
    return page(
        path=path,
        title=f"{dong_name} 방문 관리 안내｜원미구 {life_label}",
        desc=f"{dong_name}은 원미구 {life_label}에 속합니다. 자세한 안내는 상위 생활권·구 페이지를 확인하세요.",
        h1=f"{dong_name}(원미구) 방문 관리 안내",
        hero_badge=f"{dong_name} 행정동 안내",
        hero_lead=f"{dong_name}은 원미구 {life_label}에 속한 행정동입니다. 자세한 안내는 상위 생활권 페이지를 참고하세요.",
        hero_alt=f"부천 원미구 {dong_name} 행정동 방문형 관리 안내 이미지",
        breadcrumb=[("부천", "/bucheon/"), ("원미구", "/bucheon/wonmi-gu/"), (dong_name, "")],
        noindex=True,
        body=f"""
<section><h2>{dong_name} 개요</h2>
<p>{intro}</p>
<p>{dong_name}은 행정구역상 부천 <a href="/bucheon/wonmi-gu/">원미구</a>에 속하며, 생활권 기준으로는 {life_label}으로 묶입니다. 이 행정동은 인접 행정동과 생활권이 겹치는 구간이 많아, 방문 주소와 가까운 역·건물 출입 기준은 대표 생활권 페이지에서 통합해 안내합니다. 예약 전에는 구·생활권만이 아니라 가까운 역과 건물 출입 방식까지 함께 확인하면 방문 주소 안내가 한결 정확해집니다.</p></section>

<section><h2>상위 생활권·구 안내</h2>
<p>{dong_name}의 위치·역세권·이용 장소별 자세한 확인사항은 아래 페이지에서 확인하세요.</p>
<ul>
<li><a href="{life_url}">{life_label} 안내</a> — 대표 생활권</li>
<li><a href="{rep_dong_url}">{rep_dong_label}</a> — 대표 행정동</li>
<li><a href="/bucheon/wonmi-gu/">원미구 안내</a> — 상위 구</li>
<li><a href="/bucheon/">부천 전체 안내</a></li>
</ul>
<p>자세한 안내는 상위 생활권 페이지를 참고하세요.</p></section>
"""
    )

PAGES.append(_stub(
    "bucheon/wonmi-gu/jung-1-dong/", "중1동", "원미구",
    "/bucheon/life/jungdong-sinjungdong/", "중동·신중동 생활권",
    "/bucheon/wonmi-gu/jung-dong/", "중동 안내",
    "중1동은 7호선 신중동역 상권과 가까운 행정동으로, 상업시설과 오피스텔이 인접한 중동·신중동 생활권 안에 위치합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/jung-2-dong/", "중2동", "원미구",
    "/bucheon/life/jungdong-sinjungdong/", "중동·신중동 생활권",
    "/bucheon/wonmi-gu/jung-dong/", "중동 안내",
    "중2동은 중동 상권과 주거가 어우러진 행정동으로, 신중동역 상권 생활권과 이어지는 중동·신중동 생활권에 속합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/jung-3-dong/", "중3동", "원미구",
    "/bucheon/life/jungdong-sinjungdong/", "중동·신중동 생활권",
    "/bucheon/wonmi-gu/jung-dong/", "중동 안내",
    "중3동은 신중동 상권 외곽의 주거 구간을 포함하는 행정동으로, 중동·신중동 생활권 기준으로 위치를 확인하는 것이 좋습니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/jung-4-dong/", "중4동", "원미구",
    "/bucheon/life/jungdong-sinjungdong/", "중동·신중동 생활권",
    "/bucheon/wonmi-gu/jung-dong/", "중동 안내",
    "중4동은 중동신도시 주거와 신중동 상권이 만나는 구간의 행정동으로, 중동·신중동 생활권 안에서 위치를 좁혀 보면 정확합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/sang-1-dong/", "상1동", "원미구",
    "/bucheon/life/sangdong-bucheon-cityhall/", "상동·부천시청 생활권",
    "/bucheon/wonmi-gu/sang-dong/", "상동 안내",
    "상1동은 상동신도시 단지와 부천시청 생활권에 인접한 행정동으로, 계획형 주거·상권이 어우러진 상동·부천시청 생활권에 속합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/sang-2-dong/", "상2동", "원미구",
    "/bucheon/life/sangdong-bucheon-cityhall/", "상동·부천시청 생활권",
    "/bucheon/wonmi-gu/sang-dong/", "상동 안내",
    "상2동은 상동신도시 주거 단지를 중심으로 하는 행정동으로, 부천시청역 생활권과 이어지는 상동·부천시청 생활권에 속합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/sang-3-dong/", "상3동", "원미구",
    "/bucheon/life/sangdong-bucheon-cityhall/", "상동·부천시청 생활권",
    "/bucheon/wonmi-gu/sang-dong/", "상동 안내",
    "상3동은 상동신도시 동쪽 인천 부평 인접 구간을 포함하는 행정동으로, 상동·부천시청 생활권 기준으로 위치를 확인하는 것이 좋습니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/simgok-3-dong/", "심곡3동", "원미구",
    "/bucheon/life/bucheon-station-simgok/", "부천역·심곡 생활권",
    "/bucheon/wonmi-gu/simgok-1-dong/", "심곡1동 안내",
    "심곡3동은 1호선 부천역 원도심 상권과 주거가 섞인 행정동으로, 다세대·상가가 밀집한 부천역·심곡 생활권에 속합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/wonmi-1-dong/", "원미1동", "원미구",
    "/bucheon/life/bucheon-station-simgok/", "부천역·심곡 생활권",
    "/bucheon/wonmi-gu/simgok-1-dong/", "심곡1동 안내",
    "원미1동은 부천역 원도심과 중동 사이에 위치한 주거 중심 행정동으로, 부천역·심곡 생활권 기준으로 위치를 좁혀 확인하면 정확합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/wonmi-2-dong/", "원미2동", "원미구",
    "/bucheon/life/jungdong-sinjungdong/", "중동·신중동 생활권",
    "/bucheon/wonmi-gu/jung-dong/", "중동 안내",
    "원미2동은 부천역 원도심과 중동 상권 사이의 주거 구간을 포함하는 행정동으로, 중동·신중동 생활권과 부천역 생활권이 함께 닿습니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/dodang-dong/", "도당동", "원미구",
    "/bucheon/life/chunui-bucheon-stadium/", "춘의·부천종합운동장 생활권",
    "/bucheon/wonmi-gu/chunui-dong/", "춘의동 안내",
    "도당동은 부천종합운동장·춘의 일대와 가까운 행정동으로, 환승·차량 이동 성격이 있는 춘의·부천종합운동장 생활권에 속합니다."))

PAGES.append(_stub(
    "bucheon/wonmi-gu/yakdae-dong/", "약대동", "원미구",
    "/bucheon/life/jungdong-sinjungdong/", "중동·신중동 생활권",
    "/bucheon/wonmi-gu/jung-dong/", "중동 안내",
    "약대동은 중동 상권과 부천역 원도심 사이에 위치한 행정동으로, 중동·신중동 생활권과 부천역 생활권이 함께 닿는 구간입니다."))
