names_list = input().split(', ')

lines = input(). split()
count_blacklisted = 0
count_lost =0
command = lines[0]
while command != 'Report':

    command = lines[0]

    if command == 'Blacklist':
        name = lines[1]
        if name in names_list:
            print(f'{name} was blacklisted.')
            names_list[name.index(name)] = 'Blacklisted'
            count_blacklisted +=1
        else:
            print(f'{name} was not found.')

    elif command == 'Error':
        error_index = int(lines[1])

        if 0<= error_index <= len(names_list) and names_list[error_index] != 'Blacklisted' and names_list[error_index] != 'Lost':
            print(f'{names_list[error_index]} was lost due to an error.')
            names_list[error_index] = 'Lost'
            count_lost +=1
        # else:
        #     lines = input().split()
        #     continue


    elif command == 'Change':
        index = int(lines[1])
        new_name = lines [2]
        if 0<= index < len(names_list):
            print(f'{names_list[index]} changed his username to {new_name}.')
            names_list[index] = new_name
        # else:
        #     lines = input().split()
        #     continue




    lines = input().split()
    command = lines[0]


print(f'Blacklisted names: {count_blacklisted}')
print(f'Lost names: {count_lost}')
print(' '.join(map(str, names_list)))