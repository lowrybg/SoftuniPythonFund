# String explosion
string = input()
from_char = string.find('>')
num_of_explosions = 0

for i in range(from_char, len(string)):
    if string[i] == '>':
        num_of_explosions += int(string[i+1])
    elif num_of_explosions > 0:
        num_of_explosions -= 1
        string = string[:i] + ' ' + string[i+1:]

print(string.replace(' ', ''))