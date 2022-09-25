def binary_search(arr, x, left, right):
    if right <= left != 0:
        return -1
    mid = (left + right) // 2
    # if arr[mid] == x:
    if arr[mid] >= x > arr[mid - 1] or mid == 0:
        return mid + 1
    elif x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def read_input():
    days = int(input())
    arr = [int(item) for item in input().split()]
    x = int(input())
    return days, arr, x


if __name__ == '__main__':
    days, arr, x = read_input()
    index1 = binary_search(arr, x, left=0, right=days)
    index2 = binary_search(arr, x * 2, left=0, right=days)
    print(index1, index2)
