import json

import requests

with open('apikey.json', 'r') as file:
    apikey = json.load(file)

url = apikey['url']
user_id = apikey['user_id']
key = apikey['key']
HEADERS = {
    'x-api-key': key,
    'userid': user_id,
    'User-Agent': 'AI-Students' # Server throws security exception if this isn't set.
}

# List my teams
def list_my_teams(url, headers):
    params = {'type': 'myTeams'}
    return requests.get(url, headers=headers, params=params)

# Create a team
def create_team(team_name, url, headers):
    data = {
        "type": "team",
        "name": "Team 6"
    }
    return requests.post(url, headers=headers, data=data) # Currently Failing!

# Add a team member
def add_team_member(team_id, user_id, url, headers):
    data = {"type": "member", "teamId": team_id, "userId": user_id}
    return requests.post(url, headers=headers, data=data)

# Create a game
def create_game(team_id_1, team_id_2, url, headers, board_size=12, target=6):
    data = {
        "type": "game",
        "teamId1": team_id_1,
        "teamId2": team_id_2,
        "gameType": "TTT",
        "boardSize": board_size,
        "target": target
    }
    return requests.post(url, headers=headers, data=data)

def get_my_games(url, headers):
    return requests.get(url, headers=headers, params={"type": "myGames"}).json()

def move(x, y, url, headers, team_id, game_id):
    data = {
        "type": "move",
        "teamId": team_id,
        "move": f"{x},{y}",
        "gameId": game_id

    }
    return requests.post(url, headers=headers, data=data)

def get_moves(game_id, url, headers, count=20):
    params = {
        "type": "moves",
        "gameId": game_id,
        "count": count
    }
    return requests.get(url, headers=headers, params=params)

def get_board_string(game_id, url, headers):
    params = {
        "gameId": game_id,
        "type": "boardString"
    }
    return requests.get(url, headers=headers, params=params)

def get_board_map(game_id, url, headers):
    params = {
        "type": "boardMap",
        "gameId": game_id
    }
    return requests.get(url, headers=headers, params=params)