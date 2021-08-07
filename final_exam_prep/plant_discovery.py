num = int(input())

plants_dict = {}
for _ in range(num):
    plants_data = input().split('<->')
    plant_name = plants_data[0]
    plant_rarity = plants_data[1]
    plants_dict[plant_name] = {}
    plants_dict[plant_name]['rarity'] = plant_rarity
    plants_dict[plant_name]['rating'] = []

commands = input().split(':')
command = commands[0]

while commands != 'Exhibition':
    actions = commands[1].split(' - ')
    try:
        if command == 'Rate':
            plant = actions[0].strip()
            rating = int(actions[1])
            # if plant in plants_dict:
            plants_dict[plant]['rating'].append(rating)

        elif command == 'Update':
            plant = actions[0].strip()
            rarity = actions[1]
            # if plant in plants_dict:
            plants_dict[plant]['rarity'] = rarity

        elif command == 'Reset':
            plant = actions[0].strip()

            # if plant in plants_dict:
            plants_dict[plant]['rating'] = []
        else:
            print('error')
    except:
        print('error')
    commands = input().split(':')
    command = commands[0]
    if command == "Exhibition":
        break



for plant_name, value in plants_dict.items():
    if value['rating']:
        # my_sum = [ sum(el) for el in value['rating']]
        avg = sum(value['rating']) / len(value['rating'])
    else:
        avg = 0
    plants_dict[plant_name]['avg'] = avg
my_sort = sorted(plants_dict.items(),  key=lambda tkvp: (tkvp[1]['rarity'], tkvp[1]['avg']), reverse=True)

print('Plants for the exhibition:')
for k, v in my_sort:
    print(f'- {k}; Rarity: {v["rarity"]}; Rating: {v["avg"]:.2f}')