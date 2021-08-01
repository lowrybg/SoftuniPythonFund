import re


def multiply_list(my_list):
    # Multiply elements one by one
    result = 1
    for x in my_list:
        result = result * x
    return result


# Multiplies every char of elements in list according to ASCI table
def asci_sum(my_list, thresh):
    result = 0
    coolest = []
    for el in my_list:
        for n in range(2, len(el)-2):
            result += ord(el[n])
        if result >= thresh:
            coolest.append(el)
        result = 0
    return coolest


pattern_words = r"(?P<first>\*{2}|\:{2})[A-Z][a-z]{2,}(?P=first)"
pattern_digits = r'\d'

data = input()

digits = re.findall(pattern_digits, data)
digits = [int(n) for n in digits]
threshold = multiply_list(digits)

words = re.finditer(pattern_words,data)
words = [el.group() for el in words]

print(f'Cool threshold: {threshold}')
print(f'{len(words)} emojis found in the text. The cool ones are:')
print(*asci_sum(words,threshold), sep='\n')
