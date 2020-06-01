"""
Q 從前面的例子可以看到，我們要多介紹一個人，就要多好幾個資料，因此我們需要有物件的概念。
學習目標:
1. 物件就是一個東西，人、桌子、電視等等，每個東西都會有他的資料。
2. 在程式中我們用Class來設計一個物件應該有的資料和行為。

核心概念：一個物件有資料也有行為，愈好的設計就是愈直覺的設計，一個物件有的行為和資料要名實相符。
"""
import datetime

# 我用date 這個物件組合了 年/月/日 date就是一個物件，統合性的概念。
# birthday = datetime.date(year=2020,month=8,day=15)
# print("我出生於",birthday.year)


# 我們也可以用一個'人'的概念統合這些資料。
class People:
    def __init__(self,name,gender,birthday):
        self.name =name
        self.gender = gender
        self.birthday = birthday
        self.age = self.get_age()

    def get_age(self):
        birthday = self.birthday
        this_birth = datetime.datetime.now()
        age = this_birth.year-birthday.year
        return age
    


    def indroduce(self):
    # 每個人有自我介紹的功能
    # TODO 加上完整的自我介紹
        print("您好，我的名字是"+self.name)
        print("我出生於",self.birthday)
        print("我今年",self.age,"歲")
    # 如果要有其他功能，可以加在下方
    # def ....

user1 = People(name="Kylin",gender="Male",birthday=datetime.date(1993,8,15) )
user1.indroduce()
user2 = People(name="ABC",gender="Female",birthday=datetime.date(1900,12,15) )
user2.indroduce()
"""
TODO Task 5
使用Class的方式做出自我介紹，範例如下。

您好，我的名字是Kylin，可以叫我Kylin 哥哥
我出生於1993
我的生日是  8 月  15 日。
我已經活了  9040 天
再  90 天就是我的生日了~~ 
很高興認識你
"""