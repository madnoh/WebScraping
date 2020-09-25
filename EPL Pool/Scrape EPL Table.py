import requests
from bs4 import BeautifulSoup

def makeSoup(url):
    '''Template function for creating soup from url'''
    result = requests.get(url)
    soupdata = BeautifulSoup(result.content, 'html.parser')
    return soupdata

soup = makeSoup('https://www.sportinglife.com/football/league-tables')

stat_table = soup.find_all('table')
stat_table = stat_table[0]

stats = []
for record in stat_table.find_all('tr'):
    for data in record.find_all('td'):
        stats.append(data.text)

header = ['Position', 'Team', 'Played', 'Won', 'Drew', 'Lost', 'For', 'Against', 'Goal Difference', 'Points']
indx = 0
for head in header:
    stats.insert(indx, head)
    indx += 1

with open('Raw table.csv', 'w') as f:
    for stat in stats:
        f.write(stat)
        f.write(',')