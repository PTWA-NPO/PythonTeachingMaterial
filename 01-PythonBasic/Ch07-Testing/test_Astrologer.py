import unittest
import Astrologer
from Astrologer import get_constellation

class MyTestCase(unittest.TestCase):

    def test_constellation(self):
        # 導入模組方式2 直接呼叫功能
        self.assertEqual("水瓶座",get_constellation(2,19))
        self.assertEqual("牡羊座",get_constellation(3,21))
        self.assertEqual("獅子座",get_constellation(8,16))
        self.assertEqual("處女座",get_constellation(8,30))
        

if __name__ == '__main__':
    unittest.main()
