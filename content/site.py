# 부천시 출장마사지(간다GO) 사이트 공통 설정

# 배포 전 실제 도메인으로 교체하세요.
BASE_URL = "https://bodyhaven.netlify.app"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"
SITE_TAGLINE = "부천시 전지역 방문 관리"
AREA_SERVED = "경기도 부천시"

# 푸터 텔레그램(웹사이트 제작문의·제휴문의·문의하기)
TELEGRAM = "https://t.me/googleseolab"

# 기본 OG/대표 이미지(요청 시 실제 파일로 교체)
DEFAULT_OG_IMAGE = "/assets/og-image.png"

# 상단 메뉴 — 메뉴명에 "출장마사지" 반복 금지(스팸 방지), 지역명·기능명만 표시
NAV = [
    ("부천 홈", "/", []),
    ("구별 안내", "/wonmi-gu/", [
        ("부천 전체", "/"),
        ("원미구", "/wonmi-gu/"),
        ("소사구", "/sosa-gu/"),
        ("오정구", "/ojeong-gu/"),
    ]),
    ("행정동 안내", "/wonmi-gu/jung-dong/", [
        ("중동", "/wonmi-gu/jung-dong/"),
        ("상동", "/wonmi-gu/sang-dong/"),
        ("춘의동", "/wonmi-gu/chunui-dong/"),
        ("소사본동", "/sosa-gu/sosabon-dong/"),
        ("송내1동", "/sosa-gu/songnae-1-dong/"),
        ("범박동", "/sosa-gu/beombak-dong/"),
        ("원종1동", "/ojeong-gu/wonjong-1-dong/"),
        ("고강본동", "/ojeong-gu/gogangbon-dong/"),
    ]),
    ("생활권", "/life/jungdong-sinjungdong/", [
        ("부천역·심곡", "/life/bucheon-station-simgok/"),
        ("중동·신중동", "/life/jungdong-sinjungdong/"),
        ("상동·부천시청", "/life/sangdong-bucheon-cityhall/"),
        ("송내", "/life/songnae/"),
        ("역곡", "/life/yeokgok/"),
        ("소사·소사본", "/life/sosa-sosabon/"),
        ("범박·옥길", "/life/beombak-okgil/"),
        ("춘의·종합운동장", "/life/chunui-bucheon-stadium/"),
        ("원종·고강", "/life/wonjong-gogang/"),
        ("오정·신흥", "/life/ojeong-sinheung/"),
    ]),
    ("지하철역", "/station/bucheon-station/", [
        ("부천역", "/station/bucheon-station/"),
        ("중동역", "/station/jungdong-station/"),
        ("신중동역", "/station/sinjungdong-station/"),
        ("부천시청역", "/station/bucheon-cityhall-station/"),
        ("상동역", "/station/sangdong-station/"),
        ("송내역", "/station/songnae-station/"),
        ("역곡역", "/station/yeokgok-station/"),
        ("소사역", "/station/sosa-station/"),
        ("부천종합운동장역", "/station/bucheon-stadium-station/"),
        ("춘의역", "/station/chunui-station/"),
        ("까치울역", "/station/kkachiwool-station/"),
        ("원종역", "/station/wonjong-station/"),
    ]),
    ("이용 장소", "/use/home/", [
        ("자택 이용", "/use/home/"),
        ("호텔·숙소 이용", "/use/hotel/"),
        ("오피스텔 이용", "/use/officetel/"),
        ("역세권 이용", "/use/station-area/"),
        ("야간 예약", "/use/night/"),
        ("신도시 생활권 이용", "/use/newtown/"),
        ("서울·인천 인접권", "/use/adjacent-area/"),
        ("외곽 지역 이용", "/use/outer-area/"),
    ]),
    ("예약 전 확인", "/check/address/", [
        ("방문 주소 확인", "/check/address/"),
        ("건물 출입 방식", "/check/building-access/"),
        ("추가 이동비 기준", "/check/travel-fee/"),
        ("예약 가능 시간", "/check/time/"),
        ("예약 변경 기준", "/check/change-policy/"),
        ("개인정보 처리 기준", "/check/privacy/"),
        ("불법·선정적 서비스 불가", "/check/service-policy/"),
        ("고객 유의사항", "/check/customer-notice/"),
    ]),
    ("문의하기", TELEGRAM, []),
]
