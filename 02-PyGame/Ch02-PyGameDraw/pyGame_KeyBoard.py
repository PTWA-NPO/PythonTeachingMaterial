import sys
import pygame
from pygame import Rect
from os import path


# 初始化 initialize
pygame.init()
size = width, height = 640, 480
background_color = (100, 100, 100)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while 1:

    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    # print(keys)
    # print(pygame.K_UP)
    # print(pygame.K_a)
    if keys[pygame.K_UP]:
        print("UP")
        background_color = (50, 50, 50)

    elif keys[pygame.K_DOWN]:
        print("DOWN")
        background_color = (200, 200, 200)

    # 更新遊戲資料

    # 更新遊戲畫面
    screen.fill(background_color)

    pygame.display.flip()
    clock.tick(30)
