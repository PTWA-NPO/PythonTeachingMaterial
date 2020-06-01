import datetime

"""
學習目標:
1. 什麼叫做迴圈 (loop)?
2. 我們用迴圈輸出全部的人
3. 程式中，箱子的編號是從0開始

核心概念：當需要重複很多次類似的動作時，就叫做loop
"""


class People:
    def __init__(self, name, gender, birthday):
        self.name = name
        self.gender = gender
        self.birthday = birthday


students = []
students.append(People("Kylin_1", "Male", datetime.date(1993, 8, 15)))
students.append(People("Kylin_2", "Male", datetime.date(1993, 8, 15)))
students.append(People("Kylin_3", "Male", datetime.date(1993, 8, 15)))
students.append(People("Kylin_4", "Male", datetime.date(1993, 8, 15)))

# 1. for的用法，在一個list中抓出每一個元素，執行相同的動作
for stu in students:
    print(stu.name)
    print(stu.gender)
    print(stu.birthday)
    print()

# for num, student in enumerate(students):
#     print("第", num, "人的名字是 ", student.name)
