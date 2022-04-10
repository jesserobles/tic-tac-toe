import unittest

from api import APIPlayer
from game import Game
from players import minmax_player, alpha_beta_player, alpha_beta_depth_limited_player


class TestGame(unittest.TestCase):
    """Test class for the Game class"""
    def test_game(self):
        game = Game(3, 3, 3)
        self.assertEqual(game.to_move(game.initial), 'X')


class TestMiniMaxPlayer(unittest.TestCase):
    """Test class for minimax player"""
    def test_minimax_player(self):
        game = Game(3, 3, 3)
        player = minmax_player
        state = game.initial
        move = player(game, state)
        self.assertIsNotNone(move)
        state = game.result(state, move)
        self.assertIsNotNone(state)


class TestAlphaBetaPlayer(unittest.TestCase):
    """Test class for the alpha-beta player"""
    def test_alpha_beta_player(self):
        game = Game(3, 3, 3)
        player = alpha_beta_player
        state = game.initial
        move = player(game, state)
        self.assertIsNotNone(move)
        state = game.result(state, move)
        self.assertIsNotNone(state)


class TestAlphaBetaDepthLimitedPlayer(unittest.TestCase):
    """Test class for the alpha-beta depth-limited player"""
    def test_alpha_beta_depth_limited_player(self):
        game = Game(12, 12, 12)
        player = alpha_beta_depth_limited_player
        state = game.initial
        move = player(game, state)
        self.assertIsNotNone(move)
        state = game.result(state, move)
        self.assertIsNotNone(state)


class TestAPICalls(unittest.TestCase):
    """Test class for API calls. We'll just limit them to the ones
    not related to creating games or issuing moves.
    """
    def test_api_list_teams(self):
        api = APIPlayer()
        response = api.list_my_teams()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["code"], "OK")

    def test_get_my_games(self):
        api = APIPlayer()
        response = api.get_my_games()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["code"], "OK")

    def test_get_moves(self):
        api = APIPlayer(game_id=3403)
        response = api.get_moves()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["code"], "OK")
    
    def test_get_board_string(self):
        api = APIPlayer(game_id=3403)
        response = api.get_board_string()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["code"], "OK")
    
    def test_get_board_map(self):
        api = APIPlayer(game_id=3403)
        response = api.get_board_map()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["code"], "OK")


if __name__ == "__main__":
    unittest.main()