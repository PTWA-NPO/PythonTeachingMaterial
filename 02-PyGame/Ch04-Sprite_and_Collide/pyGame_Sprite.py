import random
import sys
from os import path

import pygame
from pygame.sprite import collide_circle, spritecollide

# 初始化 initialize
pygame.init()
size = width, height = 640, 480
background_color = (150, 150, 150)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Bubble(pygame.sprite.Sprite):
    def __init__(self, mouse):
        super().__init__()
        self.color = [0, 0, 0]
        self.pos = [mouse[0], mouse[1]]
        self.vec = [random.randint(-20, 20), random.randint(-10, 10)]
        self.radius = 10
        self.image = pygame.image.load(
            path.join(path.dirname(__file__), "intro_ball.gif"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = mouse

    def update(self):
        self.rect.x += self.vec[0]
        self.rect.y += self.vec[1]

        if self.rect.y < 0 or self.rect.bottom > height:
            self.vec[1] = -self.vec[1]
        if self.rect.x < 0 or self.rect.right > width:
            self.vec[0] = -self.vec[0]

        pass

    def get_color(self):
        return (self.color[0], self.color[1], self.color[2])

    def bounce(self):
        self.vec[0] = -self.vec[0]
        self.vec[1] = -self.vec[1]


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = [0, 0, 0]
        self.pos = [x, y]
        # self.vec = [random.randint(-10, 10), random.randint(-10, 0)]
        self.image = pygame.image.load(
            path.join(path.dirname(__file__), "ball2.png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):

        pass


bubble_box = []
bubble_group = pygame.sprite.Group()
ball = Ball(100, 100)
all_sprite_group = pygame.sprite.Group()
all_sprite_group.add(ball)
# 迴圈開始
while 1:
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        bubble = Bubble(pygame.mouse.get_pos())
        bubble_group.add(bubble)
        # bubble_box.append(bubble)
    # 更新遊戲資料
    bubble_group.update()
    all_sprite_group.update()
    collides = pygame.sprite.spritecollide(
        ball, bubble_group, False, collided=pygame.sprite.collide_circle_ratio(0.9))

    for bubble in collides:
        bubble.bounce()

    # 更新遊戲畫面
    screen.fill(background_color)
    all_sprite_group.draw(screen)
    bubble_group.draw(screen)
    # for bubble in bubble_box:

    #     pygame.draw.circle(screen,
    #                        bubble.get_color(),
    #                        bubble.pos,
    #                        bubble.radius,
    #                        0
    #                        )
    pygame.display.flip()
    clock.tick(10)
