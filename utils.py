import requests
import time

def make_request(url, method='GET', headers=None, params=None, data=None):
    try:
        response = requests.request(
            method, url, headers=headers, params=params, data=data)
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API request: {e}")
        return None

def replay_game():
    while True:
        data = make_request("https://replay.sportsdata.io/api/v3/nfl/stats/json/boxscoresdeltav3/2023reg/6/fantasy/all?key=1d90bc5e5aeb4b00be574e57586e744f")

        yield data[0]["Score"]

        time.sleep(5)

replay_game()