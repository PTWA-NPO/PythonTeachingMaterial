import sys
import pygame
from os import path

# 初始化 initialize
pygame.init()
size = width, height = 640, 480
background_color = 100, 100, 100
screen = pygame.display.set_mode(size)
images = []
clock = pygame.time.Clock()
for i in range(0, 75):
    image = pygame.image.load(
        path.join(path.dirname(__file__),
                  "images",
                  "hannah-lily8-"+str(i)+".jpg"))
    images.append(image)
image_rect = images[0].get_rect()
i = 0

# 迴圈開始
while 1:

    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 更新遊戲資料
    image = images[i]
    i = i+1
    if i > 74:
        i = 0

    # 更新遊戲畫面
    screen.fill(background_color)
    screen.blit(image, image_rect)
    pygame.display.flip()
    clock.tick(30)
