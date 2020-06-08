import sys
import pygame
from os import path

# 初始化 initialize
pygame.init()
size = width, height = 320, 240
speed = [10, 10]
background_color = (100, 0, 0)
screen = pygame.display.set_mode(size)
ball = pygame.image.load(path.join(path.dirname(__file__), "intro_ball.gif"))
ballrect = ball.get_rect()
clock = pygame.time.Clock()
# 迴圈開始
while 1:
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 更新遊戲資料
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 更新遊戲畫面
    screen.fill(background_color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(10)
