import unittest

from src.game import Game


class BowlingGameTest(unittest.TestCase):
    def test_gutter_game(self):
        game: Game = Game()
        for i in range(20):
            game.roll(0)
        self.assertEqual(0, game.score())

    def test_all_ones(self):
        game: Game = Game()
        for i in range(20):
            game.roll(1)
        self.assertEqual(20, game.score())
