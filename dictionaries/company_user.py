my_dict = {}
data = input().split(' -> ')

while data[0] != 'End':
    company = data[0]
    user_id = data[1]
    if company not in my_dict:
        my_dict[company] = []
        if user_id not in my_dict[company]:
            my_dict[company].append(user_id)
    else:
        if user_id not in my_dict[company]:
            my_dict[company].append(user_id)

    data = input().split(' -> ')

sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])

for key, value in sorted_dict:
    print(key)
    for el in value:
        print(f'-- {el}')