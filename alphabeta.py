
def max_value(game, state, alpha, beta, depth, depth_test, evaluate):
    if depth_test(state, depth):
        return evaluate(state)
    v = float('-inf')
    for a in game.actions(state):
        v = max(v, min_value(game, game.result(state, a), alpha, beta, depth + 1, depth_test, evaluate))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(game, state, alpha, beta, depth, depth_test, evaluate):
    if depth_test(state, depth):
        return evaluate(state)
    v = float('inf')
    for a in game.actions(state):
        v = min(v, max_value(game, game.result(state, a), alpha, beta, depth + 1, depth_test, evaluate))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alpha_beta_depth_limited_search(game, state, max_depth=4, depth_test=None, evaluate=None):
    player = game.to_move(state)
    depth_test = (depth_test or (lambda state, depth: depth > max_depth or game.is_terminal(state)))
    evaluate = evaluate or (lambda state: game.utility(state, player))
    best_score = float('-inf')
    beta = float('inf')
    best_action = None
    for a in game.actions(state):
        v = min_value(game, game.result(state, a), best_score, beta, 1, depth_test, evaluate)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

