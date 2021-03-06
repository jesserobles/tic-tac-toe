import math
import random
import json
from time import sleep

from api import APIPlayer

class State:
    def __init__(self, h=3, v=3, to_move="X", utility=0, board={}, actions=None) -> None:
        self.to_move = to_move
        self.utility = utility
        self.board = board
        self.h = h
        self.v = v
        if self.board:
            self.h = max(key[0] for key in self.board)
            self.v = max(key[-1] for key in self.board)
        self.actions = actions
    
    @property
    def opposite(self):
        if self.to_move == 'O':
            return 'X'
        else:
            return 'O'

    def __repr__(self) -> str:
        string = ''
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                string += self.board.get((x, y), '-')
            string = string.strip() + "\n"
        return string

class Game:
    """
    A class representing a tic-tac-toe game.
    """
    def __init__(self, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        self.spaces = self.h * self.v
        actions = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        self.initial = State(h=self.h, v=self.v, to_move='X', utility=0, board={}, actions=actions)
        self.max_depth = 0

    def is_terminal(self, state) -> bool:
        return state.utility == 1 or state.utility == -1 or len(state.actions) == 0

    def to_move(self, state):
        return state.to_move

    def utility(self, state, player):
        return state.utility if player == 'X' else -state.utility

    def actions(self, state):
        return state.actions

    
    def result(self, state, move):
        if move not in state.actions:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        actions = list(state.actions)
        actions.remove(move)
        return State(self.h, self.v, to_move=state.opposite,
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, actions=actions)
    
    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        longest_vertical = self.k_in_row(board, move, player, (0, 1))
        longest_horizontal = self.k_in_row(board, move, player, (1, 0))
        longest_diag_top_right_to_bottom_left = self.k_in_row(board, move, player, (1, -1))
        longest_diag_top_left_to_bottom_right = self.k_in_row(board, move, player, (1, 1))

        longest = max(longest_vertical, longest_horizontal, longest_diag_top_right_to_bottom_left, longest_diag_top_left_to_bottom_right)
        utility = self.depth_limited_utility_estimation(longest)

        if player == 'X':
            return utility
        else:
            return -utility

    def depth_limited_utility_estimation(self, longest_run):
        return round(longest_run/self.k,1)

    def k_in_row(self, board, move, player, delta_x_y):
        """Return true if there is a line through move on board for player."""
        delta_x, delta_y = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n
    
    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '-'), end=' ')
            print()

    def update_depth_limit(self, actions):
        self.max_depth = round(2 + 8 * math.e**(-actions/25))
    
    def __repr__(self) -> str:
        pass
    
    def play_game(self, *players):
        """
        Play an n-person, move-alternating game.
        """
        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                state = self.result(state, move)
                print(state)
                print()
                self.update_depth_limit(len(state.actions))
                if self.is_terminal(state):
                    print(state)
                    return self.utility(state, self.to_move(self.initial))

    def play_api(self, player, id, opponent_id, apikeyfile, first, game_id=None, board_size=3, target=3):
        apiplayer = APIPlayer(apikeyfile=apikeyfile, team_id=id, game_id=game_id)
        state = self.initial
        self.update_depth_limit(len(state.actions))

        if game_id is None:
            game_id = apiplayer.create_game(opponent_id, board_size, target).json()['gameId']
            print('Game ID: ' + str(game_id))

        if first:
            move = player(self, state, max_depth=self.max_depth)
            apiplayer.move(move[0]-1, move[1]-1)  # Code is 1 indexed, but api is 0 index
            state = self.result(state, move)
            print(state)

        while True:
            opponent_move = None
            while opponent_move is None:
                sleep(2)
                result = json.loads(apiplayer.get_moves().text)
                if result['code'] == 'OK':
                    for move in result['moves']:
                        if int(move['moveId']) not in apiplayer.get_move_id_cache():
                            apiplayer.add_move_to_cache(int(move['moveId']))

                            if int(move['teamId']) == opponent_id:
                                # Code is 1 indexed, but api is 0 index
                                opponent_move = (int(move['moveX'])+1, int(move['moveY'])+1)

            state = self.result(state, opponent_move)
            print(state)
            if self.is_terminal(state):
                return self.utility(state, self.to_move(self.initial))

            # Our Move
            move = player(self, state, max_depth=self.max_depth)
            apiplayer.move(move[0]-1, move[1]-1)  # Code is 1 indexed, but api is 0 index

            state = self.result(state, move)
            print(state)
            self.update_depth_limit(len(state.actions))
            if self.is_terminal(state):
                print(state)
                return self.utility(state, self.to_move(self.initial))
