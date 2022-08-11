"""
Напишите программу, которая определяет, будет ли положительное целое число
степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое
неотрицательное число.
"""
from math import log


def is_power_of_four(number: int) -> bool:
    return log(number, 4).is_integer()


if __name__ == '__main__':
    print(is_power_of_four(int(input())))
