import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = soup.find_all('p')
    text = ' '.join([p.get_text() for p in content])
    return text
