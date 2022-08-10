"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех
его соседей. Соседним считается элемент, находящийся от текущего на одну
ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не
считаются.
"""


from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    if row >= 1:
        result.append(matrix[row - 1][col])
    if row < len(matrix) - 1:
        result.append(matrix[row + 1][col])
    if col >= 1:
        result.append(matrix[row][col - 1])
    if col < len(matrix[row]) - 1:
        result.append(matrix[row][col + 1])
    return sorted(result)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()

if __name__ == '__main__':
    print(' '.join(map(str, get_neighbours(matrix, row, col))))
