# Ch02 PyGame Draw and Keyboard Event
讓我們開始在螢幕上畫出圖形!

## 觸發鍵盤事件

**Ｑ**　當我們按下鍵盤的時候，就會傳送一個訊號給電腦，那電腦是如何知道我們按了哪個按鍵呢?

> 電腦中會將按鍵編號，只要依照編號確認按鍵的電訊號，就知道哪個按鍵被按下了。

**Ｑ**　在程式中我們要如何知道鍵盤的狀態?
> 以Pygame為例，只要執行下面這行程式，我們就能拿到所有按鍵的狀態，1就是有按下 0則表示沒有按下。
```python
keys = pygame.key.get_pressed()
print(keys)
```


**Ｑ**　請問那個0 和這個1是哪個按鍵的狀態?
> PyGame一樣有將按鍵作對應的數字編號，ex 向上鍵對應的數字就是273，但我們不用背所有的編號，只要輸入變數就可以帶我們找到正確的號碼，這也是善用全域變數的小技巧。
:::info
pygame.K_UP = 273 代表 鍵盤 'UP'的編號

pygame.K_a  =  97 代表 鍵盤 'A' 的編號。

其他還有很多鍵盤事件，請參考 https://www.pygame.org/docs/ref/key.html
:::



## 無以規矩不成方圓，無以Pygame.Draw 無法畫圓畫方

* 畫圓
```python
# 設定圓形參數
circle_color = (255, 131, 124)
circle_pos = (200, 300)
circle_radius = 10
circle_width = 3

#畫圓
pygame.draw.circle(
    screen,
    circle_color,
    circle_pos,
    circle_radius+i,
    circle_width
)
```

* 畫方
```python
# 設定矩形參數
rect_color = (0, 204, 255)
rect_pos_x = 100
rect_pos_y = 100
rect_width = 100
rect_height = 50

#畫方
pygame.draw.rect(
    screen,
    rect_color,
    Rect(rect_pos_x,rect_pos_y,rect_width,rect_height)
)
```

## PyGame 中的矩形
@ 矩形的參數


## 我變我變我變變變 

* 將圖片放大或縮小成特定尺寸
```python
pygame.transform.scale(screen,(width,height))
```

* 將圖片旋轉一個角度
```python
pygame.transform.rotate(screen,angle)
```

**Ｑ**　為什麼圖片畫質會愈來愈差?
> 因為每經過一次轉化、變形、放大縮小，圖片就會失真，因此我們有個小技巧，用一個變數儲存原始圖片，每次變形就用原始圖片來操作。

```python
# 讀取圖片，用origin_image儲存原始圖片
image = pygame.image.load(
    path.join(path.dirname(__file__),
              "hannah-lily8-0.jpg"))
origin_image = image

# 用原始圖片進行放大再旋轉
# 注意這裡，使用image和origin_image是否有什麼不同呢?
image = pygame.transform.scale(  origin_image, (200, 150))
image = pygame.transform.rotate(image, angle)
```

## Task: 

1. 用方向鍵控制一個圓形向上向下向左向右。
2. 用方向鍵控制一個矩形的大小和顏色
3. 用方向鍵控制一個圖片的大小和旋轉角度
上下控制大小，左右旋轉角度

## Homework 

試著結合動畫與上下左右，控制動畫的大小與旋轉角度。
