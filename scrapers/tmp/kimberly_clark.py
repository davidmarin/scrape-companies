from ..common import get_soup

NAME = 'Kimberly-Clark'

_START_URL = 'http://www.kimberly-clark.com/ourbrands.aspx'

# for now, only saving US brands
_COUNTRY = 'United States'

_SKIP_SECTIONS = [
    'Kimberly-Clark Health Care',
    'Kimberly-Clark Professional',
]

# grabbed by hand from http://www.kchealthcare.com/products.aspx
_HEALTH_CARE_BRANDS = [
    'KIMVENT',
    'MIC',
    'MIC-KEY',
]

# grabbed by hand from
# http://www.kimberly-clark.com/brands/kc_professional.aspx
_PROFESSIONAL_BRANDS = [
    'Wypall',
    'Kimtech',
    'Kleenguard',
    'Jackson Safety',
]

def scrape_brands():
    yield NAME
    for brand in _HEALTH_CARE_BRANDS + _PROFESSIONAL_BRANDS:
        yield brand

    start_soup = get_soup(_START_URL)

    urls = [a['href'] for a in start_soup.select('#nav li a')
            if a.text.strip() not in _SKIP_SECTIONS]

    for url in urls:
        soup = get_soup(url)
        for h3 in soup.select('.accordion h3'):
            brand = h3.text
            if any(a.text.strip() == _COUNTRY
                   for a in h3.findNext('div').select('a')):
                yield brand
