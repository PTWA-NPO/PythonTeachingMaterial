# Chapter 03 Module

## 動動腦
* 大雄有問題會找誰?　小叮噹
* 小叮噹怎麼幫助他?　從百寶袋拿出道具。

> 程式也是一樣，有很多的工具可以使用，我們就試試其中一種工具吧。

* 延續上次的作業，請問我的程式過了幾年還可以用嗎?還可以正確算出年齡嗎?

## datetime 
因為要讓程式到了明年還能用，因此我們需要取得當天的日期、年分，此時使用datetime模組
```py
# 告訴程式我們會用到什麼工具
import datetime 
# 使用datetime模組的 now() 指令取得當下的時間
today = datetime.datetime.now()

# 也可以使用datetime模組，將我們的生日年月日包起來。
birthday = datetime.datetime(int(year),month,date)
```
## 模組的概念
* 一個模組就像一個工具箱，裡面會分類，會有很多種類似但是不同的工具。
* 每種工具的使用方式不同，為了避免誤用，最好的方式是查使用說明書。
* 透過 `.` 來取得某個模組的某個工具或是某個功能。
* 有發現 `datetime.datetime.now()` 怎麼使用的嗎? 是不是需要一個`today`儲存結果?

## Task 3 
:::success
1. 結合前面用過的程式，詢問使用者的名字，性別，還有生日。
2. 告訴使用者還有幾天生日? 還有幾天就幾歲了 ex: 恭喜你再101天就20歲了。
:::

## 使用隨機模組 random
```py
import random
# 使用隨機模組產生一個數字
final_number = random.randint(0, 100)
print(final_number)
```