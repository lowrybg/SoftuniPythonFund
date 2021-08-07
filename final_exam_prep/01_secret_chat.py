message = input()

commands = input()
while not commands == 'Reveal':
    line = commands.split(':|:')
    command = line[0]

    if command == 'InsertSpace':
        index = int(line[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif command == 'Reverse':
        substring = line[1]
        if substring in message:
            index_sub = message.find(substring)
            end_index = index_sub+len(substring)
            message = message[:index_sub] + message[end_index:] + substring[::-1]
            print(message)

        else:
            print('error')
    elif command == 'ChangeAll':
        substring = line[1]
        replacement = line[2]
        message = message.replace(substring, replacement)
        print(message)


    commands = input()

print(f'You have a new text message: {message}')