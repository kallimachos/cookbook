"""Multithread."""

from concurrent.futures import ThreadPoolExecutor

import requests


def get_url(url):
    """Get URL."""
    return requests.get(url)


urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100

with ThreadPoolExecutor() as ex:
    results = ex.map(get_url, urls)

for _result in results:
    pass
