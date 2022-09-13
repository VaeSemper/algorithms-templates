"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:
get() — вывести элемент, находящийся в голове очереди, и удалить его. Если
очередь пуста, то вывести «error»
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди.
"""


class QueueNode:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def put(self, x):
        if self.q_size == 0:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.q_size += 1

    def get(self):
        if self.is_empty():
            return 'error'
        if self.q_size == 1:
            x = self.head
            self.head = self.Node()
            self.tail = self.Node()
            self.q_size -= 1
            return x
        if self.q_size == 2:
            x = self.head
            self.head = self.tail
            self.q_size -= 1
            return x
        x = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.q_size -= 1
        return x

    def size(self):
        return self.q_size


# class QueueNode:
#     def __init__(self):
#         self.queue = [None]
#         self.head = 0
#         self.tail = 0
#         self.q_size = 0
#
#     def is_empty(self):
#         return self.q_size == 0
#
#     def put(self, x):
#         self.queue[self.tail] = x
#         self.queue.append(None)
#         self.tail += 1
#         self.q_size += 1
#
#     def get(self):
#         if self.is_empty():
#             return 'error'
#         x = self.queue[self.head]
#         self.queue[self.head] = None
#         self.head += 1
#         self.q_size -= 1
#         return x
#
#     def size(self):
#         return self.q_size


def read_input():
    command_cnt = int(input())
    q = QueueNode()
    for _ in range(command_cnt):
        command = input()
        if command.startswith('put'):
            q.put(command.split()[1])
        elif command == 'get':
            print(q.get())
        elif command == 'size':
            print(q.size())


if __name__ == '__main__':
    read_input()
