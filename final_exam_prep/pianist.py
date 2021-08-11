num = int(input())


my_dict = {}
for _ in range(num):
    line = input().split('|')
    my_dict[line[0]] = {'composer': line[1], 'key': line[2]}

command_args = input().split('|')

while not len(command_args) == 1:


    if command_args[0] == 'Add':
        piece = command_args[1]
        composer = command_args[2]
        key = command_args[3]
        if piece in my_dict:
            print(f"{piece} is already in the collection!")
        else:
            my_dict[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command_args[0] == 'Remove':
        piece = command_args[1]
        if piece in my_dict:
            del my_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command_args[0] == 'ChangeKey':
        piece = command_args[1]
        new_key = command_args[2]
        if piece in my_dict:
            my_dict[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command_args = input().split('|')


my_dict = sorted(my_dict.items(), key=lambda x: (x[0], x[1]['composer']))
for k, v in my_dict:
    print(f"{k} -> Composer: {v['composer']}, Key: {v['key']}")