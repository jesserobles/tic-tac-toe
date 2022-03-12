
"""
Pseudocode from lecture slides
def max-value(state):
    initialize v = -∞
    for each successor of state:
        v = max(v, min-value(successor))
    return v

def min-value(state):
    initialize v = +∞
    for each successor of state:
        v = min(v, max-value(successor))
    return v

def value(state):
    if the state is a terminal state: return the state's utility
    if the next agent is MAX: return max-value(state)
    if the next agent is MIN: return min-value(state)

"""

def max_value(state):
    v = float('-inf')
    for successor in state.get_successors():
        v = max(v, min_value(successor))
    return v

def min_value(state):
    v = float('inf')
    for successor in state.get_successors():
        v = min(v, max_value(successor))
    return v

def value(state):
    if state.next_state().is_terminal(): return state.utility
    if state.next_agent() == "MAX": return max_value(state)
    if state.next_agent() == "MIN": return min_value(state)