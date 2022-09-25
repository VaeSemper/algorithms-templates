def gen_button(digits):
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def button(digits, path, result):
        if digits == '':
            result.append(path)
            return
        for letter in letters[digits[0]]:
            path += letter
            button(digits[1:], path, result)
            path = path[:-1]

    result = []
    button(digits, '', result)
    for x in result:
        print(x, end=' ')


if __name__ == '__main__':
    digits = input()
    gen_button(digits)
