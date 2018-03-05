import requests
from bs4 import BeautifulSoup


def print_website(url):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "html.parser")
    out = soup.find_all("p")
    for i in range(len(out)):
        print(out[i].text)


url1 = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html'
url2 = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749_2.html'
print_website(url1)
print_website(url2)