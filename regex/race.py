import re

names = input().split(', ')

my_dict = {}
for name in names:
    my_dict[name] = 0

pattern_name = r"[A-Za-z]"
pattern_nums = r"[0-9]"
line = input()
while not line == 'end of race':
    match = re.finditer(pattern_name, line)
    found = [ch.group() for ch in match]
    found_name = ''
    for f in found:
        found_name += f
    if found_name in my_dict:
        match_nums = re.finditer(pattern_nums, line)
        found_nums = [int(ch.group()) for ch in match_nums]

        my_dict[found_name] += sum(found_nums)

    line = input()

my_dict = sorted(my_dict.items(), key=lambda x: -x[1])


print(f'1st place: {my_dict[0][0]}')
print(f'2nd place: {my_dict[1][0]}')
print(f'3rd place: {my_dict[2][0]}')