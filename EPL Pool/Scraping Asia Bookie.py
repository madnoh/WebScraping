import requests
from bs4 import BeautifulSoup

def makeSoup(url):
    '''Template function for creating soup from url'''
    result = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
    soupdata = BeautifulSoup(result.content, 'lxml')
    return soupdata

soup = makeSoup('http://www.asiabookie.info/epl.html')

print(soup.prettify())
'''for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    print(tds[0].text, tds[1].text, tds[2].text, tds[3].text)'''