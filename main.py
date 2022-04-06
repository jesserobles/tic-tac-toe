from game import Game
from players import random_player, query_player, minmax_player, alpha_beta_player, alpha_beta_depth_limited_player

game = Game(3,3,3)
# game.play_game(query_player, alpha_beta_player)
# game.play_game(alpha_beta_player, alpha_beta_player)
game.play_game(alpha_beta_depth_limited_player, alpha_beta_depth_limited_player, max_depth=12)