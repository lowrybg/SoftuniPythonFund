first_char = input()
second_char = input()


def char_range(first, second):
    result = []
    for n in range(ord(first_char)+1, ord(second_char)):
        result.append(chr(n))
    return result


print(*char_range(first_char,second_char))