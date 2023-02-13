import pygame
pygame.init()
fps = 15
fpsclock = pygame.time.Clock()

window = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Snake")
Running = True
green = pygame.Color(0, 255, 0)
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
p1 = 10
p2 = 10
step = 5


while Running:

    pygame.draw.rect(window, green, (p1, p2, 10, 10))
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= step
    if key_input[pygame.K_UP]:
        p2 -= step
    if key_input[pygame.K_RIGHT]:
        p1 += step
    if key_input[pygame.K_DOWN]:
        p2 += step
    window.fill((0, 0, 0))
    pygame.display.update()
    fpsclock.tick(fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Running = False
