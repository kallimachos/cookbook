import requests
from concurrent.futures import ThreadPoolExecutor


def get_url(url):
    return requests.get(url)


urls = ["http://www.jython.org", "http://olympus.realpython.org/dice"] * 100

with ThreadPoolExecutor() as ex:
    results = ex.map(get_url, urls)

for result in results:
    print(result.url)
