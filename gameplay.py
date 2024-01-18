import pygame
from pygame.event import Event
from pygame.time import Clock

from color import Color
from direction import Direction
from playground import playground
from snake import Snake
from treat import Treat

clock = Clock()


def event_handling(event: Event):
    if event.type == pygame.QUIT:
        raise SystemExit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            Snake.direction = Direction.LEFT
        elif event.key == pygame.K_RIGHT:
            Snake.direction = Direction.RIGHT
        elif event.key == pygame.K_UP:
            Snake.direction = Direction.UP
        elif event.key == pygame.K_DOWN:
            Snake.direction = Direction.DOWN


def tick():
    for event in pygame.event.get():
        event_handling(event)

    if Treat.eaten_by_snake():
        Snake.go(growth=True)
        Treat.move()
    else:
        Snake.go()

    playground.fill(Color.WHITE)

    pygame.draw.rect(playground, Color.BLUE, Treat.get_rect())
    for rect in Snake.get_rects():
        pygame.draw.rect(playground, Color.BLACK, rect)

    pygame.display.update()

    clock.tick(10)
