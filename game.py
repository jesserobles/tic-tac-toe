
class State:
    def __init__(self, to_move="X", utility=0, board={}, actions=None) -> None:
        self.to_move = to_move
        self.utility = utility
        self.board = board
        self.h = None
        self.v = None
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
                string += self.board.get((x, y), '.') + ' '
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
        actions = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        self.initial = State(to_move='X', utility=0, board={}, actions=actions)

    def is_terminal(self, state) -> bool:
        return state.utility != 0 or len(state.actions) == 0

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
        return State(to_move=state.opposite,
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, actions=actions)
    
    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        """Return true if there is a line through move on board for player."""
        (delta_x, delta_y) = delta_x_y
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
        return n >= self.k
    
    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()
    
    def __repr__(self) -> str:
        pass

    @classmethod
    def from_json(self, json):
        pass
    
    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                state = self.result(state, move)
                if self.is_terminal(state):
                    print(state)
                    return self.utility(state, self.to_move(self.initial))