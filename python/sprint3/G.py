def sort_by_color(arr):
    count = 3
    ext_arr = [0] * count
    for color in arr:
        ext_arr[color] += 1
    # index = 0
    # for value in range(count):
    #     for _ in range(ext_arr[value]):
    #         arr[index] = value
    #         index += 1
    arr = []
    for i in range(count):
        arr += [i] * ext_arr[i]
    return arr


def read_input():
    _ = int(input())
    arr = [int(i) for i in input().split()]
    return arr


if __name__ == '__main__':
    arr = read_input()
    print(*sort_by_color(arr))
