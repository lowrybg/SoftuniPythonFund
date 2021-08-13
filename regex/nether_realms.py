import re
# TODO 20%
data = input().split(', ')
pattern_alpha = r"[A-Za-z]"
pattern_digit = r"([\-?\d+\.?\d]+)"
health = 0
sum_digits = 0
signs = []
result = {}
for d in data:
    matched_alpha = re.findall(pattern_alpha,d)
    matched_digit = re.findall(pattern_digit, d)
    for m in matched_alpha:
        health += ord(m)
    for dig in matched_digit:
        sum_digits += float(dig)
    for r in d:
        if r == '*' or r == '/':
            signs.append(r)
    for s in signs:
        if s == '*':
            sum_digits = sum_digits * 2
        elif s == '/':
            sum_digits = sum_digits / 2


    result[d] = {'health':health, 'damage': sum_digits}
    health = 0
    sum_digits = 0
    signs = []
sort = sorted(result.items(), key=lambda x: x)
for k in sort:
    print(f"{k[0]} - {int(k[1]['health'])} health, {float(k[1]['damage']):.2f} damage")