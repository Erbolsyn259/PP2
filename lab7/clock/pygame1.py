import pygame,datetime
from pygame import mixer
from random import randint
# black - minute, blue - hour, red - second

# Инициализация Pygame
pygame.init()
mixer.init()
mixer.music.load('tictac.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)



# Создаем окно
screen = pygame.display.set_mode((800, 800))

# Создаем заголовок окна
pygame.display.set_caption('Clock')
#Ограничение частоты кадров
clock = pygame.time.Clock()
FPS = 1
done = False

# Загружаем изображение
myClock = pygame.image.load('clock.png')
myClock = pygame.transform.scale(myClock,(600,600))

hour_arrow = pygame.image.load('hour.png')
hour_arrow = pygame.transform.scale(hour_arrow,(23,166))
minute_arrow  = pygame.image.load('minute.png')
minute_arrow = pygame.transform.scale(minute_arrow,(20,233))
second_arrow = pygame.image.load('second.png')
second_arrow = pygame.transform.scale(second_arrow,(16,266))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    my_time = datetime.datetime.now()
    hourINT = int(my_time.strftime("%I"))
    minuteINT = int(my_time.strftime("%M"))
    secondINT = int(my_time.strftime("%S"))

    angleHOUR = hourINT* 30 * -1
    angleMINUTE = minuteINT *6* -1
    angleSECOND = secondINT *6*-1

    hour = pygame.transform.rotate(hour_arrow,angleHOUR)
    minute = pygame.transform.rotate(minute_arrow,angleMINUTE)
    second = pygame.transform.rotate(second_arrow,angleSECOND)

    green = randint(0,255)
    red = randint(0,255)
    blue = randint(0,255)

    screen.fill((245,245,245))
    screen.blit(myClock,(100,100))
    screen.blit(second, ((399 - int(second.get_width()/2)),400 - int(second.get_height()/2)))
    screen.blit(hour, ((399 - int(hour.get_width()/2)),400 - int(hour.get_height()/2)))
    screen.blit(minute, ((399 - int(minute.get_width()/2)),400 - int(minute.get_height()/2)))
    pygame.draw.circle(screen, (green,red,blue),(400,400),20)
    pygame.display.flip()
    clock.tick(FPS)



# Закрываем Pygame
pygame.quit()
