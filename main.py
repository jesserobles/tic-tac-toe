from game import Game
from players import alpha_beta_depth_limited_player
import sys
import json

config_file = sys.argv[1]
with open(config_file, 'r') as file:
    config = json.load(file)

game = Game(config['board_size'], config['board_size'], config['target'])

game.play_api(
    player=alpha_beta_depth_limited_player,
    id=config['id'],
    opponent_id=config['opponent_id'],
    apikeyfile=config['api_key_file'],
    first=config['move_first'],
    game_id=config['game_id'],
    board_size=config['board_size'],
    target=config['target']
)
