def flowers_sort(arr):
    arr.sort()
    results = []
    index = 0
    start, end = arr[index]
    index += 1
    while index < len(arr):
        if start <= arr[index][0] <= end:
            _, current_end = arr[index]
            index += 1
            if current_end > end:
                end = current_end
        else:
            results.append([start, end])
            start, end = arr[index]
            index += 1
    results.append([start, end])

    for res in results:
        print(*res)
    

def read_input():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(tuple(int(coord) for coord in input().split()))
    return n, arr


if __name__ == '__main__':
    n, arr = read_input()
    flowers_sort(arr)
