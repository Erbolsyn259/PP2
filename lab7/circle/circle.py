import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

FPS = 50
done = False
posX = 400
posY = 400
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        green = randint(0,255)
        red = randint(0,255)
        blue = randint(0,255)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if posY > 20:
                posY -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if posY < 780:
                posY += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if posX > 20:
                posX -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if posX <780:
                posX += 20
        screen.fill((red,green,blue))
        pygame.draw.circle(screen, (0,200,0),(posX,posY),50)
        pygame.display.flip()
        clock.tick(FPS)
pygame.quit()
        
