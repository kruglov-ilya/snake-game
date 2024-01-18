import playground
from direction import Direction


class Snake:
    position_x: int = 100
    position_y: int = 100
    direction: int = Direction.NONE

    body: list[tuple[int, int]] = [(position_x, position_y), (position_x, position_y)]

    speed = 10

    @staticmethod
    def change_direction(direction: int):
        Snake.direction = direction

    @staticmethod
    def go(growth=False):
        if Snake.direction == Direction.LEFT:
            Snake.position_x -= Snake.speed
        elif Snake.direction == Direction.RIGHT:
            Snake.position_x += Snake.speed
        elif Snake.direction == Direction.UP:
            Snake.position_y -= Snake.speed
        elif Snake.direction == Direction.DOWN:
            Snake.position_y += Snake.speed

        Snake.position_x = Snake.position_x % playground.WIDTH
        Snake.position_y = Snake.position_y % playground.HEIGHT

        if not growth:
            Snake.body.pop(0)
        Snake.body.append((Snake.position_x, Snake.position_y))

    @staticmethod
    def get_rects():
        return [list(part) + [Snake.speed] * 2 for part in Snake.body]
