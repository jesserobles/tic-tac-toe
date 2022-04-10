"""
This module contains the depth limited version of the alpha-beta pruning search. The regular
alpha-beta search is in the minimap.py module, since it uses the same min and max functions
as the minimax search.
"""
import random
import time


def max_value(game, state, player, alpha, beta, depth, depth_test, evaluate):
    if depth_test(game, state, depth):
        return evaluate(game, state, player)
    v = float('-inf')
    for a in game.actions(state):
        v = max(v, min_value(game, game.result(state, a), player, alpha, beta, depth + 1, depth_test, evaluate))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(game, state, player, alpha, beta, depth, depth_test, evaluate):
    if depth_test(game, state, depth):
        return evaluate(game, state, player)
    v = float('inf')
    for a in game.actions(state):
        v = min(v, max_value(game, game.result(state, a), player, alpha, beta, depth + 1, depth_test, evaluate))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alpha_beta_depth_limited_search(game, state, max_depth=4, evaluate=None):
    s = time.time()
    player = game.to_move(state)
    evaluate = evaluate or (lambda state: game.utility(state, player))
    best_score = float('-inf')
    beta = float('inf')
    best_action = None
    for a in game.actions(state):
        v = min_value(game, game.result(state, a), player, best_score, beta, 1, depth_test_function, evaluation_function)
        if v > best_score:
            best_score = v
            best_action = a
    print(time.time() - s)
    return best_action

def depth_test_function(game, state, depth):
    return depth > game.max_depth or game.is_terminal(state)

def evaluation_function(game, state, player):
    return game.utility(state, player)