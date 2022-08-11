"""
Чтобы подготовиться к семинару, Гоше надо прочитать статью по
эффективному менеджменту. Так как Гоша хочет спланировать день заранее,
ему необходимо оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и в
нём ищется самое длинное слово. Его длина и будет условной сложностью
статьи.
"""
from typing import List


def get_longest_word(line: List[str]) -> str:
    result = ''
    for word in line:
        if len(word) > len(result):
            result = word
    return result


def read_input() -> List[str]:
    _ = input()
    line = input().strip().split()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


if __name__ == '__main__':
    print_result(get_longest_word(read_input()))
