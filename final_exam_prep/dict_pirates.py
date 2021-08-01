data = input()

dict_of_towns = {}
while data != 'Sail':
    city, population, gold = data.split("||")

    if city not in dict_of_towns:
        dict_of_towns[city] = {}
        dict_of_towns[city]['population'] = int(population)
        dict_of_towns[city]['gold'] = int(gold)
    else:
        dict_of_towns[city]['population'] += int(population)
        dict_of_towns[city]['gold'] += int(gold)

    data = input()

commands = input()
while commands != 'End':
    command = commands.split('=>')
    if command[0] == 'Plunder':
        city = command[1]
        people = int(command[2])
        stolen_gold = int(command[3])
        dict_of_towns[city]['population'] -= people
        dict_of_towns[city]['gold'] -= stolen_gold
        print(f'{city} plundered! {stolen_gold} gold stolen, {people} citizens killed.')
        if dict_of_towns[city]['population'] == 0 or dict_of_towns[city]['gold'] == 0:
            print(f'{city} has been wiped off the map!')
            del dict_of_towns[f'{city}']

    elif command[0] == 'Prosper':
        town = command[1]
        gold_to_add = int(command[2])

        if gold_to_add < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            dict_of_towns[town]['gold'] += gold_to_add
            print(f'{gold_to_add} gold added to the city treasury. {town} now has {dict_of_towns[town]["gold"]} gold.')
    commands = input()

dict_of_towns = sorted(dict_of_towns.items(), key=lambda tkvp: (-tkvp[1]["gold"], tkvp[0]))
if dict_of_towns:
    print(f'Ahoy, Captain! There are {len(dict_of_towns)} wealthy settlements to go to:')

    for key, value in dict_of_towns:
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')