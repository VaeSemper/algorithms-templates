"""
Id:69676035

Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек. На клавише
написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t. Гоша и Тимофей могут нажать в один момент
времени на k клавиш каждый. Если в момент времени t нажаты все нужные
клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут
нажимать на клавиши вдвоём.
"""
from typing import Tuple


def juggle(number_of_keys: int, arr: str) -> int:
    result = 0
    for time_moment in range(1, 10):
        result += 1 if 0 < arr.count(str(time_moment)) <= number_of_keys else 0
    return result


def read_input() -> Tuple[int, str]:
    number_of_keys = int(input()) * 2
    arr = ''.join([input().strip() for _ in range(4)])
    return number_of_keys, arr


if __name__ == '__main__':
    number_of_keys, arr = read_input()
    print(juggle(number_of_keys, arr))
