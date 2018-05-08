from bs4 import BeautifulSoup
import requests

r = requests.get("https://boston.craigslist.org/search/sof")

soup = BeautifulSoup(r.text, 'lxml')

attr = {
    'class':'result-title hdrlnk'
}
results = []
urls = soup.find_all('a', attrs=attr)
for url in urls:
    results.append((url.text, url['href']))
    print("Job:", url.text)
    print("URL:", url['href'])
    print()
