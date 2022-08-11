from typing import List, Tuple


def get_sum(number_list: List[int], k: List[int]) -> List[int]:
    max_len = len(number_list)
    next_bit = 0
    result = []
    for index in reversed(range(max_len)):
        sum_number = number_list[index] + k[index] + next_bit
        if sum_number >= 10:
            next_bit = 1
            result.append(int(str(sum_number)[-1]))
        else:
            result.append(sum_number)
            next_bit = 0
    if next_bit:
        result += [1]
    return result[::-1]


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = input()
    len_k = len(k)
    if n < len_k:
        number_list = [0] * (len_k - n) + number_list
    k = list(map(int, k.zfill(len(number_list))))
    return number_list, k


if __name__ == '__main__':
    number_list, k = read_input()
    print(' '.join(map(str, get_sum(number_list, k))))
