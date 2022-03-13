import constants


def terminal(state):
    if None not in state:
        return True
    elif n_in_a_row(state):
        return True
    else:
        return False


def n_in_a_row(state):
    if vertical_terminal_check(state) == True:
        return True
    elif horizontal_terminal_check(state) == True:
        return True
    elif vertical_terminal_check(state) == True:
        return True
    else:
        return False


def vertical_terminal_check(state):
    char_at_n = None
    for row in range(len(state[0])):
        solution_found = True
        for col in range(len(state)):
            if state[col][row] != None:
                if char_at_n == None:
                    char_at_n = state[col][row]
                elif char_at_n == state[col][row]:
                    continue
                else:
                    solution_found = False
                    break
            else:
                solution_found = False
                break
        if solution_found:
            constants.terminal_symbol = char_at_n
            return True


def horizontal_terminal_check(state):
    char_at_n = None
    for col in range(len(state)):
        solution_found = True
        for row in range(len(state[0])):
            if state[col][row] != None:
                if char_at_n == None:
                    char_at_n = state[col][row]
                elif char_at_n == state[col][row]:
                    continue
                else:
                    solution_found = False
                    break
            else:
                solution_found = False
                break
        if solution_found:
            constants.terminal_symbol = char_at_n
            return True


def diagonal_terminal_check(state):
    # This requires that the tic-tac-toe board is a square
    char_at_n = None
    length = len(state)

    # top left to bottom right
    for n in range(length):
        solution_found = True
        if state[n][n] != None:
            if char_at_n == None:
                char_at_n = state[n][n]
            elif char_at_n == state[n][n]:
                continue
            else:
                solution_found = False
                break
        else:
            solution_found = False
            break
    if solution_found:
        constants.terminal_symbol = char_at_n
        return True

    # top right to bottom left
    for n in range(length):
        solution_found = True
        if state[n][length - n] != None:
            if char_at_n == None:
                char_at_n = state[n][length - n]
            elif char_at_n == state[n][length - n]:
                continue
            else:
                solution_found = False
                break
        else:
            solution_found = False
            break
    if solution_found:
        constants.terminal_symbol = char_at_n
        return True