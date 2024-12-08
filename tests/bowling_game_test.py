import unittest

from src.game import Game


class BowlingGameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__game: Game = Game()

    def test_gutter_game(self) -> None:
        self.roll_many(20, 0)
        self.assertEqual(0, self.__game.score())

    def roll_many(self, rolls: int, pins: int) -> None:
        for i in range(rolls):
            self.__game.roll(pins)

    def test_all_ones(self) -> None:
        self.roll_many(20, 1)
        self.assertEqual(20, self.__game.score())
