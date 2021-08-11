message = input()

line = input()

while not line == 'Decode':
    command_args = line.split('|')

    if command_args[0] == 'Move':
        num_letters_to_move = int(command_args[1])
        message = message[num_letters_to_move:] + message[:num_letters_to_move]
    elif command_args[0] == 'Insert':
        index = int(command_args[1])
        value = command_args[2]
        message = message[:index] + value + message[index:]

    elif command_args[0] == 'ChangeAll':
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)

    line = input()
print(f'The decrypted message is: {message}')


