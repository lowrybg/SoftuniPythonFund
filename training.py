names_list = input().split(', ')

lines = input(). split()

while lines != 'Report':

    command = lines[0]

    if command == 'Blacklist':
        name = lines[1]
        if name in names_list:
            print(f'{name} was blacklisted.')
            names_list[name.index(name)] = 'Blacklisted'
        else:
            print(f'{name} was not found.')

    elif command == 'Error':
        error_index = int(lines[1])

        if 0<=error_index <len(names_list) and names_list[error_index] != 'Blacklisted' and names_list[error_index] != 'Lost':
           print(f'{names_list[error_index]} was lost due to an error.')
           names_list[error_index] = 'Lost'
        else:
            continue

    elif command == 'Change':
           pass