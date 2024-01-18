import pygame
from pygame import Surface, SurfaceType
from pygame.event import Event
from pygame.time import Clock

from color import Color
from direction import Direction
from snake import Snake

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


def tick(display: Surface | SurfaceType):
    for event in pygame.event.get():
        event_handling(event)

    Snake.go()

    display.fill(Color.WHITE)
    pygame.draw.rect(display, Color.BLACK, Snake.get_rect())
    pygame.display.update()

    clock.tick(30)
