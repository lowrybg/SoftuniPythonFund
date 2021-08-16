import re
import math
num = int(input())
pattern = r"^(\$|%)(?P<word>[A-Z][a-z]{2,})\1:\s(?P<ords>\[\d+\]\|\[\d+\]\|\[\d+\]\|)$"


for n in range(num):
    line = input()
    match = re.finditer(pattern, line)
    match = [el.groupdict() for el in match]
    # print(match)
    # print(match[0]['word'])
    # print(match[0]['ords'])
    if match:
        print(f'{match[0]["word"]}: ', end='')
        word = []
        temp = ''
        for el in match[0]['ords']:

            if el.isdigit():
                temp += el
            else:
                if temp:
                    word.append(chr(int(temp)))
                temp = ''
        print("".join(word))

    else:
        print('Valid message not found!')

