import numpy as np
import math

def max_value(Game, state, player, alpha, beta):
    if Game.terminal_test(state):
        return Game.utility(state, player)
    v = -np.inf
    for a in Game.actions(state):
        v = max(v, min_value(Game.result(state, a), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(Game, state, player, alpha, beta):
    if Game.terminal_test(state):
        return Game.utility(state, player)
    v = np.inf
    for a in Game.actions(state):
        v = min(v, max_value(Game.result(state, a), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def expect_minmax(state, Game):
    """
    [Figure 5.11]
    Return the best move for a player after dice are thrown. The game tree
	includes chance nodes along with min and max nodes.
	"""
    player = state.to_move(state)

    # Body of expect_min_max:
    return max_value(Game, state, player, alpha=0, beta=0)

def alpha_beta_search(state, Game):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move(state)
    # Body of alpha_beta_search:
    return max_value(Game, state,player, -math.inf, +math.inf)
