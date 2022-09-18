# 70572804


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calc(operand_operations_list):
    operation = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y,
    }

    stack = Stack()

    for item in operand_operations_list:
        if item in operation:
            operation_result = operation[item](stack.pop(), stack.pop())
            stack.push(operation_result)
        else:
            stack.push(int(item))

    return stack.pop()


def read_input():
    operand_operations_list = input().split()
    return operand_operations_list


def main():
    operand_operations_list = read_input()
    print(calc(operand_operations_list))


if __name__ == '__main__':
    main()
