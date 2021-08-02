import re

number = int(input())


pattern_valid = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"


for _ in range(number):
    lines = input()

    if re.match(pattern_valid,lines):

        digits = re.findall(r"\d", lines)

        if digits:
            print(f'Product group: {"".join(digits)}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
