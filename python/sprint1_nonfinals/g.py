"""
Вася реализовал функцию, которая переводит целое число из десятичной системы
в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.
"""


def to_binary(number: int) -> str:
    binary = ''
    while number:
        if number & 1:
            binary += '1'
        else:
            binary += '0'
        number >>= 1
    return binary[::-1]


def read_input() -> int:
    return int(input().strip())


if __name__ == '__main__':
    print(to_binary(read_input()))
