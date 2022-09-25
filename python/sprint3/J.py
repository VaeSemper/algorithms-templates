def bubble_sorting(arr_len, arr):
    flag, alrdy_sort = True, True
    while flag:
        flag = False
        for index in range(arr_len - 1):
            element = arr[index]
            next_el = arr[index + 1]
            if element > next_el:
                arr[index], arr[index + 1] = next_el, element
                flag = True
                alrdy_sort = False
        if flag or alrdy_sort:
            print(*arr)
    return arr


def read_input():
    arr_len = int(input())
    arr = [int(i) for i in input().split()]
    return arr_len, arr


if __name__ == '__main__':
    arr_len, arr = read_input()
    bubble_sorting(arr_len, arr)
