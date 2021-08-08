num = int(input())

heroes_dict = {}
for n in range(num):
    heroes = input().split()
    hero = heroes[0]
    hp = int(heroes[1])
    mp = int(heroes[2])
    heroes_dict[hero] = {}
    heroes_dict[hero]['hp'] = hp
    heroes_dict[hero]['mp'] = mp

lines = input()

while not lines == 'End':
    split_commands = lines.split(' - ')
    command = split_commands[0]

    if command == 'CastSpell':
        hero_name = split_commands[1]
        mp_needed = int(split_commands[2])
        spell_name = split_commands[3]
        if heroes_dict[hero_name]['mp'] >= mp_needed:
            heroes_dict[hero_name]['mp'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == 'TakeDamage':
        hero_name = split_commands[1]
        damage = int(split_commands[2])
        attacker = split_commands[3]
        heroes_dict[hero_name]['hp'] -= damage
        if heroes_dict[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes_dict[hero_name]
    elif command == 'Recharge':
        hero_name = split_commands[1]
        amount = int(split_commands[2])

        n_a = 200 - heroes_dict[hero_name]['mp']
        if n_a >= amount:
            heroes_dict[hero_name]['mp'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            heroes_dict[hero_name]['mp'] += n_a
            print(f"{hero_name} recharged for {n_a} MP!")

    elif command == 'Heal':
        hero_name = split_commands[1]
        amount = int(split_commands[2])
        needed_amount = 100 - heroes_dict[hero_name]['hp']
        if needed_amount >= amount:
            heroes_dict[hero_name]['hp'] += amount
            print(f"{hero_name} healed for {amount} HP!")
        else:
            heroes_dict[hero_name]['hp'] += needed_amount
            print(f"{hero_name} healed for {needed_amount} HP!")

    lines = input()

my_sort = sorted(heroes_dict.items(), key=lambda x: (-x[1]['hp'], x[0]))

for k, v in my_sort:
    print(f'{k}')
    print(f'HP: {v["hp"]}')
    print(f'MP: {v["mp"]}')