data = input().split(", ")


def is_palindrome(data):
    if data[:] == data[::-1]:
        return True
    return False


for n in range(len(data)):
    print(is_palindrome(data[n]))