import constants


def utility(state):
    if constants.terminal_symbol == constants.max_agent_symbol:
        return 1
    elif constants.terminal_symbol == constants.min_agent_symbol:
        return -1
    else:
        return 0
