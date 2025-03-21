import pygame, random, time, sys
from pygame.locals import *
import pygame.pypm

# Initialize Pygame
pygame.init()

# Game settings
FPS = 60  # Frames per second
FramePerSec = pygame.time.Clock()  # Creating an object to control FPS

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size
SCREEN_WHIDTH = 400
SCREEN_HEIGHT = 600

# Object speeds
SPEED = 5
COINSPEED = 5

# Score variables
SCORE = 0
COINS = 0

# Font settings
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game over", True, BLACK)  # "Game over" text to display when the game ends

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create window
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill("white")  # Fill with white color
pygame.display.set_caption("Game")  # Set window title

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")  # Load enemy image
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.rect.center = (random.randint(40, SCREEN_WHIDTH - 40), 0)  # Set initial random position at the top

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Move enemy down
        if self.rect.bottom > 600:  # If enemy moves out of screen
            self.rect.top = 0  # Reset position to the top
            self.rect.center = (random.randint(30, 370), 0)  # Set random horizontal position
            SCORE += 1  # Increment score for each time the enemy is reset

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Draw the enemy on the screen

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  # Load coin image
        self.image = pygame.transform.scale(self.image, (40, 40))  # Resize coin image
        self.rect = self.image.get_rect()  # Get the rectangle of the coin
        self.rect.center = (random.randint(40, SCREEN_WHIDTH - 40), 0)  # Set initial random position at the top

    def move(self):
        self.rect.move_ip(0, 5)  # Move coin down
        if self.rect.bottom > 600:  # If coin moves out of screen
            self.rect.top = 0  # Reset position to the top
            self.rect.center = (random.randint(30, 370), 0)  # Set random horizontal position

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Draw the coin on the screen

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")  # Load player image
        self.rect = self.image.get_rect()  # Get the rectangle of the player
        self.rect.center = (160, 520)  # Set initial position of the player

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Get the pressed keys

        # Move player left
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        # Move player right
        if self.rect.right < SCREEN_WHIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Draw the player on the screen

# Create objects
P1 = Player()
E1 = Enemy()
COIN = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)  # Add enemy to the group
coins = pygame.sprite.Group()
coins.add(COIN)  # Add coin to the group

all_sprite = pygame.sprite.Group()
all_sprite.add(E1)  # Add enemy to the all_sprite group
all_sprite.add(P1)  # Add player to the all_sprite group
all_sprite.add(COIN)  # Add coin to the all_sprite group

# Set timer event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Increase speed every 1000 milliseconds
        if event.type == QUIT:
            pygame.quit()  # Quit the game on close
            sys.exit()

    # Display background
    DISPLAYSURF.blit(background, (0, 0))

    # Display scores
    score = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score, (10, 10))  # Display score at the top-left
    score2 = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(score2, (370, 10))  # Display coin count at the top-right

    # Update all objects on the screen
    for entity in all_sprite:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()  # Play sound on collision
        time.sleep(1)  # Pause for 1 second after collision

        # Display "Game Over" screen
        DISPLAYSURF.fill(RED)  # Fill the screen with red
        DISPLAYSURF.blit(game_over, (30, 250))  # Display "Game over" text

        pygame.display.update()
        for entity in enemies:  # Remove enemies from the screen
            entity.kill()
        time.sleep(2)  # Pause before quitting
        pygame.quit()  # Quit the game
        sys.exit()

    # Check for collision between player and coins
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound("collect.wav").play()  # Play sound on collecting coin
        COINS += 1  # Increase coin count
        for entity in coins:  # Remove coin from the screen
            entity.kill()
        pygame.display.update()

    # If all coins are collected, create a new coin
    if len(coins) == 0:
        COIN = Coin()  # Create a new coin object
        coins.add(COIN)  # Add new coin to the coins group
        all_sprite.add(COIN)  # Add new coin to the all_sprite group

    # Update the screen
    pygame.display.update()
    FramePerSec.tick(FPS)  # Wait for the next frame to maintain FPS
