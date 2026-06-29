# 부천시 출장마사지(간다GO) 사이트 공통 설정

# 배포 전 실제 도메인으로 교체하세요.
BASE_URL = "https://bucheon-massage.pages.dev"

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
    ("부천 홈", "/bucheon/", []),
    ("구별 안내", "/bucheon/wonmi-gu/", [
        ("부천 전체", "/bucheon/"),
        ("원미구", "/bucheon/wonmi-gu/"),
        ("소사구", "/bucheon/sosa-gu/"),
        ("오정구", "/bucheon/ojeong-gu/"),
    ]),
    ("행정동 안내", "/bucheon/wonmi-gu/jung-dong/", [
        ("중동", "/bucheon/wonmi-gu/jung-dong/"),
        ("상동", "/bucheon/wonmi-gu/sang-dong/"),
        ("춘의동", "/bucheon/wonmi-gu/chunui-dong/"),
        ("소사본동", "/bucheon/sosa-gu/sosabon-dong/"),
        ("송내1동", "/bucheon/sosa-gu/songnae-1-dong/"),
        ("범박동", "/bucheon/sosa-gu/beombak-dong/"),
        ("원종1동", "/bucheon/ojeong-gu/wonjong-1-dong/"),
        ("고강본동", "/bucheon/ojeong-gu/gogangbon-dong/"),
    ]),
    ("생활권", "/bucheon/life/jungdong-sinjungdong/", [
        ("부천역·심곡", "/bucheon/life/bucheon-station-simgok/"),
        ("중동·신중동", "/bucheon/life/jungdong-sinjungdong/"),
        ("상동·부천시청", "/bucheon/life/sangdong-bucheon-cityhall/"),
        ("송내", "/bucheon/life/songnae/"),
        ("역곡", "/bucheon/life/yeokgok/"),
        ("소사·소사본", "/bucheon/life/sosa-sosabon/"),
        ("범박·옥길", "/bucheon/life/beombak-okgil/"),
        ("춘의·종합운동장", "/bucheon/life/chunui-bucheon-stadium/"),
        ("원종·고강", "/bucheon/life/wonjong-gogang/"),
        ("오정·신흥", "/bucheon/life/ojeong-sinheung/"),
    ]),
    ("지하철역", "/bucheon/station/bucheon-station/", [
        ("부천역", "/bucheon/station/bucheon-station/"),
        ("중동역", "/bucheon/station/jungdong-station/"),
        ("신중동역", "/bucheon/station/sinjungdong-station/"),
        ("부천시청역", "/bucheon/station/bucheon-cityhall-station/"),
        ("상동역", "/bucheon/station/sangdong-station/"),
        ("송내역", "/bucheon/station/songnae-station/"),
        ("역곡역", "/bucheon/station/yeokgok-station/"),
        ("소사역", "/bucheon/station/sosa-station/"),
        ("부천종합운동장역", "/bucheon/station/bucheon-stadium-station/"),
        ("춘의역", "/bucheon/station/chunui-station/"),
        ("까치울역", "/bucheon/station/kkachiwool-station/"),
        ("원종역", "/bucheon/station/wonjong-station/"),
    ]),
    ("이용 장소", "/bucheon/use/home/", [
        ("자택 이용", "/bucheon/use/home/"),
        ("호텔·숙소 이용", "/bucheon/use/hotel/"),
        ("오피스텔 이용", "/bucheon/use/officetel/"),
        ("역세권 이용", "/bucheon/use/station-area/"),
        ("야간 예약", "/bucheon/use/night/"),
        ("신도시 생활권 이용", "/bucheon/use/newtown/"),
        ("서울·인천 인접권", "/bucheon/use/adjacent-area/"),
        ("외곽 지역 이용", "/bucheon/use/outer-area/"),
    ]),
    ("예약 전 확인", "/bucheon/check/address/", [
        ("방문 주소 확인", "/bucheon/check/address/"),
        ("건물 출입 방식", "/bucheon/check/building-access/"),
        ("추가 이동비 기준", "/bucheon/check/travel-fee/"),
        ("예약 가능 시간", "/bucheon/check/time/"),
        ("예약 변경 기준", "/bucheon/check/change-policy/"),
        ("개인정보 처리 기준", "/bucheon/check/privacy/"),
        ("불법·선정적 서비스 불가", "/bucheon/check/service-policy/"),
        ("고객 유의사항", "/bucheon/check/customer-notice/"),
    ]),
    ("문의하기", TELEGRAM, []),
]
