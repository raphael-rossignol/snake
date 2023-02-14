import pygame
import random

# Global layout

pygame.init()
speed = 15
fps = pygame.time.Clock()
x = 720
y = 480
window = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")

# Condition for the game loop

Running = True

# Color set up

green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)

# Set up the body size and position as well as the initial direction

body = [[100, 50], [90, 50], [80, 50], [70, 50]]
position = [100, 50]
direction = 'RIGHT'
change_to = direction

# Return a random number within the range of the window to place the fruit

fruit = [random.randrange(1, (x//10))*10, random.randrange(1, (y//10))*10]


def game_over():        # End the game if a condition is trigger
    global Running
    Running = False
    pygame.quit()
    quit()


# Main loop

while Running:

    # Receive the arrow keys input

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # While Running the snake moves into the direction defined by the user's input

    if direction == 'UP':
        position[1] -= 10
    if direction == 'DOWN':
        position[1] += 10
    if direction == 'LEFT':
        position[0] -= 10
    if direction == 'RIGHT':
        position[0] += 10

    # Refresh the position of the snake

    body.insert(0, list(position))

    # Remove the leftover body of the snake while moving

    body.pop()
    window.fill(black)

    # Create the physical form of the snake and fruits

    for pos in body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(window, red, pygame.Rect(fruit[0], fruit[1], 10, 10))

    # If the snake touch a wall --> game_over

    if position[0] < 0 or position[0] > x - 10:
        game_over()
    if position[1] < 0 or position[1] > y - 10:
        game_over()

    # If the snake touch itself --> game_over

    for self in body:
        if position[0] == self[0] and position[1] == self[1]:
            game_over()

    pygame.display.update()
    fps.tick(speed)
