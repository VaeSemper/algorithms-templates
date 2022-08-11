"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу
вывести их сумму, также в двоичной системе. Встроенную в язык
программирования возможность сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального
числа на входе.
"""
from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    max_len = max(len(first_number), len(second_number))
    first_number = first_number.zfill(max_len)
    second_number = second_number.zfill(max_len)
    next_bit = 0
    result = ''
    for index in reversed(range(max_len)):
        bit = next_bit
        bit += 1 if first_number[index] == '1' else 0
        bit += 1 if second_number[index] == '1' else 0
        result += '1' if bit % 2 == 1 else '0'
        next_bit = 0 if bit < 2 else 1
    if next_bit:
        result += '1'
    return result[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


if __name__ == '__main__':
    first_number, second_number = read_input()
    print(get_sum(first_number, second_number))
