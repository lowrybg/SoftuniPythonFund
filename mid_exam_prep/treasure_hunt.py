loot = input().split('|')

commands = input()


def if_index_valid (collection, index):

    if 0 <= index < len(collection):

        return  True
    return False


while commands != 'Yohoho!':

    command_split = commands.split()
    command = command_split [0]

    if command == 'Loot':
        for el in command_split[1:len(command_split)]:
            if el not in loot:
                loot.insert(0,el)

    elif command == 'Drop':
        index = int(command_split[1])
        if if_index_valid(loot, index):

            loot.remove(index)



    elif command == 'Steal':
        pass




    commands = input()