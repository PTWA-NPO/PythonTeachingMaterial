"""
學習目標:
1. 認識另外一種迴圈 : while loop

核心概念：只要滿足一個條件就繼續做，做到天荒地老
"""

import random
print("While Loop")
rand_int = 0
# 1.當數字小於20就一直執行程式
while (rand_int < 20):
    rand_int = random.randint(1, 20)
    print(rand_int)
print("=================================")

card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Diane_card = ''
Kylin_card = ''

# 2.當A 在 card中，就一直執行程式
while ('A' in card):
    random.shuffle(card)
    Diane_card = card.pop()
    print("Diane draws", Diane_card)
    random.shuffle(card)
    Kylin_card = card.pop()
    print("Kylin draws", Kylin_card)

if Diane_card == 'A':
    print("Diane is winner")
elif Kylin_card == 'A':
    print("Kylin is winner")
