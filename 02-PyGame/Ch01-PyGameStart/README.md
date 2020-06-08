# Ch01 PyGame Basic

## 遊戲運作的大小事
### 動動腦
Q. 執行 pyGameIntroduction.py，你看到什麼?
A. 有視窗、有一張球的圖片、球有小鋸齒、會移動
Q. 跟我們一開始學執行程式，執行的狀態有什麼不同嗎?
A. 一開始學的程式，執行到底，輸出結果就結束了，遊戲程式會不斷執行，直到我們按下叉叉才會結束。

### 遊戲是事件驅動的程式
* 按下叉叉會關閉視窗，是因為我們設定了按下叉叉後執行關閉這個功能。
* 按下叉叉-->就是一種事件，其他還有按下鍵盤、按下按鈕、按下滑鼠等等事件

* **以下示範請勿隨便嘗試**
:::warning 
把這一段
```python
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
```
改成
```python
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
            # sys.exit()
```
叉叉的功能就失效囉，需要從工作管理員強制關閉。
:::

### 顏色的組成

* 電腦中的顏色是Red Green Blue三種色光組成的，也就是所謂的色光三原色，跟顏料三原色是不同的。
可以到這個網站 https://www.w3schools.com/colors/colors_picker.asp 玩玩看。
* * Q. 為什麼最大值是255?
A. 因為電腦中是用8bit的大小來表示每種色光比例，8bit最多能表示的數值轉成10進位就是255。
**小試身手**
:::success
試著將顏色的RGB換成不一樣的數值
```python
background_color = (0,0,0 )
```
:::

### 畫面的更新

* 遊戲畫面更新的原理跟動畫一樣，每秒更新的次數只要超過24次，大腦就會覺得東西動起來了
Q. 為什麼球卡卡的? 是因為他的速度 speed太慢，還是畫面更新的頻率太慢了?
**小試身手**
:::success
試著將clock.tick 裡面的數字加大或減少，調整畫面更新的**頻率**。
```python
    # 更新遊戲畫面
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(10)
```
:::
Q. 如果把這行註解掉，會發生什麼事?為什麼會這樣?


### 遊戲的座標軸

### Image Rectangle
* PyGame中圖片會有一個矩形物件，決定這張圖片要繪製的位置與大小
請參考 https://www.pygame.org/docs/ref/rect.html 了解如何取得Rect座標位置與如何改變物件位置。
```python
ballrect = ballrect.move()
```

### 遊戲迴圈


## 練習1
下載一張自己喜歡的圖片，並把圖片放到遊戲視窗中。

## 練習2
1. Google搜尋 Gif 找一組喜歡的動畫，並下載
2. 把gif丟到 https://image.online-convert.com/convert/gif-to-jpg  
3. 仿造 pyGame_Animation.py 製作屬於自己的動畫
© Hannah Lily

## 練習3
讓我們遊戲的背景顏色可以隨機改變顏色。