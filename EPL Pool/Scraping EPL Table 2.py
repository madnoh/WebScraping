"""
Python code snippets vol 40.
xxx-Scrape Football Premier League Table.

By Steve Shambles Nov 2019, with help from r/learnpython/reddit.
stevepython.wordpress.com """

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.skysports.com/premier-league-table')
soup = BeautifulSoup(r.text, 'html.parser')
league_table = soup.find('table', class_='standing-table__table callfn')

print("Team                         Pl  W  D  L  F  A GD Pts")

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')

    for row in rows:
        rank = row.find_all('td', class_='standing-table__cell')[0].text
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name')
        pl_team = pl_team['data-long-name']
        games_played = row.find_all('td', class_='standing-table__cell')[2].text
        games_won = row.find_all('td', class_='standing-table__cell')[3].text
        games_drawn = row.find_all('td', class_='standing-table__cell')[4].text
        games_lost = row.find_all('td', class_='standing-table__cell')[5].text
        goals_for = row.find_all('td', class_='standing-table__cell')[6].text
        goals_against = row.find_all('td', class_='standing-table__cell')[7].text
        goal_diff = row.find_all('td', class_='standing-table__cell')[8].text
        total_points = row.find_all('td', class_='standing-table__cell')[9].text

        # Need 25 spaces after pl_team to format table for printing.
        space_pad = 25 - len(pl_team)
        pl_team = pl_team + " " * space_pad

        # If single figure, pad with a space to format table.
        if int(games_won) < 10:
            games_won = " " + str(games_won)

        if int(games_drawn) < 10:
            games_drawn = " " + str(games_drawn)

        if int(games_lost) < 10:
            games_lost = " " + str(games_lost)

        if int(goals_for) < 10:
            goals_for = " " + str(goals_for)

        if int(goals_against) < 10:
            goals_against = " " + str(goals_against)

        if int(goal_diff) < 10 and int(goal_diff) >= 0:
            goal_diff = " " + str(goal_diff)

        if int(rank) < 10:
            rank = " " + str(rank)

        # Print table in shell.
        print(rank, pl_team, games_played, games_won, games_drawn, games_lost,
              goals_for, goals_against, goal_diff, total_points)