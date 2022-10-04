# 71199755
from collections import namedtuple


def qs_parting(members, left, right):
    pivot = members[left]
    major_l = left + 1
    minor_r = right - 1
    while True:
        if major_l <= minor_r and members[major_l] < pivot:
            major_l += 1
        elif major_l <= minor_r and members[minor_r] > pivot:
            minor_r -= 1
        elif members[minor_r] > pivot or members[major_l] < pivot:
            continue
        if major_l <= minor_r:
            members[major_l], members[minor_r] = members[minor_r], members[
                major_l]
        else:
            members[left], members[minor_r] = members[minor_r], members[left]
            return minor_r


def quick_sort(members, left, right):
    if right - left > 1:
        part_result = qs_parting(members, left, right)
        quick_sort(members, left, part_result)
        quick_sort(members, part_result + 1, right)


def read_and_prepare_data():
    Member = namedtuple('Member', 'penalty tasks name')

    def create_member(member):
        typed_data = {
            'name': member[0],
            'penalty': -int(member[1]),
            'tasks': int(member[2]),
        }
        return Member(**typed_data)

    default_left = 0
    number_of_members = int(input())
    members = [
        create_member(input().split()) for _ in range(number_of_members)
    ]
    return default_left, number_of_members, members


if __name__ == '__main__':
    default_left, number_of_members, members = read_and_prepare_data()
    quick_sort(members, default_left, number_of_members)
    for member in members:
        print(member.name)
