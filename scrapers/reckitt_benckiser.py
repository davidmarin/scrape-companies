from bs4 import BeautifulSoup
import scraperwiki


COMPANY = u'Reckitt-Benckiser'


START_URL = 'http://www.rb.com/ourbrands/search-rb-brands-a-z/a-f'

MORE_BRANDS = [
    COMPANY,
    u'Reckitt',
    #u'Reckitt & Benckiser',  # appears on amazon, but not really legit
]


def scrape_brands():

    for brand in MORE_BRANDS:
        yield brand

    start_soup = BeautifulSoup(scraperwiki.scrape(START_URL))

    urls = [a['href'] for a in start_soup.select('li.active_ancestor_2 li a')]

    for url in urls:
        if url == START_URL:
            soup = start_soup
        else:
            soup = BeautifulSoup(scraperwiki.scrape(url))

        for fp in soup.select('div.featuredproduct'):
            h2 = fp.h2
            if h2 and h2.text:
                # TODO: for now, just getting US brands
                if 'USA' in fp.text:
                    brand = h2.text.strip()
                    if '/' in brand:  # Lysol/Lizol
                        # TODO: This doesn't handle Glen 10/20 (AU) right
                        # (should be "Glen 10", "Glen 20")
                        for part in brand.split('/'):
                                yield part
                    else:
                        yield brand
