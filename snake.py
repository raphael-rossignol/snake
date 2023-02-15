import random
from sys import exit
import time
import pygame

# Global layout
pygame.init()
pygame.font.init()
speed = 15
fps = pygame.time.Clock()
x = 720
y = 480
window = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake")
font = pygame.font.Font(None, 35)

# Condition for the game loop
Running = True
score = 0
score_increment = 1
last_score = ''

# Color set up
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)

# Set up the body size and position as well as the initial direction
body = [[100, 50], [90, 50], [80, 50], [70, 50]]
position = [100, 50]
direction = 'RIGHT'
change_to = direction

# Return a random number within the range of the window to place the fruit
fruit_spawn = False
fruit = [random.randrange(1, (x//10))*10, random.randrange(1, (y//10))*10]


def game_over():        # End the game when condition is trigger
    global last_score

    # Game over text layout
    last_score = score
    game_over_text = pygame.font.Font(None, 50)
    game_over_frame = game_over_text.render('GAME OVER' + '  ' + f'Your score: {score}', True, white)
    game_over_set = game_over_frame.get_rect()
    game_over_set.midtop = (x / 2, y / 4)

    # Display the text
    window.blit(game_over_frame, game_over_set)

    # Refresh the screen
    pygame.display.flip()

    # Wait 2 sec before quiting the program
    time.sleep(2)
    game_menu()


def main_loop():    # Main game loop
    global change_to
    global direction
    global fruit
    global fruit_spawn
    global score

    # Main loop
    while Running:
        for event in pygame.event.get():

            # Quit the program if close button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Receive the arrow keys input
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

        # Check if the snake is touching a fruit, if fruit touched snake increases it length
        if position[0] == fruit[0] and position[1] == fruit[1]:
            fruit_spawn = False
            score += score_increment
        else:
            body.pop()

        # If the snake touched a fruit --> fruit respawn
        if not fruit_spawn:
            fruit = [random.randrange(1, (x // 10)) * 10, random.randrange(1, (y // 10)) * 10]
            fruit_spawn = True

        # Remove the leftover body of the snake (stop infinite body length)
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
        for self in body[1:]:
            if position[0] == self[0] and position[1] == self[1]:
                game_over()

        # Draw the score to the screen
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        window.blit(score_text, (50, 50))

        # Refresh the game at 15 fps
        pygame.display.flip()
        fps.tick(speed)


def game_menu():        # Menu displaying last score and reset the game
    global Running
    global direction
    global change_to
    global body
    global position
    global last_score
    global score

    # Reset game
    Running = False
    body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    position = [100, 50]
    direction = 'RIGHT'
    change_to = direction

    # Press space to play
    while not Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Running = True
                    main_loop()

        # Game_menu text layout
        game_menu_text = pygame.font.Font(None, 50)
        game_menu_frame = game_menu_text.render('PRESS SPACE TO START THE GAME', True, white)
        game_menu_set = game_menu_frame.get_rect()
        game_menu_set.midtop = (x / 2, y / 4)
        score_frame = game_menu_text.render(f'Last score : {last_score}', True, white)
        score_set = score_frame.get_rect()
        score_set.midbottom = (x / 2, y / 4)


        # Display the text
        window.blit(game_menu_frame, game_menu_set)
        window.blit(score_frame, score_set)

        # Refresh the screen
        pygame.display.flip()
        window.fill(black)

        score = 0


game_menu()