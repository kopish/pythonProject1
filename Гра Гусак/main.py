import pygame
from pygame. constants import QUIT


pygame.init()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RAD = 255, 0, 0
BLUE = 0, 0, 255

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill((255, 255, 255))
bal_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    bal_rect = bal_rect.move(ball_speed)
    if bal_rect.bottom >= height or bal_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball.fill(WHITE)
    if bal_rect.right >= width or bal_rect.right <= 0:
        ball_speed[0] = ball_speed[1]
        ball.fill(RAD)
    if bal_rect.left >= width or bal_rect.left <= 0:
        ball_speed[0] = ball_speed[1]
        ball.fill(BLUE)
    main_surface.fill((0, 0, 0))
    main_surface.blit(ball, (bal_rect))


    # main_surface.fill((155, 155, 155))
    pygame.display.flip()