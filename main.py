from game import Game
from players import random_player, query_player, expect_min_max_player, alpha_beta_player

Tictactoe = Game(3,3,3)
Tictactoe.play_game(dict(X=random_player,O=alpha_beta_player))