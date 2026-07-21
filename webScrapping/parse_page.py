from bs4 import BeautifulSoup

def parse_page(html):
    soup = BeautifulSoup(html,"html.parser")
    title = soup.find("h1").get_text(strip=True)
    paragraphs = [p.get_text("",strip=True) for p in soup.find_all("p")]
    return {"title":title,"paragraphs":paragraphs}
