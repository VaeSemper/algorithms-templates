def gen_bracket(left_bracket, right_bracket, prefix=''):
    if left_bracket == right_bracket == 0:
        print(prefix)
    else:
        if left_bracket > 0:
            gen_bracket(left_bracket - 1, right_bracket, prefix + '(')
        if left_bracket < right_bracket:
            gen_bracket(left_bracket, right_bracket - 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    left_bracket, right_bracket = n, n
    gen_bracket(left_bracket, right_bracket)
