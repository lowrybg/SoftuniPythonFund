orders_num = int(input())

total = 0
for n in range(orders_num):
    price_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price = price_capsule * days * capsule_count
    total += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total:.2f}')