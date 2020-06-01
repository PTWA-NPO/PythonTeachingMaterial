import unittest
import Astrologer


class MyTestCase(unittest.TestCase):

    def test_birthday_dict(self):

        self.assertEqual(8, sum(Astrologer.get_birthday_number_list(1, 1, 1)))
        self.assertListEqual(Astrologer.get_birthday_number_list(1995, 12, 13),
                             [0, 3, 1, 1, 0, 1, 0, 0, 0, 2]
                             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                             )
        self.assertListEqual(Astrologer.get_birthday_number_list(2005, 1, 13),
                             [3, 2, 1, 1, 0, 1, 0, 0, 0, 0]
                             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                             )
        self.assertListEqual(Astrologer.get_birthday_number_list(1, 1, 1),
                             [5, 3, 0, 0, 0, 0, 0, 0, 0, 0]
                             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                             )

    def test_life_number(self):
        self.assertEqual(4, Astrologer.get_life_number(1995, 12, 13))
        self.assertEqual(9, Astrologer.get_life_number(1993, 8, 15))
        self.assertEqual(1, Astrologer.get_life_number(1993, 8, 16))
        self.assertEqual(6, Astrologer.get_life_number(1993, 8, 30))
        self.assertEqual(3, Astrologer.get_life_number(1, 1, 1))
        self.assertEqual(6, Astrologer.get_life_number(800, 8, 8))
        self.assertEqual(4, Astrologer.get_life_number(1001, 1, 1))

    def test_constellation(self):
        self.assertEqual("獅子座", Astrologer.get_constellation(8, 16))
        self.assertEqual("處女座", Astrologer.get_constellation(8, 30))
        self.assertEqual("天蠍座", Astrologer.get_constellation(10, 23))
        self.assertEqual("雙魚座", Astrologer.get_constellation(2, 29))


if __name__ == '__main__':
    unittest.main()
