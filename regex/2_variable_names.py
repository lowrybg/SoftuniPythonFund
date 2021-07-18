import re

text = input()

pattern = r"(^_|(?<=\s\_))[a-zA-Z0-9]+\b"

print(*[el.group() for el in re.finditer(pattern,text)], sep=',')