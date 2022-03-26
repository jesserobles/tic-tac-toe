from board import Board

"""
Pseudocode from lecture slides:

MAX VALUE:
def max-value(state):
    initialize v = -∞
    for each successor of state:
        v = max(v, min-value(successor))
    return v

With alpha-beta pruning:

def max-value(state, α, β):
    initialize v = -∞
    for each successor of state:
        v = max(v, value(successor, α, β))
        if v ≥ β return v
        α = max(α, v)
    return v

MIN VALUE:
def min-value(state):
    initialize v = +∞
    for each successor of state:
        v = min(v, max-value(successor))
    return v

With alpha-beta pruning:

def min-value(state , α, β):
    initialize v = +∞
    for each successor of state:
        v = min(v, value(successor, α, β))
        if v ≤ α return v
        β = min(β, v)
    return v

def value(state):
    if the state is a terminal state: return the state's utility
    if the next agent is MAX: return max-value(state)
    if the next agent is MIN: return min-value(state)


function MINIMAX-SEARCH(game, state) returns an action
    player←game.TO-MOVE(state)
    value, move←MAX-VALUE(game, state)
    return move

function MAX-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v ← -∞
    for each a in game.ACTIONS(state) do
        v2, a2←MIN-VALUE(game, game.RESULT(state, a))
        if v2 > v then
            v, move←v2, a
    return v, move

function MIN-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v ← +∞
    for each a in game.ACTIONS(state) do
        v2, a2←MAX-VALUE(game, game.RESULT(state, a))
        if v2 < v then
            v, move←v2, a
    return v, move
"""

def minimax_search(game, state):
    player = game.to_move(state)
    value, move = max_value(game, state, player)
    return move

def alpha_beta_search(game, state):
    player = game.to_move(state)
    value, move = max_value(game, state, float('-inf'), float('inf'))
    return move

def max_value(game, state, player, alpha=None, beta=None):
    if game.is_terminal(state): return game.utility(state, player), None
    v = float('-inf')
    for a in game.actions(state):
        v2, a2 = min_value(game, game.result(state, a), player, alpha, beta)
        if v2 > v:
            v, move = v2, a
            if not alpha is None:
                a = max(alpha, v)
            if not beta is None and v >= beta: return v, move
    return v, move

def min_value(game, state, player, alpha=None, beta=None):
    if game.is_terminal(state): return game.utility(state, player), None
    v = float('inf')
    for a in game.actions(state):
        v2, a2 = max_value(game, game.result(state, a), player, alpha, beta)
        if v2 < v:
            v, move = v2, a
            if not beta is None:
                beta = min(beta, v)
            if not alpha is None and v <= alpha: return v, move
    return v, move