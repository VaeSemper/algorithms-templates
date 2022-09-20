# 70681534


class FullDeckError(Exception):
    pass


class Deck:
    def __init__(self, deck_max_size):
        self.__deck = [None] * deck_max_size
        self.__head = 0
        self.__tail = 0
        self.__deck_size = 0
        self.__max_size = deck_max_size

    def is_empty(self):
        return self.__deck_size == 0

    def push_back(self, value):
        if self.__deck_size == self.__max_size:
            raise FullDeckError()
        self.__deck[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__deck_size += 1

    def push_front(self, value):
        if self.__deck_size == self.__max_size:
            raise FullDeckError()
        self.__deck[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_size
        self.__deck_size += 1

    def pop_front(self, *args):
        if self.is_empty():
            raise FullDeckError()
        value, self.__deck[self.__head] = self.__deck[self.__head], None
        self.__head = (self.__head + 1) % self.__max_size
        self.__deck_size -= 1
        return value

    def pop_back(self, *args):
        if self.is_empty():
            raise FullDeckError()
        value, self.__deck[self.__tail - 1] = self.__deck[self.__tail - 1], None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__deck_size -= 1
        return value


def read_input():
    read_command_cnt = int(input())
    read_size = int(input())
    return read_command_cnt, read_size


def main():
    command_cnt, deck_size = read_input()
    deck = Deck(deck_size)
    for i in range(command_cnt):
        command = input().split()
        try:
            result = getattr(deck, command[0])(command[-1])
            if result:
                print(result)
        except FullDeckError:
            print('error')


if __name__ == '__main__':
    main()
