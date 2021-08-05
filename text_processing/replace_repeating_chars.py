line = input()
line = line + 'T'
my_list = []

for n in range(len(line) - 1):

    if line[n + 1] == line[n]:
        n += 1
        continue
    else:
        my_list.append(line[n])
print("".join(my_list))