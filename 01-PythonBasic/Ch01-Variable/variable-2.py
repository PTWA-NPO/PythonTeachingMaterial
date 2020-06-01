"""
學習目標:
1. 資料有各種型態，我們可以用type()來知道他是哪一種。
2. 使用 str() int() 轉換資料的型態。
3. 使用運算符號 + - * / ，不同型態的資料 井水不犯河水，無法互相運算。
"""

name = "Kylin"
year = "2019"
month = 5
date = 15

# 1.資料有各種型態，我們可以用type()來知道他是哪一種
print("type(year) = :" )
print(type(year))
print("type(month) = :" )
print(type(month))

# 2.使用 str() int() 轉換資料的型態。
year = int(year)
print("轉換後的 type(year) = :" )
print(type(year))

# 3. 使用運算符號 + - * / ，不同型態的資料 井水不犯河水，無法互相運算。
# 字串可以相加，但字串和數字不能相加
print("My name is "+name)
# TODO 下面這個要怎麼改?
print("I was born at"+year+"/"+month+"/"+date)


# TODO 計算出使用者現在幾歲
print("你已經?歲了。")

"""
Q 可以在月份輸入13 嗎?
Q 有人隨便輸入月份的時候怎麼辦? --> A.趕出去 B.請他再輸入一次 C.不理他 D.你連怎麼判斷錯誤都不知道了，還談什麼處理。
"""