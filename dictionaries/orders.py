line = input().split()

my_dict = {}
while len(line) > 1:

    product = line[0]
    price = float(line[1])
    quantity = int(line[2])
    if product not in my_dict:
        my_dict[product] = {'price': price, 'quantity': quantity}
    else:
        my_dict[product]['price'] = price
        my_dict[product]['quantity'] += quantity
    line = input().split()


for key, value in my_dict.items():
    print(f'{key} -> {my_dict[key]["price"]*my_dict[key]["quantity"]:.2f}')