commands = input().split()

command = commands[0]

message = []
while command != 'end':
    command = commands[0]

    if command == 'Chat':
       message.append(commands[1])

    elif command == 'Delete':
        delete_message = commands[1]

        if delete_message in message:
            message.remove(delete_message)
        else:
            commands = input().split()
            continue

    elif command == 'Edit':
        edit_message = commands[1]
        edited_message = commands[2]
        # message = [message[edit_message] ==edited_message for n in message if edit_message in message]
        if edit_message in message:
            index = message.index(edit_message)
            message[index] = edited_message
        else:
            commands = input().split()
            continue


    elif command == 'Pin':
        pinned_message = commands[1]
        # if pinned_message in message:
        #     message.remove(pinned_message)
        #     message.append(pinned_message)
        if pinned_message in message:
            index = message.index(edit_message)
            message[index] .remove(pinned_message)
            message.append(pinned_message)
        else:
            commands = input().split()
            continue



    elif command == 'Spam':
        spam_message = commands[1:]
        message.append(spam_message)


    commands = input().split()
    command = commands[0]

for n in message:
    print(' '.join(map(str, n)))
