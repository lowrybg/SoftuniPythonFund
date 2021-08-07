raw = input()

line = input()

while not line == 'Done':
    commands = line.split()
    command = commands[0]
    if command == 'TakeOdd':
        raw = ("".join([str(raw[i]) for i in range(len(raw)) if i % 2 == 1]))
        print(raw)
    elif command == 'Cut':
        index = int(commands[1])
        length = int(commands[2])
        raw = raw[:index] + raw[index + length:]
        print(raw)
    elif command == 'Substitute':
        substring = commands[1]
        substitute = commands[2]
        if substring in raw:
            raw = raw.replace(substring, substitute)
            print(raw)
        else:
            print("Nothing to replace!")

    line = input()
print(f"Your password is: {raw}")