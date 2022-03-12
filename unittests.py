import unittest

from board import Board, Space

class TestBoard(unittest.TestCase):
    """
    Unit tests for the Board class
    """
    def test_board(self):
        """
        General unit test for the Board class
        """
        # Empty board
        board = Board()
        

    def test_is_won(self):
        """
        Test the Board.is_won method to check if a game is won.
        """
        # Simple win in a row
        position = [
            ['O', 'O', 'O'],
            ['X', 'O', 'X'],
            ['X', 'X', 'O']
        ]
        board = Board(position=position)
        self.assertTrue(board.is_win, "Expected win for position, got False")
        # Win in a column
        position = [
            ['O', 'X', 'X'],
            ['O', 'O', 'X'],
            ['O', 'X', ' ']
        ]
        board = Board(position=position)
        self.assertTrue(board.is_win, "Expected win for position, got False")
        # Win in forward diagonal
        position = [
            ['O', 'X', 'O'], 
            ['X', 'O', 'X'], 
            ['X', 'X', 'O']
        ]
        board = Board(position=position)
        self.assertTrue(board.is_win, "Expected win for position, got False")
        # Win in backward diagonal
        position = [
            ['X', 'X', 'O'], 
            ['X', 'O', 'X'], 
            ['O', 'X', ' ']
        ]
        board = Board(position=position)
        self.assertTrue(board.is_win, "Expected win for position, got False")



if __name__ == "__main__":
    unittest.main()