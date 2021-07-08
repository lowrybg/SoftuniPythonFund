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

            element = loot.pop(index)
            loot.append(element)



    elif command == 'Steal':
        count = int(command_split[1])

        length = len(loot) -count
        if len(loot) >= count:
            stealed = loot[length:]
        print(*stealed, sep=', ')




    commands = input()

sum = 0
for el in loot[:length]:
    sum += len(el)
if length > 0:
    print(f'Average treasure gain: {sum/length:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')