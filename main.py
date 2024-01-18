import pygame

import gameplay

pygame.init()
display = pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption('SnakeGame')

x1 = 300
y1 = 300

clock = pygame.time.Clock()


while True:
    gameplay.tick(display)


