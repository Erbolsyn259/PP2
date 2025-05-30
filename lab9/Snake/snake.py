import pygame, sys, random  # Import necessary libraries

pygame.init()  # Initialize pygame

# Set up the game window and clock
pygame.display.set_caption("Snake!")  # Set the title of the window
screen = pygame.display.set_mode((800, 800))  # Set the screen size to 800x800
clock = pygame.time.Clock()  # Create a clock object to man`age FPS
sw, sh = 800, 800  # Set screen width and height variables
block_size = 50  # Size of each snake block
font = pygame.font.Font("font.ttf", 24)  # Font for rendering text
dead = False  # Variable to track if the snake is dead

# Snake class, which represents the player (the snake)
class Snake:
    def __init__(self):
        self.x, self.y = block_size, block_size  # Set initial position of the snake's head
        self.dirx = 1  # Snake's initial movement direction on x-axis (right)
        self.diry = 0  # Snake's initial movement direction on y-axis (no movement)
        self.level = 1  # Snake's initial level
        self.speed = 5  # Snake's initial speed
        self.head = pygame.Rect(self.x, self.y, block_size, block_size)  # Create the head rectangle
        self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]  # Initialize the snake's body
        self.dead = False  # Variable to track if the snake is dead

    # Update the snake's position and handle collisions
    def update(self):
        for squere in self.body:  # Check if the head collides with any part of the body
            if self.head.x == squere.x and self.head.y == squere.y:
                self.dead = True  # If head collides with body, snake dies
            if self.head.x < 0 or self.head.x >= sw or self.head.y < 0 or self.head.y >= sh:  # Check if the snake hits the wall
                self.dead = True
        self.body.append(self.head)  # Add the head to the body
        for i in range(len(self.body) - 1):  # Move the body by shifting each square
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.dirx * block_size  # Update the head's x position
        self.head.y += self.diry * block_size  # Update the head's y position
        self.body.remove(self.head)  # Remove the last part of the body to maintain the snake's length

    # Draw the score and level on the screen
    def scoreDrawing(self):
        score_text = "Score: " + str(len(snake.body) - 3)  # Calculate score based on snake's body length
        score_surface = font.render(score_text, True, (56, 74, 12))  # Render the score text
        score_rect = score_surface.get_rect(center=(block_size * block_size - 120, 40))  # Set the position of the score
        screen.blit(score_surface, score_rect)  # Draw the score on the screen

        level_text = "Level: " + str(self.level)  # Display current level
        level_surface = font.render(level_text, True, (56, 74, 12))  # Render the level text
        level_rect = level_surface.get_rect(center=(block_size * block_size - 120, 70))  # Set the position of the level
        screen.blit(level_surface, level_rect)  # Draw the level on the screen

# Load apple image and scale it to fit the grid
# Apple class, which represents the food for the snake
class Apple:
    def __init__(self):
        self.food = random.randint(1,3)
        self.apples1 = pygame.image.load(f'food{self.food}.png').convert_alpha()  # Load apple image with transparency
        self.apples = pygame.transform.scale(self.apples1, (40, 40))  # Resize apple image
        self.x = int(random.randint(0, sw) / block_size) * block_size  # Random x position
        self.y = int(random.randint(0, sh) / block_size) * block_size  # Random y position
        self.rect = pygame.Rect(self.x, self.y, block_size,block_size)  # Create apple rectangle
        self.TimeEvent = pygame.USEREVENT + 1
        if self.food == 1:
            pygame.time.set_timer(self.TimeEvent,12 * 1000)
        elif self.food == 2:
            pygame.time.set_timer(self.TimeEvent,6 * 1000)
        elif self.food == 3:
            pygame.time.set_timer(self.TimeEvent,3 * 1000)

    def update(self):
        screen.blit(self.apples, self.rect)  # Draw the apple on the screen

# Initialize snake and apple objects
snake = Snake()
apple = Apple()

score = font.render("", True, "green")  # Create a surface for the score text
score_rect = score.get_rect(center=(575, 50))  # Set the position of the score
level = font.render("", True, "green")  # Create a surface for the level text
level_rect = level.get_rect(center=(575, 85))  # Set the position of the level

# Draw the grid on the screen
def DrawGrid():
    for x in range(0, sw, block_size):  # Draw vertical lines for the grid
        for y in range(0, sh, block_size):  # Draw horizontal lines for the grid
            rect = pygame.Rect(x, y, block_size, block_size)  # Create rectangle for each grid cell
            pygame.draw.rect(screen, (50, 100, 50), rect, 1)  # Draw the grid cell

# Main game loop
while True:
    for event in pygame.event.get():  # Handle events (e.g., key presses)
        if event.type == pygame.QUIT:  # If the player closes the window, quit the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Check for key presses
            if event.key == pygame.K_DOWN:  # If DOWN arrow is pressed, move snake down
                snake.dirx = 0
                snake.diry = 1
            elif event.key == pygame.K_UP:  # If UP arrow is pressed, move snake up
                snake.dirx = 0
                snake.diry = -1
            elif event.key == pygame.K_RIGHT:  # If RIGHT arrow is pressed, move snake right
                snake.dirx = 1
                snake.diry = 0
            elif event.key == pygame.K_LEFT:  # If LEFT arrow is pressed, move snake left
                snake.dirx = -1
                snake.diry = 0 
            if event.key == pygame.K_s:  # If 'S' is pressed, move snake down
                snake.dirx = 0
                snake.diry = 1
            elif event.key == pygame.K_w:  # If 'W' is pressed, move snake up
                snake.dirx = 0
                snake.diry = -1
            elif event.key == pygame.K_d:  # If 'D' is pressed, move snake right
                snake.dirx = 1
                snake.diry = 0
            elif event.key == pygame.K_a:  # If 'A' is pressed, move snake left
                snake.dirx = -1
                snake.diry = 0 
        if event.type == apple.TimeEvent:
            apple = Apple()
    snake.update()  # Update the snake's position and check for collisions
    if snake.dead:  # If the snake is dead, break the loop and end the game
        break

    screen.fill((0, 0, 0))  # Fill the screen with black
    apple.update()  # Update the apple's position
    score = font.render(f"Score: {len(snake.body) + 1}", True, "green")  # Update the score text
    level = font.render(f"Level: {snake.level}", True, "green")  # Update the level text
    pygame.draw.rect(screen, (0, 255, 0), snake.head)  # Draw the snake's head
    for squere in snake.body:  # Draw each part of the snake's body
        pygame.draw.rect(screen, (0, 255, 0), squere)

    DrawGrid()  # Draw the grid

    snake.scoreDrawing()  # Draw the score and level

    screen.blit(score, score_rect)  # Display the score on the screen
    screen.blit(level, level_rect)  # Display the level on the screen

    # If the snake eats the apple, grow the snake and increase the level
    if snake.head.x == apple.x and snake.head.y == apple.y:
        for i in range(0,apple.food):
            snake.body.append(pygame.Rect(squere.x, squere.y, block_size, block_size))
            if (len(snake.body) - 3) % 3 == 0:  # Every 3 apples eaten, increase level and speed
                snake.level += 1
                snake.speed += 0.5  # Add a new segment to the snake
        apple = Apple()  # Create a new apple
        #pygame.time.set_timer(appleTimeEvent,apple.time)

    pygame.display.update()  # Update the display
    clock.tick(snake.speed)  # Control the game's frame rate based on the snake's speed
