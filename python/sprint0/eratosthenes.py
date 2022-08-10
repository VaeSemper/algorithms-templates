"""
Решето Эратосфена. Находит все простые числа, не превосходящие n.
O(n*log(log(n)))

1. Выписываем все целые числа от 0 до n. Сразу помечаем, что числа 0 и 1 не
являются простыми (записываем на соответствующих этим числам позициях False).
2. Заводим переменную num, равную первому не рассмотренному простому числу.
Изначально она равна 2.
3. Помечаем в списке числа от 2 * num до n с шагом, равным num, составными.
Например, для 2 пометим значением False чётные числа — 4, 6, 8 и так далее.
4. Теперь в num присваиваем следующее простое число, то есть не
рассмотренное число в списке. Для этого достаточно увеличивать num с шагом 1,
пропуская числа, отмеченные как составные. На первом найденном простом числе
следует остановиться.
5. Повторяем два предыдущих шага, пока это возможно.
"""


import time


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


start_time = time.time()
# print(*eratosthenes(1000000))
eratosthenes(1000000)
print("--- %s seconds, eratosthenes ---" % (time.time() - start_time))

"""
Линейное решето.
O(n)

1. Для каждого числа i будем хранить lp[i] — минимальный простой делитель 
числа i. Заведём массив lp длины n + 1. А также массив primes, в который 
будем добавлять найденные простые числа.
2. Перебираем i по возрастанию.
3. Если lp[i] = 0, можно сделать вывод, что число i простое, и добавить его в 
массив primes.
4. Рассматриваем все простые числа p, которые не больше lp[i]. 
Обновляем lp[p * i] = p.
"""


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


start_time = time.time()
# print(*get_least_primes_linear(1000000))
get_least_primes_linear(1000000)
print("--- %s seconds, primes_linear ---" % (time.time() - start_time))


"""Не столь быстрый алгоритм нахождения всех простых чисел."""


def is_prime(n):
    if n == 1:
        return False
    i = 2
    # while i < n:  # brrr O(n)
    while i * i < n:    # O(sqrt(n))
        if n % i == 0:
            return False
        i = i + 1
    return True


def get_smaller_primes(n):
    smaller_primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            smaller_primes.append(num)
    return smaller_primes


start_time = time.time()
# print(*get_smaller_primes(100000))
get_smaller_primes(1000000)
print("--- %s seconds, O(n) algorithm ---" % (time.time() - start_time))
