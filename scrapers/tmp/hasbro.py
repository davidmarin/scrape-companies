from ..common import get_soup


COMPANY = u'Hasbro'

ALL_BRANDS_URL = 'http://www.hasbro.com/shop/brandlist.cfm'


# these are licensed by multiple companies
LICENSED_BRANDS = [
    'Angry Birds',
    'Captain America',
    'Disney',
    'Disney Princesses',
    'Elmo',
    'Incredible Hulk',
    'Iron Man',
    'Marvel',
    'Marvel Universe',
    'Sesame Street',
    'Star Trek',
    'Star Wars',  # Star Wars Jedi Force seems to be exclusively Hasbro
    'The Avengers',
    'Thor',
    'Wolverine',
    'Zynga',
]


def scrape_brands():
    yield COMPANY

    soup = get_soup(ALL_BRANDS_URL)

    for a in soup.select('#hsb_shop_bl_container li ul li a'):
        brand = a.text
        if brand not in LICENSED_BRANDS:
            yield brand
