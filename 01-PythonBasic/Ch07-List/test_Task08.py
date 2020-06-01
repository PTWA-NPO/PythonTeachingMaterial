from Task08 import get_constellation, get_constellation_list

import unittest


class TestTask08(unittest.TestCase):
    def test_constellation_list(self):
        # 導入模組方式1 模組.功能
        result = get_constellation_list()
        self.assertEqual(12, len(result), "陣列長度要一樣")

        self.assertListEqual(
            [
                "牡羊座	3月21日～4月20日",
                "金牛座	4月21日～5月20日",
                "雙子座	5月21日～6月20日",
                "巨蟹座	6月21日～7月22日",
                "獅子座	7月23日～8月22日",
                "處女座	8月23日～9月22日",
                "天秤座	9月23日～10月22日",
                "天蠍座	10月23日～11月22日",
                "射手座	11月23日～12月22日",
                "魔羯座	12月23日～1月21日",
                "水瓶座	1月22日～2月19日",
                "雙魚座	2月20日～3月20日"
            ], result

        )

    def test_constellation(self):
        self.assertEqual("牡羊座", get_constellation(1))
        self.assertEqual("雙魚座", get_constellation(12))
        self.assertEqual("雙子座", get_constellation(3))
        self.assertEqual("處女座", get_constellation(6))


if __name__ == "__main__":
    unittest.main()
