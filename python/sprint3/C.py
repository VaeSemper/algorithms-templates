def sequence(first, second):
    len_first, len_second = len(first), len(second)
    if len_first == 0:
        return True

    if len_first > len_second:
        return False

    idx_second = 0
    for idx_first in range(len_second):
        if first[idx_second] == second[idx_first]:
            idx_second += 1
            if idx_second == len_first:
                return True
    return False


if __name__ == '__main__':
    print(sequence(input(), input()))
