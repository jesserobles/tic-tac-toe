from collections import defaultdict
import json

import requests
from requests.exceptions import HTTPError


class APIPlayer:
    def __init__(self, apikeyfile='apikey.json', team_id=1290, team_name="Team 6", game_id=None) -> None:
        self.team_id = team_id
        self.team_name = team_name
        self.game_id = game_id
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
        self.move_id_cache = []

    def validate_response(func):
        """
        A decorator to validate the responses for the methods in this class.
        It simply checks that code=OK.
        """
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
        r = requests.post(self.url, headers=self.HEADERS, data=data)
        self.game_id = r.json()['gameId']
        return r

    @validate_response
    def get_my_games(self):
        return requests.get(self.url, headers=self.HEADERS, params={"type": "myGames"})

    @validate_response
    def move(self, x, y):
        data = {
            "type": "move",
            "teamId": self.team_id,
            "move": f"{x},{y}",
            "gameId": self.game_id

        }

        return requests.post(self.url, headers=self.HEADERS, data=data)


    @validate_response
    def get_moves(self, count=1000):
        """
        Sample response:
        {
            "moves": [
                {
                    "moveId": "86727",
                    "gameId": "3302",
                    "teamId": "1290",
                    "move": "4,4",
                    "symbol": "O",
                    "moveX": "4",
                    "moveY": "4"
                }
            ],
            "code": "OK"
        }
        """
        params = {
            "type": "moves",
            "gameId": self.game_id,
            "count": count
        }
        return requests.get(self.url, headers=self.HEADERS, params=params)
    
    def get_move(self, state):
        pass

    @validate_response
    def get_board_string(self):
        params = {
            "gameId": self.game_id,
            "type": "boardString"
        }
        return requests.get(self.url, headers=self.HEADERS, params=params)

    @validate_response
    def get_board_map(self):
        params = {
            "type": "boardMap",
            "gameId": self.game_id
        }
        return requests.get(self.url, headers=self.HEADERS, params=params)
    
    def parse_moves(self, moves):
        """
        moves = [
                {
                    "moveId": "86727",
                    "gameId": "3302",
                    "teamId": "1290",
                    "move": "4,4",
                    "symbol": "O",
                    "moveX": "4",
                    "moveY": "4"
                }
            ]
        """
        parsed_moves = []
        for move in moves:
            if not int(move["teamId"]) != self.team_id:
                parsed_moves.append((int(move['moveX']), int(move['moveY'])))
        return parsed_moves

    def add_move_to_cache(self, move_id):
        self.move_id_cache.append(move_id)

    def get_move_id_cache(self):
        return self.move_id_cache