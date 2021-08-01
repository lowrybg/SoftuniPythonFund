import re
# TODO Working on 80%
number = int(input())


pattern_valid = r'(@(#)+)+(?P<important>[A-Z][A-Za-z0-9]{4,}[A-Z])\1'


for _ in range(number):
    lines = input()
    valid = re.search(pattern_valid,lines)

    if valid:
        valid = valid.group()
        valid = str(valid)
        product_group = ''
        for n in range(len(valid)):
            if valid[n].isdigit():
                product_group += valid[n]
        if product_group != '':
            print(f'Product group: {product_group}')
        else:
            print(f'Product group: 00')
        product_group = ''
    else:
        print(f'Invalid barcode')

