# -*- coding: utf-8 -*-
from urlparse import urljoin

from srs.scrape import scrape_soup



COMPANY = u'Nestlé'

R_AND_TM = u'®™'

START_URL = 'http://www.nestleusa.com/brands'

SKIP_LINKS = ['websites']


def scrape_brands():
    yield COMPANY

    start_soup = scrape_soup(START_URL)

    urls = [urljoin(START_URL, a['href'])
            for a in start_soup.select('#sNavigation a')
            if a.text.strip().lower() not in SKIP_LINKS]

    for url in urls:
        soup = scrape_soup(url)

        for a in soup.select('.brandCarousel a'):
            href = a['href']
            # weirdly, brand is only available in the URL fragment
            if href.startswith('#'):
                href = href[1:]
            if '|' in href:
                href = href[:href.index('|')]

            # stop at the (r)/(tm)
            for c in R_AND_TM:
                if c in href:
                    href = href[:href.index(c)]

            yield href
