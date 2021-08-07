key = input()

line = input()

while not line == 'Generate':
    commands = line.split('>>>')
    command = commands[0]

    if command == 'Contains':
        substring = commands[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        up_or_lo = commands[1].lower()
        start_index = int(commands[2])
        end_index = int(commands[3])
        substr = key[start_index:end_index]
        if up_or_lo == 'lower':
            substr = substr.lower()
        else:
            substr = substr.upper()
        key = key[:start_index] + substr + key[end_index:]
        print(key)

    elif command == 'Slice':
        start_index = int(commands[1])
        end_index = int(commands[2])
        key = key[:start_index] + key[end_index:]
        print(key)



    line = input()
print(f"Your activation key is: {key}")