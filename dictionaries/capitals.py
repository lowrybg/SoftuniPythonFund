line = input().split(', ')

my_dict = {}
counter = 1
country = []
while counter <= 2:
    for n in range(len(line)):

        if counter ==1:
            country.append(line[n])

        else:
            my_dict[country[n]] = line[n]
    counter+=1
    if counter >2:
        break
    line = input(). split(', ')

for key, value in my_dict.items():
    print(f'{key} -> {value}')