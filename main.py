from game import Game
from players import random_player, query_player, minmax_player, alpha_beta_player

game = Game(4,4,4)
game.play_game(query_player, random_player)
# game.play_game(random_player,minmax_player)