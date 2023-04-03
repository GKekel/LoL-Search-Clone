import requests
import os

API_KEY = os.getenv('API_KEY')

# %%

# API_KEY = "YOUR_API_KEY_HERE"
REGION = "na1"
SUMMONER_NAME = "Jhinatalia"


def fetch_summoner_data(summoner_name, region):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {
        "X-Riot-Token": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return (data)
    else:
        return ("Error:", response.status_code, response.text)
