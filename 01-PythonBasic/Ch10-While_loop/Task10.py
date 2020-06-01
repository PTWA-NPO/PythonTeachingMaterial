"""
1. 寫一個終極密碼的程式
2. 遊戲規則，從1~100隨機選出一個號碼當作目標。
3. 每個人輪流猜，猜到數字的人就贏了。
"""


class NumberGame:
    def __init__(self, target=0):
        """
        要包含三種資料，終極密碼、上限、下限
        """
        pass

    def get_target(self):
        """
        回傳終極密碼
        """
        return 0

    def get_range(self) -> []:
        """
        回傳一個list，第一個數字是數字下限，第二個數字是數字上限
        """
        return [1, 100]

    def guess(self, num: int):
        """
        根據猜的數字告訴玩家是否猜對，
        猜到回傳"Bingo",
        不在範圍內就回傳"Error"
        沒猜到就回傳"Sorry"，並且更新上下限
        """
        return ""


if __name__ == "__main__":
    """
    實作一個小遊戲
    使用while 迴圈寫一個遊戲
    Hint:
    遊戲開始會隨機產生一個數字2~99，要有輸入介面讓玩家要不斷輸入數字，去猜電腦產生的數字是多少。
    每猜一次，電腦也會更新數字範圍
    答對密碼，遊戲才會結束
    """
    pass
