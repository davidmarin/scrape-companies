# -*- coding: utf-8 -*-
import json

from srs.scrape import scrape_soup


# TODO: scrape all countries, not just U.S.
# will probably want to use U.S. category names (match on color)

COMPANY = 'Unilever'

# this page says Unilever has "more than 1000 brands" (!)
URLS = [
    'http://www.unilever.com/brands-in-action/view-brands.aspx?view=AtoZ',
    'http://www.unileverusa.com/brands-in-action/view-brands.aspx?view=AtoZ',
]


# Best Foods is an alternate name for Hellmann's (mayo)
# Marmite and PG Tips are U.K. brands available in the U.S.
#
# TODO: just scrape from the U.K. page, and let people make a reasonable
# guess that U.K. brands might be available from U.S. websites.
EXTRA_BRANDS = {
    'Best Foods': 'Food and drink',
    'Marmite': 'Food and drink',
    'PG Tips': 'Food and drink',
}


def scrape_brands():
    yield COMPANY
    for brand, category in sorted(EXTRA_BRANDS.items()):
        yield {'brand': brand, 'category': category}

    for url in URLS:
        soup = scrape_soup(url)

        key_to_cat = dict((a['data-filter'], a.text)
                          for a in soup.select('div.boxSellcontent a'))

        for div in soup.select('.zlist'):
            cat_keys = json.loads(div['data-category'])['c']
            categories = [key_to_cat[k] for k in cat_keys]

            brands = div.find('span', class_='title').text.split(', ')
            for brand in brands:
                yield {'brand': brand, 'categories': categories}
