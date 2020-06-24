"""
學習目標:
1. 使用外部模組幫忙計算日期， import datetime
2. 了解什麼是模組，如何使用模組。

比喻: 大雄有問題會找誰?小叮噹
小叮噹怎麼幫助他?從百寶袋拿出道具。
程式也是一樣，有很多的工具可以使用，我們就試試其中一種工具吧。
"""

import random
import datetime
name = "Kylin"
gender = "Male"
year = "1995"
month = 10
date = 25

# 要讓程式到了明年還能用->取得當下的日期。

# datetime模組下方的某個工具的某個功能
today = datetime.datetime.now()
birthday = datetime.datetime(int(year), month, date)

print(today)
print(birthday)

# 告訴使用者他已經活了幾天
result = today - birthday
print(result)


# TODO Task 3
"""
1. 結合前面用過的程式，詢問使用者的名字，性別，還有生日。
2. 告訴使用者還有幾天生日? 還有幾天就幾歲了 ex: 恭喜你再101天就20歲了。
"""

# 使用隨機模組
final_number = random.randint(0, 100)
print(final_number)

# 使用隨機模組產生-100~100的數字
final_number = random.randint(-100, 100)
print(final_number)

# 使用隨機模組產生0~100中，2的倍數
final_number = random.randint(0, 50)*2
print(final_number)
# 使用隨機模組產生 -100 ~ -50, 50~100 的數字
final_number = random.randint(50, 100) * random.choice([1, -1])
print(final_number)
