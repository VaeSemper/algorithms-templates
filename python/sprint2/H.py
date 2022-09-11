"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно
популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

пустая строка —– правильная скобочная последовательность; правильная
скобочная последовательность, взятая в скобки одного типа, –— правильная
скобочная последовательность; правильная скобочная последовательность с
приписанной слева или справа правильной скобочной последовательностью —–
тоже правильная. На вход подаётся последовательность из скобок трёх видов: [
], (), {}. Напишите функцию is_correct_bracket_seq, которая принимает на
вход скобочную последовательность и возвращает True, если последовательность
правильная, а иначе False.
"""


def is_correct_bracket_seq(seq):
    if len(seq) == 0:
        return True
    result = []
    d = {'(': ')', '{': '}', '[': ']'}
    for bracket in seq:
        if bracket in '({[':
            result.append(bracket)
        elif len(result) != 0 and bracket == d[result[-1]]:
            result.pop()
        else:
            result.append(bracket)
            break
    if len(result) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_correct_bracket_seq(input()))
