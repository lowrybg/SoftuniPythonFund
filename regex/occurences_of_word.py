import re
text = input().lower()

word = input().lower()

pattern = rf'{word}\b'
my_list =[]
my_list.extend([el for el in re.findall(pattern,text)])

print(len(my_list))
