from enum import Enum


class Space(Enum):
    """
    A class representing a space on the tic-tac-toe board.
    Spaces can be empty, or contain an X or an O.
    """
    X = "X"
    O = "O"
    E = " "

    @property
    def opposite(self):
        if self == Space.X:
            return Space.O
        if self == Space.O:
            return Space.X
        return Space.E
    
    def __str__(self) -> str:
        return self.value


class Board:
    """
    A class representing a tic-tac-toe board.
    This class maintains the state of the game. It should
    also keep track of whose turn it is, and whether the 
    game is won, lost, or a draw. For simplicity, we will
    initially assume the board is a standard 3x3 board.
    The spaces are designated using a 1-D array as follows:
        0|1|2
        -----
        3|4|5
        -----
        6|7|8
    """
    def __init__(self, turn=Space.X, position=None, board_dimensions=(3,3), max_depth=8) -> None:
        self.board_dimensions = board_dimensions
        self.max_depth = max_depth
        if position is None:
            position = self.reshape([Space.E] * (board_dimensions[0] * board_dimensions[1]), board_dimensions)
        self.position = self.convert_array(position)
        self.turn = turn
    
    def convert_array(self, array):
        """
        Helper method to reshape array and convert string inputs into Space objects.
        """
        array = self.reshape(array, self.board_dimensions)
        if isinstance(array[0][0], Enum):
            return array
        array = [[Space(col) for col in row] for row in array]
        return array

    def __repr__(self) -> str:
        """
        TODO: Implement this correctly
        """
        return '\n--- --- ---\n'.join('  | '.join(col.value for col in row) for row in self.position)

    def reshape(self, array, dimensions) -> list[list[int]]:
        """
        Helper method to reshape a 1-D into the dimension
        specified by dimensions. This should check that the
        length of the array can accomodate the given dimension.
        """
        # First check if the array is already in the desired dimension
        if len(array) == dimensions[0]:
            if all(len(row) == dimensions[1] for row in array):
                return array
            else: # Not all rows are the correct size; raise exception
                raise ValueError("Dimensions mismatch")
        if len(dimensions) != 2:
            raise ValueError("Dimensions mismatch")
        if dimensions[0] * dimensions[1] != len(array):
            raise ValueError("Dimensions mismatch")
        return [array[i:i+dimensions[0]] for i in range(0, len(array), dimensions[1])]
    
    def ravel(self, array):
        """
        Helper method to convert an nxn dimensional array into a 1-D array
        """
        return [col for row in array for col in row]

    @property
    def play(self, location):
        """Play the next space"""
        tmp_position = self.position.copy()
        tmp_position[location] = self.turn
        return Board(tmp_position, self.turn.opposite)
    
    @property
    def legal_moves(self) -> list[int]:
        """
        Moves are just integers representing which space in
        the board we can play. For tic-tac-toe, this is simply
        any empty space.
        """
        return [i for i in range(len(self.position)) if self.position[i] == Space.E]
    
    def get_successors(self):
        return self.legal_moves
    
    def next_state(self):
        return
    
    def is_terminal(self):
        return self.is_win or self.is_draw or self.max_depth == 0

    @property
    def is_win(self) -> bool:
        """
        A method to determine if the game is won. This should be implemented
        in a way that is generic enough to cover different board sizes. In
        general, if an entire row, column, or full diagonal contains the same
        player's symbol, then the game is won by that player.
        """
        # First check the rows
        for row in self.position:
            if all(elem == Space.O for elem in row) or all(elem == Space.X for elem in row):
                return True
        # Now check the columns
        for col in range(self.board_dimensions[-1]):
            values = [row[col] for row in self.position]
            if all(elem == Space.O for elem in values) or all(elem == Space.X for elem in values):
                return True
        # Finally, check the diagonals
        # First case is forward diagonal
        if all(self.position[ix][ix] == Space.O for ix in range(self.board_dimensions[0])) \
            or all(self.position[ix][ix] == Space.X for ix in range(self.board_dimensions[0])):
            return True
        # Second case is backwards diagonal
        if all(self.position[ix][self.board_dimensions[0] - ix - 1] == Space.O for ix in range(self.board_dimensions[0])) \
            or all(self.position[ix][self.board_dimensions[0] - ix - 1] == Space.X for ix in range(self.board_dimensions[0])):
            return True
        return False

    def evaluate(self, player):
        if self.is_win:
            if self.turn == player:
                return -1
            else:
                return 1
        # Draw
        return 0

    @property
    def utility(self):
        pass

    @property
    def is_draw(self) -> bool:
        return not self.is_win and len(self.legal_moves) == 0
    
    @classmethod
    def from_json(self, json):
        pass

    def read_move(self, opponent_move):
        """
        Assuming we get the opponent's next move from the
        api call.
        """
        pass

