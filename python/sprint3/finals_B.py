# 71080727


def qs_parting(member, left, right):
    pivot = (member[left])
    major_l = left + 1
    minor_r = right - 1
    while True:
        if major_l <= minor_r and member[major_l] < pivot:
            major_l += 1
        elif major_l <= minor_r and member[minor_r] > pivot:
            minor_r -= 1
        elif member[minor_r] > pivot or member[major_l] < pivot:
            continue
        if major_l <= minor_r:
            member[major_l], member[minor_r] = member[minor_r], member[major_l]
        else:
            member[left], member[minor_r] = member[minor_r], member[left]
            return minor_r


def quick_sort(member, left, right):
    if (right - left) > 1:
        part_result = qs_parting(member, left, right)
        quick_sort(member, left, part_result)
        quick_sort(member, part_result + 1, right)


def read_input():
    def typing_member(member):
        member[1] = -int(member[1])
        member[2] = int(member[2])
        return [member[1], member[2], member[0]]
    count = int(input())
    member = [typing_member(input().split()) for _ in range(count)]
    return count, member


if __name__ == '__main__':
    default_left = 0
    count, member = read_input()
    quick_sort(member, default_left, len(member))
    result = list(zip(*member))[2]
    print(*result, sep='\n')
