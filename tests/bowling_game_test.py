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

    def test_one_spare(self) -> None:
        self.roll_spare()
        self.__game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.__game.score())

    def roll_spare(self) -> None:
        self.__game.roll(5)
        self.__game.roll(5)

    def test_one_strike(self) -> None:
        self.roll_strike()
        self.__game.roll(3)
        self.__game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.__game.score())

    def roll_strike(self) -> None:
        self.__game.roll(10)
