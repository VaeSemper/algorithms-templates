"""
Астрологи объявили день очередей ограниченного размера. Тимофею нужно
написать класс MyQueueSized, который принимает параметр max_size, означающий
максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит
5000.

Далее идут команды по одной на строке. Команды могут быть следующих видов:
push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове
операций pop() или peek() для пустой очереди нужно вывести «None».
"""


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.q_size = 0
        self.max_n = max_size

    def is_empty(self):
        return self.q_size == 0

    def push(self, x):
        if self.q_size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.q_size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.q_size -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.q_size


def read_input():
    command_cnt = int(input())
    q = MyQueueSized(int(input()))
    for _ in range(command_cnt):
        command = input()
        if command.startswith('push'):
            q.push(command.split()[1])
        elif command == 'peek':
            print(q.peek())
        elif command == 'pop':
            print(q.pop())
        elif command == 'size':
            print(q.size())


if __name__ == '__main__':
    read_input()
