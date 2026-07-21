import requests
from bs4 import BeautifulSoup

URL = "https://sqlite.org/pragma.html#pragma_foreign_keys"

def fetch_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_page(html):
    soup = BeautifulSoup(html,"html.parser")
    title = soup.find("h1").get_text(strip=True)
    paragraphs = [p.get_text("",strip=True) for p in soup.find_all("p")]
    return {"title":title,"paragraphs":paragraphs}

if __name__ == "__main__":
    html = fetch_page(URL)
    data = parse_page(html)
    print("Title:",data["title"])
    print("Paragraphs found:", len(data["paragraphs"]))
    # print(data["paragraphs"],[0][:200])