import sys
import pygame
from pygame import Rect
from os import path


# 初始化 initialize
pygame.init()
size = width, height = 640, 480
background_color = 200, 200, 200
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# 設定圓形參數
circle_color = (3, 169, 244)
circle_pos = (150, 150)
circle_radius = 100
circle_width = 0

# 設定矩形參數
rect_color = (233, 30, 99)
rect_pos_x = 400
rect_pos_y = 200
rect_width = 200
rect_height = 150


while 1:

    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 更新遊戲資料
    # TODO Task1 & 2

    # 更新遊戲畫面
    screen.fill(background_color)

    # 畫圓
    pygame.draw.circle(
        screen,
        circle_color,
        circle_pos,
        circle_radius,
        circle_width
    )

    # 畫方
    pygame.draw.rect(
        screen,
        rect_color,
        Rect(rect_pos_x, rect_pos_y, rect_width, rect_height)
    )
    pygame.display.flip()
    clock.tick(10)
