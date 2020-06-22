# Ch05 PyGame Music and Sound
讓我們開始播放聲音和音效吧!

## 音效、Sound
```python
pygame.mixer.init()
pop_sound = pygame.mixer.Sound(
    path.join(path.dirname(__file__), 'space ripple.wav'))
pop_sound.stop()
pop_sound.play()
```
## 音樂、Music
```python
pygame.mixer.music.play()
```

## 時間閘門
```python
   time = pygame.time.get_ticks()
    print(time)
    if keys[pygame.K_UP] and time-begin_time > SOUND_FREQ:
        begin_time = time
        pop_sound.stop()
        pop_sound.play()
```

**Ｑ**　