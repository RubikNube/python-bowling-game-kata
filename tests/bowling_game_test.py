import unittest

from src.game import Game


class BowlingGameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__game: Game = Game()

    def test_gutter_game(self) -> None:
        for i in range(20):
            self.__game.roll(0)
        self.assertEqual(0, self.__game.score())

    def test_all_ones(self) -> None:
        for i in range(20):
            self.__game.roll(1)
        self.assertEqual(20, self.__game.score())
