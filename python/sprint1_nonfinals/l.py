"""
Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2
строки s и t, состоящие только из строчных букв. Строка t получена
перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
Нужно найти добавленную букву.
"""
from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    result = list(longer)
    for char in shorter:
        result.remove(char)
    return result[0]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


if __name__ == '__main__':
    shorter, longer = read_input()
    print(get_excessive_letter(shorter, longer))
