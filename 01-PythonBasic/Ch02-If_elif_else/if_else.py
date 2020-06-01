"""
學習目標:
1. 了解條件判斷，使用 if - elif - else 
2. 了解python中的程式區塊(block)，一個縮排就是一個區塊。
3. 了解條件的組合 "and" "or"
"""

name = "Kylin"
gender = "Male"
year = "2019"
month = 13
date = 25

if month>12:
    print("你騙我，月份不能大於 12 阿!")
elif month<1:
    print("別開玩笑了，月份不可能小於 1")
else :
    print("你的生日是 ",year,"/",month,"/",date)


# Q 用口語一點的思考方式，合併條件
# 邏輯1 如果 月份大於1 "且" 月份小於12 就自我介紹。
month = -1
if 1<int(month) and int(month)<12:
    print("你的生日是 ",year,"/",month,"/",date)
else :
    print("別開玩笑了，月份不可能是 ",month)



# 邏輯2 如果 月份小於1 "或" 月份大於12 就輸出錯誤訊息。
month = -1
if month<1 or month>12  :
    print("別開玩笑了，月份不可能是 ",month)
else :
    print("你的生日是 ",year,"/",month,"/",date)


# TODO Task 2 
"""
1. 根據使用者的生日，計算出使用者的年齡
2. 如果大於18歲，根據性別用哥哥姊姊作為稱呼 ex: Kylin 是哥哥
3. 如果小於12歲，用弟弟妹妹來稱呼 ex: Kylin 是弟弟
"""

# OS: 50歲還用哥哥姊姊實在是太勉強了...
#  Q  每個月分的日期合理範圍都不一樣怎麼辦?
#  Q  請問這個程式到明年還可以正常使用嗎?
