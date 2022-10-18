import cloudscraper


def bypass(url, referer='https://google.com'):
    scraper = cloudscraper.CloudScraper()

    return scraper.get(
        url,
        headers={'referer': referer},
        timeout=3,
    )
