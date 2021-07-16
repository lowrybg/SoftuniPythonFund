import numpy as np
num = input()
def unique(list1):
    x = np.array(list1)
    return np.unique(x)

num_int = int(num)
is_unique = False
my_list = []
while not is_unique:
    num_int += 1
    num_str = str(num_int)
    for n in range(0, len(num_str)):
        my_list.append(num_str[n])

    unique_elements = unique(my_list)
    if  len(unique_elements) == len(num):
        is_unique = True
    else:
        my_list = []
        continue

print(f''.join(map(str, my_list)))