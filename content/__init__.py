from . import (root, main, districts, life_areas, stations,
               admin_wonmi, admin_sosa, admin_ojeong,
               use_cases, checks, policies)

PAGES = (
    [root.PAGE] +
    [main.PAGE] +
    districts.PAGES +
    life_areas.PAGES +
    stations.PAGES +
    admin_wonmi.PAGES +
    admin_sosa.PAGES +
    admin_ojeong.PAGES +
    use_cases.PAGES +
    checks.PAGES +
    policies.PAGES
)
