"""
У Тимофея было n стажёров. Каждый стажёр хотел быть лучше своих
предшественников, поэтому i-й стажёр делал столько коммитов, сколько делали
два предыдущих стажёра в сумме. Два первых стажёра были менее инициативными —–
они сделали по одному коммиту.
Пусть Fi —– число коммитов, сделанных i-м стажёром (стажёры нумеруются с нуля).
Тогда выполняется следующее: F0=F1=1. Для всех i≥2 выполнено Fi=Fi−1+Fi−2.
Определите, сколько кода напишет следующий стажёр –— найдите последние k цифр
числа Fn.
"""


n, k = (int(i) for i in input().split())
ab = [1, 1]
d = 10 ** k

if n < 2:
    fib = 1
else:
    n -= 1
    for i in range(n):
        s = (ab[0] + ab[1]) % d
        ab[0] = ab[1]
        ab[1] = s
        fib = ab[1]
print(fib)

# def fibonacci_recursive_mod(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci_recursive_mod(n - 1) + fibonacci_recursive_mod(n - 2)
#
#
# def read_input():
#     n, k = [int(i) for i in input().split()]
#     n += 1
#     return n, k
#
#
# if __name__ == '__main__':
#     n, k = read_input()
#     print(fibonacci_recursive_mod(n) % (10 ** k))
