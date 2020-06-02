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
        self.assertEqual(11, judger.count_one_card_point('A'))
        self.assertEqual(2, judger.count_one_card_point('2'))
        self.assertEqual(10, judger.count_one_card_point('10'))
        self.assertEqual(10, judger.count_one_card_point('J'))
        self.assertEqual(10, judger.count_one_card_point('Q'))
        self.assertEqual(10, judger.count_one_card_point('K'))

    def test_countPoint(self):
        judger = BlackJack.Judger()
        self.assertEqual(11, judger.count_cards_point(['A']))
        self.assertEqual(2, judger.count_cards_point(['2']))
        self.assertEqual(10, judger.count_cards_point(['10']))
        self.assertEqual(10, judger.count_cards_point(['J']))
        self.assertEqual(10, judger.count_cards_point(['Q']))
        self.assertEqual(10, judger.count_cards_point(['K']))
        self.assertEqual(21, judger.count_cards_point(['A', 'K']))
        self.assertEqual(21, judger.count_cards_point(['K', 'A']))
        self.assertEqual(18, judger.count_cards_point(['A', '2', '5']))
        self.assertEqual(16, judger.count_cards_point(['J', 'A', '5']))
        self.assertEqual(11, judger.count_cards_point(['2', '4', '5']))
        self.assertEqual(19, judger.count_cards_point(['8', 'A']))
        self.assertEqual(21, judger.count_cards_point(['8', 'A', '2']))
        self.assertEqual(20, judger.count_cards_point(['J', 'Q']))
        self.assertEqual(12, judger.count_cards_point(['7', 'A', '4']))
        self.assertEqual(12, judger.count_cards_point(['A', 'A']))
        self.assertEqual(19, judger.count_cards_point(['5', '6', '8']))
        # self.assertEqual(13, judger.countPoint(['A', 'A','A']))

    def test_decideWinner(self):
        judger = BlackJack.Judger()

        self.assertEqual("Win", judger.decideWinner(21, 16))
        self.assertEqual("Win", judger.decideWinner(16, 24))
        self.assertEqual("Win", judger.decideWinner(19, 17))
        self.assertEqual("Lose", judger.decideWinner(24, 21))
        self.assertEqual("Lose", judger.decideWinner(20, 21))
        self.assertEqual("Lose", judger.decideWinner(17, 19))
        self.assertEqual("Draw", judger.decideWinner(17, 17))
        self.assertEqual("Draw", judger.decideWinner(21, 21))


if __name__ == "__main__":
    unittest.main()
