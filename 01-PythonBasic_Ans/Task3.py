# Task 3 
"""
1. 結合前面用過的程式，詢問使用者的名字，性別，還有生日。
2. 告訴使用者還有幾天生日? 還有幾天就幾歲了 ex: 恭喜你還有101天就20歲了。
"""
name = input("請問你的名字是? ")
gender = input("你的性別是? Male or Female? ")
year = input("出生於哪一年? ")
month = input("幾月 ? ")
day = input("幾號 ? ")

import datetime

if gender=="Male":
    print(name,"先生您好")
else :
    print(name,"小姐您好")

birthday = datetime.datetime(int(year),int(month),int(day))
this_birth = datetime.datetime(2020,int(month),int(day))
age = this_birth.year-birthday.year
day_to_birth = this_birth - datetime.datetime.now()

print("恭喜你再",day_to_birth.days,"就",age,"歲了")
