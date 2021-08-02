data = input().split()


a_list = []
b_list = []
a_list.extend(range(1,12))
b_list.extend(range(1,12))

for n in range(len(data)):
    splitted = data[n].split('-')

    if splitted[0] == 'A':
        if int(splitted[1]) in a_list:
            a_list.remove(int(splitted[1]))
    elif splitted[0] == 'B':
        if int(splitted[1]) in b_list:
            b_list.remove(int(splitted[1]))
    if len(a_list)<7 or len(b_list)<7:
        print(f'Team A - {len(a_list)}; Team B - {len(b_list)}')
        print('Game was terminated')
        exit(0)
print(f'Team A - {len(a_list)}; Team B - {len(b_list)}')