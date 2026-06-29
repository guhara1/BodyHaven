# 루트 페이지 (/) — 부천 메인(/bucheon/)으로 리다이렉트
from .components import page

PAGE = page(
    path="",
    title="부천 출장마사지｜간다GO 원미·소사·오정 생활권 안내",
    desc="부천 출장마사지·홈타이 예약 전 원미구·소사구·오정구 생활권과 역세권을 확인하세요.",
    h1="부천 출장마사지",
    breadcrumb=[],
    body='<section><h2>부천 출장마사지 안내</h2>'
         '<meta http-equiv="refresh" content="0;url=/bucheon/">'
         '<p>부천 출장마사지 안내 페이지로 이동합니다. 자동으로 이동하지 않으면 '
         '<a href="/bucheon/">여기를 클릭</a>하세요.</p></section>',
    noindex=True,
)
