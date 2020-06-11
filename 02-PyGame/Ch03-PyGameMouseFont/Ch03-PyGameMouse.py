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
pos = (0, 0)
pos_x = 0
pos_y = 0
radius = 10
circle_box_x = []
circle_box_y = []
circle_box_r = []

while 1:

    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse = pygame.mouse.get_pressed()
    # print(mouse)
    if mouse[0]:
        # 製造一顆圓 泡泡
        pos_x, pos_y = pygame.mouse.get_pos()
        radius = 5
        circle_box_x.append(pos_x)
        circle_box_y.append(pos_y)
        circle_box_r.append(radius)
        # print("Pos :", pos)
        pass

    # 更新遊戲資料
    i = 0
    while i < len(circle_box_x):
        circle_box_y[i] = circle_box_y[i] - 15
        circle_box_r[i] = circle_box_r[i] + 1
        i = i+1
    print("泡泡的數量", len(circle_box_x))

    # 更新遊戲畫面
    screen.fill(background_color)
    # 畫圓
    i = 0
    while i < len(circle_box_x):
        pygame.draw.circle(
            screen,
            (0, 0, 255),
            (circle_box_x[i], circle_box_y[i]),
            circle_box_r[i],
            0
        )
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (circle_box_x[i], circle_box_y[i]),
            circle_box_r[i],
            3
        )
        i = i+1

    pygame.display.flip()
    clock.tick(10)
