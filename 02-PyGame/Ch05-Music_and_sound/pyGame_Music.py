import sys
import pygame
from os import path
SOUND_FREQ = 100
# 初始化 initialize
pygame.init()
pygame.mixer.init()
size = width, height = 320, 240
background_color = (100, 0, 0)
begin_time = 0
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
pop_sound = pygame.mixer.Sound(
    path.join(path.dirname(__file__), 'space ripple.wav'))
bgm = pygame.mixer.music.load(
    path.join(path.dirname(__file__), '傳承恆遠悠揚-輕音樂.mp3'))

# 迴圈開始
pygame.mixer.music.play()
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
    time = pygame.time.get_ticks()
    print(time)
    if keys[pygame.K_UP] and time-begin_time > SOUND_FREQ:
        begin_time = time
        pop_sound.stop()
        pop_sound.play()

    # 更新遊戲畫面
    screen.fill(background_color)

    pygame.display.flip()
    clock.tick(30)
