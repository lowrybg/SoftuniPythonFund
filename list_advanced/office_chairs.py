rooms_number = int(input())

counter = 0
boolean = True
for n in range(1, rooms_number+1):
    line = input().split()
    chairs = line[0]
    people = int(line[1])

    if len(chairs) < people:
        print(f'{people - len(chairs)} more chairs needed in room {n}')
        boolean = False

    else:
        counter += (len(chairs)-people)

if boolean:
    print(f'Game On, {counter} free chairs left')