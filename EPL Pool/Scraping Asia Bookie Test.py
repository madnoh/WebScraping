import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata


soup = make_soup('http://www.asiabookie.info/epl.html')

for record in soup.find_all('tr'):
    matches = ''
    for data in record.find_all('td'):
        matches = matches + ',' + data.text




