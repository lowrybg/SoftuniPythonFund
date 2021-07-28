line = input(). split(' : ')

my_dict = {}

while len(line) > 1:
    course = line[0]
    name = line[1]

    if course not in my_dict:
        my_dict[course] = []
        my_dict[course].append(name)

    else:
        my_dict[course]. append(name)


    line = input().split(' : ')

order = sorted(my_dict.items(), key=lambda x: (len(x[1])), reverse=True)
max_value = sorted(order, key=lambda x: (x[1]), reverse=False)
for key, value in order:
    print(f'{key}: {len(value)}')
    value = sorted(value, reverse=False)
    for n in value:
       print(f'-- {n}')