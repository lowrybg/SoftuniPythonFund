n = int(input())

my_dict = {}
for lines in range(n):
    line = input().split()
    command = line[0]
    name = line[1]


    if command == 'register':
        if name in my_dict:
            print(f'ERROR: already registered with plate number {my_dict.get(name)}')
        else:
            my_dict[name] = line[2]
            print(f'{name} registered {line[2]} successfully')

    elif command == 'unregister':
        if name not in my_dict:
            print(f'ERROR: user {name} not found')
        else:
            my_dict.pop(name, None)
            print(f'{name} unregistered successfully')

for key, value in my_dict.items():
    print(f'{key} => {value}')