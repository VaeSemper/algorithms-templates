# 70459088


class Deck:
    def __init__(self, deck_max_size):
        self.deck = [None] * deck_max_size
        self.head = 0
        self.tail = 0
        self.deck_size = 0
        self.max_size = deck_max_size

    def is_empty(self):
        return self.deck_size == 0

    def push_back(self, value):
        if self.deck_size != self.max_size:
            self.deck[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.deck_size += 1
        else:
            print('error')

    def push_front(self, value):
        if self.deck_size != self.max_size:
            self.deck[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.deck_size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        value, self.deck[self.head] = self.deck[self.head], None
        self.head = (self.head + 1) % self.max_size
        self.deck_size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            return 'error'
        value, self.deck[self.tail - 1] = self.deck[self.tail - 1], None
        self.tail = (self.tail - 1) % self.max_size
        self.deck_size -= 1
        return value


def read_input():
    read_command_cnt = int(input())
    read_size = int(input())
    return read_command_cnt, read_size


def main():
    command_cnt, deck_size = read_input()
    deck = Deck(deck_size)
    for i in range(command_cnt):
        command = input()
        if command.startswith('push_back'):
            deck.push_back(command.split()[1])
        elif command.startswith('push_front'):
            deck.push_front(command.split()[1])
        elif command == 'pop_back':
            print(deck.pop_back())
        elif command == 'pop_front':
            print(deck.pop_front())


if __name__ == '__main__':
    main()
