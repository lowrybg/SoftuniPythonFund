name = input()

line = input()

while not line == 'Sign up':
    command_args = line.split()
    command = command_args[0]
    if command == 'Case':
        if command_args[1] == 'lower':
            name = name.lower()
        elif command_args[1] == 'upper':
            name = name.upper()
        print(name)
    elif command == 'Reverse':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if start_index < len(name) and end_index <= len(name):
            sub = name[start_index:end_index+1]
            reversed_sub = sub[::-1]
            print(reversed_sub)
            # name = name[:start_index] + reversed_sub + name[end_index+1:]
    elif command == 'Cut':
        substr_to_cut = command_args[1]
        if substr_to_cut in name:
            temp_name = name.replace(substr_to_cut,'')
            print(temp_name)
        else:
            print(f"The word {name} doesn't contain {temp_name}.")

    elif command == 'Replace':
        char_to_replace = command_args[1]
        if char_to_replace in name:
            name = name.replace(char_to_replace, '*')
            print(name)

    elif command == 'Check':
        ch_to_check = command_args[1]
        if ch_to_check in name:
            print('Valid')
        else:
            print(f"Your username must contain {ch_to_check}.")

    line = input()