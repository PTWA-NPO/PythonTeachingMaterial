from Task09 import get_constellation, get_constellations

import unittest
from datetime import date


class TestTask09(unittest.TestCase):
    def test_constellation(self):
        birthday = date(2000, 10, 20)
        self.assertEqual("天秤座", get_constellation(birthday))
        birthday = date(2000, 3, 20)
        self.assertEqual("雙魚座", get_constellation(birthday))
        birthday = date(2000, 9, 22)
        self.assertEqual("處女座", get_constellation(birthday))

    def test_constellations(self):
        # 導入模組方式2 直接呼叫功能
        birthdays = [date(2000, 10, 20), date(2000, 3, 20), date(
            2000, 9, 22), date(2000, 8, 15), date(2000, 11, 1)]
        ans = ["天秤座", "雙魚座", "處女座", "獅子座", "天蠍座"]
        self.assertListEqual(ans, get_constellations(birthdays))


if __name__ == "__main__":
    unittest.main()
