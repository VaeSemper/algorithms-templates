from typing import List, Tuple


def zipper(a: List[int], b: List[int], n) -> List[int]:
    result_list = []
    for i in range(n):
        result_list += a[i], b[i]
    return result_list


def read_input() -> Tuple[int, List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return n, a, b


n, a, b = read_input()
print(' '.join(map(str, zipper(a, b, n))))
