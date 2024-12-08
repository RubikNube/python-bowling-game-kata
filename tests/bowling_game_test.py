import unittest

from src.game import Game


class BowlingGameTest(unittest.TestCase):
    def test_gutter_game(self):
        game: Game = Game()
