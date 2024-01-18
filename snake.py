from direction import Direction


class Snake:
    position_x: int = 100
    position_y: int = 100
    direction: int = Direction.NONE

    speed = 10

    @staticmethod
    def change_direction(direction: int):
        Snake.direction = direction

    @staticmethod
    def go():
        if Snake.direction == Direction.LEFT:
            Snake.position_x -= Snake.speed
        elif Snake.direction == Direction.RIGHT:
            Snake.position_x += Snake.speed
        elif Snake.direction == Direction.UP:
            Snake.position_y -= Snake.speed
        elif Snake.direction == Direction.DOWN:
            Snake.position_y += Snake.speed

    @staticmethod
    def get_rect():
        return [Snake.position_x, Snake.position_y, 10, 10]