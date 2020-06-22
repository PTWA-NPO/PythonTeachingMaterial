import sys
import pygame
from os import path

# 初始化 initialize
pygame.init()
size = width, height = 640, 480

background_color = (3, 169, 244)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = [50, 50]

        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 235, 59))
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    def move(self):
        pass

    def update(self):
        pass


GAME_WIDTH = 800
GAME_HEIGHT = 600
rect = pygame.Rect(0, 0, GAME_WIDTH, GAME_HEIGHT)
sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)
# 迴圈開始
while 1:
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 更新遊戲資料
    keys = pygame.key.get_pressed()
    # print(keys)
    # print(pygame.K_UP)
    # print(pygame.K_a)
    if keys[pygame.K_UP]:
        rect.move_ip(0, -15)
    elif keys[pygame.K_DOWN]:
        rect.move_ip(0, +15)
    elif keys[pygame.K_LEFT]:
        rect.move_ip(-15, 0)
    elif keys[pygame.K_RIGHT]:
        rect.move_ip(15, 0)

        # 更新遊戲畫面
    screen.fill(background_color)
    pygame.draw.rect(screen, WHITE, rect, 5)
    sprite_group.draw(screen)
    # screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(10)
