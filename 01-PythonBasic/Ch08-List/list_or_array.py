import datetime
import random

"""
學習目標:
1. 了解Python 中的 List

比喻: 就像一個有編號的盒子一樣。

"""

# 1. 舉例:樂透號碼有六個
lottery = [11, 2, 3, 4, 5, 6]

# 1.1 新增元素
lottery.append(0)
# 1.2 清空
lottery.clear()
lottery.append(random.randint(1, 49))
lottery.append(random.randint(1, 49))
lottery.append(random.randint(1, 49))
lottery.append(random.randint(1, 49))
lottery.append(random.randint(1, 49))
lottery.append(random.randint(1, 49))
print("開出樂透", lottery)

# 1.3 常見用法
print("lottery的大小", len(lottery))
print("第一個號碼:", lottery[0])
print("吐出最後一個號碼:", lottery.pop())
print("lottery 變成 ", lottery)

# 1.4 注意使用index 範圍
# print("超出範圍會 ")
# print(lottery[5])

# 1.5 由小到大排序
lottery.sort()
print(lottery)
# 1.6 翻轉順序
lottery.reverse()
print(lottery)


# 1.7 可以放任何雜七雜八的東西: bool , int , str , object, []
class People:
    def __init__(self, name, gender, birthday):
        self.name = name
        self.gender = gender
        self.birthday = birthday


students = []
students.append(People("Kylin_1", "Male", datetime.date(1993, 8, 15)))
students.append(People("Kylin_2", "Male", datetime.date(1993, 8, 15)))

print(students[0].name)
print(students[1].name)
