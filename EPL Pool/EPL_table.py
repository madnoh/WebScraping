import requests
import json

url = "https://api.football-data.org/v2/competitions/2021/standings?standingType=TOTAL"
headers = {"X-Auth-Token" : "f51a776af9e642e184a42921d3f24828"}
r = requests.get(url, headers = headers)

# response = json.load(r)
print(r)