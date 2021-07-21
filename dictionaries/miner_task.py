line = input()

counter = 1
word = ''
my_dict = {}
while line != 'stop':

    if counter % 2 != 0:
        if line not in my_dict:
            my_dict[line] = line
            my_dict[line] = 0
        word = line
    else:
        line = int(line)
        my_dict[word] += line
        word = ''
    counter += 1
    line = input()

for key, value in my_dict.items():
    print(f'{key} -> {value}')