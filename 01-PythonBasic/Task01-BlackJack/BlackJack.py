import random


class Player:
    def __init__(self):
        self.cards = []

    def receive_a_card(self, card):
        """
        收到一張牌
        """
        self.cards.append(card)
        pass


class Judger:
    def __init__(self):
        # 全部的排組
        self.deck = []
        self.init_deck()
        # 莊家的牌
        self.cards = []
        pass

    def init_deck(self):
        # 初始化52張牌，並且洗亂，先不計花色 ['A','1','2',...]
        self.deck.append('A')
        self.deck.append('2')
        self.deck = ['A', '2', ...]
        pass

    def get_card(self):
        return self.deck.pop()

    def count_one_card(self, card='A'):
        return 11

    def countPoint(self, cards: list) -> int:
        """
        計算點數
        """
        return 1

    def self_draw_card(self):
        """
        莊家點數要大於17點才會停止抽牌。
        """
        pass


if __name__ == "__main__":
    willDrawCard = True
    # 初始化 莊家、玩家
    # 莊家玩家各發兩張牌
    # 顯示莊家的第一張牌、顯示玩家的牌，並算出分數
    while willDrawCard:
        # 玩家拿一張牌，並顯示點數
        # 問玩家還要拿一張牌嗎?
        pass
    # 莊家抽牌
    # 判斷結果

    print("下次再玩")
# Q 現在執行一次程式只能玩一局，怎麼讓我們可以選擇要不要繼續玩呢?
