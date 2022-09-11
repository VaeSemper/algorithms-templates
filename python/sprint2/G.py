"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1). Для
пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.
В первой строке записано одно число — количество команд, оно не
превосходит 100000. Далее идут команды по одной в строке. Команды могут быть
следующих видов:
push(x) — добавить число x в стек; pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке; Если стек пуст,
при вызове команды get_max нужно напечатать «None», для команды pop —
«error».
"""


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.is_empty():
            self.max.append(item)
        elif item > self.max[len(self.items) - 1]:
            self.max.append(item)
        else:
            self.max.append(self.max[len(self.items) - 1])
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('error')
            return
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.is_empty():
            return None
        return self.max[-1]


stack = StackMaxEffective()


def input_data():
    n = int(input())
    for command in range(n):
        command = input().split()
        if command[0] == 'get_max':
            print(stack.get_max())
        elif command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            stack.pop()


if __name__ == '__main__':
    input_data()
