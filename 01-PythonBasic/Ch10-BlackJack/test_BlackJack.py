import BlackJack
import unittest
import random
origin_deck = ['A', '2', '3', '4', '5',
               '6', '7', '8', '9', '10', 'J', 'Q', 'K',
               'A', '2', '3', '4', '5',
               '6', '7', '8', '9', '10', 'J', 'Q', 'K'
               'A', '2', '3', '4', '5',
               '6', '7', '8', '9', '10', 'J', 'Q', 'K'
               'A', '2', '3', '4', '5',
               '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class TestTask10(unittest.TestCase):
    def test_game_initial(self):
        judger = BlackJack.Judger()
        self.assertEqual(52, len(judger.cards))
        coutn_A = judger.cards.count('A')
        self.assertEqual(4, coutn_A)
        coutn_K = judger.cards.count('K')
        self.assertEqual(4, coutn_K)
        self.assertNotEqual(origin_deck, judger.cards)
        pass

    def test_player_draw_card(self):
        player = BlackJack.Player()
        self.assertListEqual([], player.cards)
        player.receive_a_card('A')
        self.assertListEqual(['A'], player.cards)
        player.receive_a_card('1')
        self.assertListEqual(['A', '1'], player.cards)

    def test_one_card(self):
        judger = BlackJack.Judger()
        self.assertEqual(11, judger.count_one_card('A'))
        self.assertEqual(2, judger.count_one_card('2'))
        self.assertEqual(10, judger.count_one_card('10'))
        self.assertEqual(10, judger.count_one_card('J'))
        self.assertEqual(10, judger.count_one_card('Q'))
        self.assertEqual(10, judger.count_one_card('K'))

    def test_countPoint(self):
        judger = BlackJack.Judger()
        self.assertEqual(11, judger.countPoint(['A']))
        self.assertEqual(2, judger.countPoint(['2']))
        self.assertEqual(10, judger.countPoint(['10']))
        self.assertEqual(10, judger.countPoint(['J']))
        self.assertEqual(10, judger.countPoint(['Q']))
        self.assertEqual(10, judger.countPoint(['K']))
        self.assertEqual(21, judger.countPoint(['A', 'K']))
        self.assertEqual(21, judger.countPoint(['K', 'A']))
        self.assertEqual(18, judger.countPoint(['A', '2', '5']))
        self.assertEqual(16, judger.countPoint(['J', 'A', '5']))
        self.assertEqual(11, judger.countPoint(['2', '4', '5']))
        self.assertEqual(19, judger.countPoint(['8', 'A']))
        self.assertEqual(21, judger.countPoint(['8', 'A', '2']))
        self.assertEqual(20, judger.countPoint(['J', 'Q']))
        self.assertEqual(12, judger.countPoint(['7', 'A', '4']))
        self.assertEqual(12, judger.countPoint(['A', 'A']))
        self.assertEqual(19, judger.countPoint(['5', '6', '8']))
        # self.assertEqual(13, judger.countPoint(['A', 'A','A']))


if __name__ == "__main__":
    unittest.main()
