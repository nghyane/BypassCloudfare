import cloudscraper


def bypass(url, referer='https://google.com'):
    scraper = cloudscraper.create_scraper()

    return scraper.get(
        url,
        headers={'referer': referer},
        timeout=3,

    )
