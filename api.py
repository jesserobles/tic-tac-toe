import json

import requests
from requests.exceptions import HTTPError

# def validate_response(func):
#     def wraps(*args, **kwargs):
#         response = func(*args, **kwargs)
#         payload = response.json()
#         if payload["code"] != "OK":
#             raise HTTPError(f"Received unexpected code: {payload['code']}")
#         return response
#     return wraps

class APIPlayer:
    def __init__(self, apikeyfile='apikey.json', team_id=1290, team_name="Team 6") -> None:
        self.team_id = team_id
        self.team_name = team_name
        with open(apikeyfile, 'r') as file:
            apipayload = json.load(file)
        self.url = apipayload['url']
        self.user_id = apipayload['user_id']
        self.key = apipayload['key']
        self.HEADERS = {
            'x-api-key': self.key,
            'userid': self.user_id,
            'User-Agent': 'AI-Students' # Server throws security exception if this isn't set.
        }

    def validate_response(func):
        """A decorator to validate the responses for the methods."""
        def wraps(*args, **kwargs):
            response = func(*args, **kwargs)
            payload = response.json()
            if payload["code"] != "OK":
                raise HTTPError(f"Received unexpected code: {payload['code']}")
            return response
        return wraps

    @validate_response
    def list_my_teams(self):
        params = {'type': 'myTeams'}
        return requests.get(self.url, headers=self.HEADERS, params=params)
    
    @validate_response
    def create_team(self):
        """
        Sample response: {"code": "OK", "teamId": 1290}
        """
        data = {
            "type": "team",
            "name": self.team_name
        }
        return requests.post(self.url, headers=self.HEADERS, data=data)

    @validate_response
    def add_team_member(self, user_id):
        data = {"type": "member", "teamId": self.team_id, "userId": user_id}
        return requests.post(self.url, headers=self.HEADERS, data=data)

    @validate_response
    def create_game(self, opponent_id, board_size=3, target=3):
        """
        Sample response {"code": "OK", "gameId": 3302}
        """
        data = {
            "type": "game",
            "teamId1": self.team_id,
            "teamId2": opponent_id,
            "gameType": "TTT",
            "boardSize": board_size,
            "target": target
        }
        return requests.post(self.url, headers=self.HEADERS, data=data)

    @validate_response
    def get_my_games(self):
        return requests.get(self.url, headers=self.HEADERS, params={"type": "myGames"})

    @validate_response
    def move(self, game_id, x, y):
        data = {
            "type": "move",
            "teamId": self.team_id,
            "move": f"{x},{y}",
            "gameId": game_id

        }
        return requests.post(self.url, headers=self.HEADERS, data=data)

    @validate_response
    def get_moves(self, game_id, count=20):
        params = {
            "type": "moves",
            "gameId": game_id,
            "count": count
        }
        return requests.get(self.url, headers=self.HEADERS, params=params)

    @validate_response
    def get_board_string(self, game_id):
        params = {
            "gameId": game_id,
            "type": "boardString"
        }
        return requests.get(self.url, headers=self.HEADERS, params=params)

    @validate_response
    def get_board_map(self, game_id):
        params = {
            "type": "boardMap",
            "gameId": game_id
        }
        return requests.get(self.url, headers=self.HEADERS, params=params)