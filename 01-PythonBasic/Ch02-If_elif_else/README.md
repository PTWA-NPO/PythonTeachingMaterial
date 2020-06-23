# Chapter 02 使用條件判斷句控制程式流程
<!-- TODO 加上比較符號 比較 == <= >=  -->
## 動動腦
:::warning
Q 月份可以大於12嗎? 可以小於1嗎? 我們該怎麼檢查月份是不是合理的?
    **如果**月份>12，**就** 顯示`你騙我，月份不能大於 12 阿!`
    **如果**月份<1，**就** 顯示`別開玩笑了，月份不可能小於 1`
:::
## Python語法 如果...就...
```python
if month>12:
    print("你騙我，月份不能大於 12 阿!")

if month<1:
    print("別開玩笑了，月份不可能小於 1")

```

## 如果...否則如果...否則...
```python
if month>12:
    print("你騙我，月份不能大於 12 阿!")
elif month<1:
    print("別開玩笑了，月份不可能小於 1")
else :
    print("謝謝你的配合，你的月份是正常的")
```
:::info
* Python中，每開啟一個程式區塊，就需要一個`':'`。
* 為了美觀起見，Python規定同一區塊的程式要空出同樣的格子數，都會是4的倍數。
* 不可以打了冒號，但下一行沒有程式縮排；不可以沒有冒號就縮排。
* 如果打了冒號，暫時不想寫程式可以使用 `pass` 
```python
if month>12:
    print("你騙我，月份不能大於 12 阿!")
    print("我們在同一個程式區塊")
else :
    pass
```
:::
<!-- TODO 流程圖 -->

## 比較符號 Comparison
1. 基礎條件判斷式，判斷這個條件是否成立，比較符號如下。
```python
if a > b :
    print("a 大於 b")
elif a < b :
    print("a 小於 b")
elif a == b :
    print("a 等於 b")

if a >= b :
    print("a 大於等於 b")
elif a <= b :
    print("a 小於等於 b")

if a != b :
    print("a 不等於 b")

```
2. 多個條件 
* 邏輯1 如果 月份大於1 **而且** 月份小於12 就自我介紹。
```py
month = 11
if month > 1 and month<12:
    print("自我介紹，我出生的月份是",month,"月")
else :
    print("別開玩笑了，月份不可能是 ",month)
```
* 邏輯2 如果 月份小於1 **或** 月份大於12 就輸出錯誤訊息。
```py
month = -1
if month<1 or month>12  :
    print("別開玩笑了，月份不可能是 ",month)
else :
    print("自我介紹，我出生的月份是",month,"月")
```

## Boolean
這種條件判斷的結果是對或錯的資料，我們就叫布林值(Boolean)
在電腦中，我們用0 1表示對錯，真假。

* 1 就是 對 就是真 英文是 True
* 0 就是 錯 就是假 英文是 False
