first = int(input())
second = int(input())
third = int(input())


def sum_numbers(n_1, n_2):
    return n_1 + n_2


def subtract(first, second):
    return first - second


def sum_and_subtract(one, two, three):
    result = subtract(sum_numbers(one, two),three)
    return  result

print(sum_and_subtract(first, second, third))

