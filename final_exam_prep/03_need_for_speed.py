count = int(input())

cars_dict = {}
for _ in range(count):
    car, mileage, fuel = input().split('|')
    cars_dict[car] = {}
    cars_dict[car]['mileage'] =int(mileage)
    cars_dict[car]['fuel'] = int(fuel)

commands = input()

while not commands == 'Stop':
    line = commands.split(' : ')
    command = line[0]
    if command == 'Drive':
        car = line[1]
        distance = int(line[2])
        fuel = int(line[3])
        if cars_dict[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['fuel'] -= fuel
            cars_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del cars_dict[car]
    elif command == 'Refuel':
        car = line[1]
        fuel = int(line[2])
        need_fuel = 75 - cars_dict[car]['fuel']
        if need_fuel <= fuel:
            cars_dict[car]['fuel'] += need_fuel
            print(f"{car} refueled with {need_fuel} liters")
        else:
            cars_dict[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        car = line[1]
        kilometers = int(line[2])
        cars_dict[car]['mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
        if cars_dict[car]['mileage'] < 10000:
            cars_dict[car]['mileage'] == 10000


    commands = input()

my_sort = sorted(cars_dict.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for k, v in my_sort:
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")

