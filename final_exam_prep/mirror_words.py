import  re
import  math

string_line = input()

pattern = r"(?<=(@|#))+(?P<first_word>[A-Za-z]{3,})(\1){2}[A-Za-z]{3,}(?=\1)"

matches = re.finditer(pattern,string_line)
matches = [el.group() for el in matches]
if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print("No word pairs found!")


mirror = False
mirror_words = []
for el in matches:
    middle = int(len(el)/2)
    first =  el[:middle-1]
    second = el[middle+1:]
    if first == second[::-1]:
        mirror_words.append(f'{first} <=> {second}')
        mirror = True

if not mirror:
    print('No mirror words!')
if mirror_words:
    print('The mirror words are:')
    print(", ".join(mirror_words))