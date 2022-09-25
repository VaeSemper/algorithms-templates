def comparator(num1, num2):
    if len(num1) == len(num2):
        return num1 < num2
    return num1 + num2 < num2 + num1


def func(cnt, numbers):
    flag = True
    while flag:
        flag = False
        for index in range(cnt - 1):
            number = numbers[index]
            number_next = numbers[index + 1]
            if comparator(number, number_next):
                numbers[index], numbers[index + 1] = number_next, number
                flag = True
    return ''.join(numbers)


def read_input():
    cnt = int(input())
    numbers = input().split()
    return cnt, numbers


if __name__ == '__main__':
    cnt, numbers = read_input()
    print(func(cnt, numbers))
