import random

import playground
from snake import Snake


class Treat:
    position_x: int = 100
    position_y: int = 100

    @staticmethod
    def get_rect():
        return Treat.position_x, Treat.position_y, Snake.speed, Snake.speed

    @staticmethod
    def move():
        Treat.position_x, Treat.position_y = Treat.__find_allowed_cell(
            random.randint(0, playground.WIDTH / Snake.speed) * Snake.speed,
            random.randint(0, playground.HEIGHT / Snake.speed) * Snake.speed)
        print(Treat.position_x, Treat.position_y)

    @staticmethod
    def eaten_by_snake() -> bool:
        return Snake.position_x == Treat.position_x and Snake.position_y == Treat.position_y

    @staticmethod
    def __find_allowed_cell(start_x: int, start_y: int) -> tuple[int, int]:
        for x in range(0, playground.WIDTH, Snake.speed):
            for y in range(0, playground.HEIGHT, Snake.speed):
                if ((start_x + x) % playground.WIDTH, (start_y + y) % playground.HEIGHT) not in Snake.body:
                    return start_x, start_y
        print("You win!!!")
        raise SystemError("You win!!")
