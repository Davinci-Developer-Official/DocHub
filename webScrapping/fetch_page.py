import requests

def fetch_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text