import requests


def get_player_season_stats(year):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=1000"
    response = requests.get(url, verify=False)
    return response.json()




