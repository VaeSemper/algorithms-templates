"""
Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы
и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.
"""


def is_palindrome(line: str) -> bool:
    line = ''.join(e for e in line if e.isalnum()).lower()
    return line == line[::-1]


if __name__ == '__main__':
    print(is_palindrome(input().strip()))
