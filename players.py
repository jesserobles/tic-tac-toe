import random
from time import sleep
from alphabeta import alpha_beta_depth_limited_search

from api import APIPlayer
from minimax import minimax_search, alpha_beta_search

def query_player(game, state):
    """Make a move by querying standard input."""
    print("current state:")
    game.display(state)
    print("available moves: {}".format(game.actions(state)))
    print("")
    move = None
    if game.actions(state):
        move_string = input('Your move? ')
        try:
            move = eval(move_string)
        except NameError:
            move = move_string
    else:
        print('no legal moves: passing turn to next player')
    return move


def random_player(game, state):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state)) if game.actions(state) else None


def alpha_beta_player(game, state):
    return alpha_beta_search(game, state)


def alpha_beta_depth_limited_player(game, state, max_depth=4):
    return alpha_beta_depth_limited_search(game, state, max_depth=max_depth)

def minmax_player(game, state):
    return minimax_search(game, state)
