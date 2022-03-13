from constants import max_agent
from value import value

board_size = 3
board = [[None for col in range(board_size)] for row in range(board_size)]
agent_making_move = max_agent


value(board, agent_making_move)
