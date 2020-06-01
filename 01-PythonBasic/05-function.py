"""
學習目標:
1. 化繁為簡，將瑣碎的程式碼整理起來，讓我們能重複使用，也能更容易了解。
2. 整理程式碼的方式就是寫一個function。

核心概念：有工具的時候，運用工具，沒有工具的時候，自己發明工具。
"""

name = "Kylin"
gender = "Male"
year = "1995"
month = 8
date = 15

# 第一種function 執行動作的function
# 這是一個完整的自我介紹
print("您好，我的名字是"+name)
print("我出生於"+year)
print("我的生日是 ", month , "月 " ,date,"日。" )
# Q 但是如果有一個新的同學Jessica，要自我介紹，程式怎麼寫?

"""
name_2 = "Jessica"
gender_2 = "Female"
year_2 = "1993"
month_2 = 9
date_2 = 5

def introduction(name,year,month,date):
    print("您好，我的名字是"+name)
    print("我出生於"+year)
    print("我的生日是 ", month , "月 " ,date,"日。" )

"""

# 第二種function 回傳結果的function
import datetime
def get_number_of_living_days(year,month,date): 
    ''' 計算已經生活幾天，並回傳。'''
    today = datetime.datetime.now()
    birthday = datetime.datetime(int(year),month,date)
    result = today - birthday
    return result

living_days = get_number_of_living_days(int(year),month,date)
print("我已經活了 ",living_days.days,"天")



# TODO 小試身手 計算還有幾天就生日
def get_days_to_birth(month,date):
    return 0
days_to_birth = get_days_to_birth(month,date)

print("再 ",days_to_birth,"天就是我的生日了~~")


# TODO Task 4
"""
寫一個涵式，做自我介紹，範例如下。
您好，我的名字是Kylin，可以叫我Kylin 哥哥
我出生於1993
我的生日是  8 月  15 日。
我已經活了  9040 天
再  90 天就是我的生日了~~ 
很高興認識你
"""

def introduce():
    pass