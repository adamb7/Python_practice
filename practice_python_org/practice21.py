import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")

out = soup.find_all("h2", "story-heading")
for m in range(len(out)):
    print(out[m].getText())

with open("pelda.txt", "w") as open_file:
    for m in range(len(out)):
        open_file.write(out[m].getText())
