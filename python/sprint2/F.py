"""
Нужно реализовать класс StackMax, который поддерживает операцию
определения максимума среди всех элементов в стеке. Класс должен
поддерживать операции push(x), где x – целое число, pop() и get_max().
В первой строке записано одно число n — количество команд, которое не
превосходит 10000. В следующих n строках идут команды. Команды могут быть
следующих видов:
push(x) — добавить число x в стек; pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке; Если стек пуст,
при вызове команды get_max() нужно напечатать «None», для команды pop() —
«error».
"""


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except Exception:
            print('error')

    def get_max(self):
        try:
            return max(self.items)
        except Exception:
            return None


stack = StackMax()


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
