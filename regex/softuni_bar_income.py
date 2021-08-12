import re

pattern = r"%(?P<name>[A-Z][a-z]+)%<(?P<product>[A-Za-z]+)>[A-Za-z]*(\|)(?P<quantity>[0-9]+)(\|)[A-Za-z]*(?P<price>\d+(.\d+)?)\$"

line = input()

my_dict = {}

while not line == 'end of shift':
    match = re.finditer(pattern, line)
    match = [el.groupdict() for el in match]

    for k in match:
        my_dict[k['name']] = {'product': k['product'],'quantity': int(k['quantity']),'price': float(k['price']) }

    line = input()
total = 0
for p in my_dict.items():
    total += p[1]['price']*p[1]['quantity']
    print(f"{p[0]}: {p[1]['product']} - {p[1]['price']*p[1]['quantity']:.2f}")
print(f'Total income: {total:.2f}')
