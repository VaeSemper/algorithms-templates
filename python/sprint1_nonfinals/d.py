"""
Метеорологическая служба вашего города решила исследовать погоду новым
способом.

Под температурой воздуха в конкретный день будем понимать максимальную
температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые
температура строго больше, чем в день до (если такой существует) и в день
после текущего (если такой существует). Например, если за 5 дней
максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные
условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот
период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.
"""


from typing import List, Tuple


def get_weather_randomness(temperatures: List[int], n: int) -> int:
    result = 0
    # passed = set()
    if n == 1:
        return 1
    if temperatures[0] > temperatures[1]:
        result += 1
    if temperatures[n - 1] > temperatures[n - 2]:
        result += 1
    for day in range(1, n - 1):
        # if day not in passed:
        #     if temperatures[day - 1] < temperatures[day] > temperatures[day + 1]:
        #         result += 1
        #         passed.add(day + 1)
        if temperatures[day - 1] < temperatures[day] > temperatures[day + 1]:
            result += 1
    return result


# def get_weather_randomness(temperatures: List[int], n: int) -> int:
#     result = [0] * n
#     if n == 1:
#         return 1
#     if temperatures[0] > temperatures[1]:
#         result[0] = 1
#     if temperatures[n - 1] > temperatures[n - 2]:
#         result[n - 1] = 1
#     for day in range(1, n - 1):
#         # if result[day - 1]:
#         #     continue
#         if temperatures[day - 1] < temperatures[day] > temperatures[day + 1]:
#             result[day] = 1
#     return sum(result)


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures, n


temperatures, n = read_input()

if __name__ == '__main__':
    print(get_weather_randomness(temperatures, n))
