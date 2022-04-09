from game import Game
from players import random_player, query_player, minmax_player, alpha_beta_player, alpha_beta_depth_limited_player
import sys
import json

config_file = sys.argv[1]
with open(config_file, 'r') as file:
    config = json.load(file)

game = Game(3,3,3)
# game.play_game(alpha_beta_depth_limited_player, query_player, max_depth=12)
game.play_api(
    player=alpha_beta_depth_limited_player,
    id=config['id'],
    opponent_id=config['opponent_id'],
    apikeyfile=config['api_key_file'],
    first=config['move_first'],
    game_id=config['game_id']
)
