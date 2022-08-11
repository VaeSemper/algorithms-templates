from math import sqrt
from typing import List


# def factorize(number: int) -> List[int]:
#     while number > 1:
#         for i in range(2, number + 1):
#             if number % i == 0:
#                 number //= i
#                 yield i
#                 break



# def factorize(number: int) -> List[int]:
#     result = []
#     for i in range(2, number + 1):
#         while number % i == 0:
#             result.append(i)
#             # print(i, end=' ')
#             number //= i
#     return result


def factorize(number: int) -> List[int]:
    j = 2
    while number > 1:
        for i in range(j, int(sqrt(number+0.05)) + 1):
            if number % i == 0:
                number /= i
                j = i
                yield i
                break
        else:
            if number > 1:
                yield number
                break


if __name__ == '__main__':
    print(' '.join(map(str, factorize(int(input())))).rstrip('.0'))
