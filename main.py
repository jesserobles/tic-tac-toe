'''
CSCI 6511 Artifical Intelligence
Project 3 -- Tic-Tac-Toe
'''


player, opponent = 'x', 'o'

def isMovesLeft(board):
    '''
    :param board:
    :return:
    '''
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def evaluate(b):
    '''
    Description: Checking to see if there are any winners
    :param b:
    :return:
    '''
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10
    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10

    return 0


def minimax(board, depth, isMax):
    '''

    :param board:
    :param depth:
    :param isMax:
    :return:
    '''
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if isMovesLeft(board) == False:
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board,
                                             depth + 1,
                                             not isMax))
                    board[i][j] = '_'
        return best

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = '_'
        return best


def findBestMove(board):
    '''

    :param board:
    :return:
    '''
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove


def main(test_board):

    test_board = [
        ['x', 'x', '_'],
        ['o', 'o', '_'],
        ['x', '_', 'o']
    ]

    bestMove = findBestMove(test_board)

    print("The Optimal Move is :")
    print("ROW:", bestMove[0], " COL:", bestMove[1])


