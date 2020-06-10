import sys
import pygame
from pygame import Rect
from os import path


# 初始化 initialize
pygame.init()
size = width, height = 640, 480
background_color = 100, 100, 100
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# 讀取圖片，用origin_image儲存原始圖片
image = pygame.image.load(
    path.join(path.dirname(__file__),
              "hannah-lily8-0.png"))
origin_image = image
# 設定透明色彩
# origin_image.set_colorkey((0, 0, 0))
image_rect = image.get_rect()
image_scale_var = 0
image_roate_angle = 0

while 1:

    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        image_scale_var = image_scale_var+10
    elif keys[pygame.K_DOWN]:
        image_scale_var = image_scale_var-10
    if keys[pygame.K_LEFT]:
        image_roate_angle = image_roate_angle-1
    elif keys[pygame.K_RIGHT]:
        image_roate_angle = image_roate_angle+1

    # 更新遊戲資料

    # 更新遊戲畫面
    screen.fill(background_color)

    # 用原始圖片進行放大再旋轉
    # 注意這裡，使用image和origin_image是否有什麼不同呢?
    image = pygame.transform.scale(
        origin_image, (200+image_scale_var, 150+image_scale_var))
    image = pygame.transform.rotate(image, image_roate_angle)
    screen.blit(image, image_rect)

    pygame.display.flip()
    clock.tick(10)
