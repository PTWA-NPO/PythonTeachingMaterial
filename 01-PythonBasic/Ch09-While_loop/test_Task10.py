from Task10 import NumberGame

import unittest
import random


class TestTask10(unittest.TestCase):
    def test_game_initial(self):
        game = NumberGame(36)
        self.assertEqual(36, game.get_target())
        self.assertListEqual([1, 100], game.get_range())

        game = NumberGame(72)
        self.assertEqual(72, game.get_target())
        self.assertListEqual([1, 100], game.get_range())

    def test_game_could_guess(self):
        game = NumberGame(36)

        self.assertEqual("Sorry", game.guess(15))
        self.assertListEqual([15, 100], game.get_range(), "範圍下限要更新")
        self.assertEqual("Error", game.guess(-1))
        self.assertListEqual([15, 100], game.get_range(), "猜不合理的數字，不能改變範圍")
        self.assertEqual("Error", game.guess(100))
        self.assertListEqual([15, 100], game.get_range(), "猜不合理的數字，不能改變範圍")
        self.assertEqual("Error", game.guess(15))
        self.assertListEqual([15, 100], game.get_range(), "猜不合理的數字，不能改變範圍")
        self.assertEqual("Error", game.guess(1))
        self.assertListEqual([15, 100], game.get_range(), "猜不合理的數字，不能改變範圍")
        self.assertEqual("Sorry", game.guess(52))
        self.assertListEqual([15, 52], game.get_range(), "範圍上限要更新")

        self.assertEqual("Sorry", game.guess(35))
        self.assertListEqual([35, 52], game.get_range(), "範圍下限要更新")
        self.assertEqual("Sorry", game.guess(37))
        self.assertListEqual([35, 37], game.get_range(), "範圍上限要更新")

        self.assertEqual("Bingo", game.guess(36))


if __name__ == "__main__":
    unittest.main()
