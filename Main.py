import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480

window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Snake Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
