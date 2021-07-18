import re

text = input()

pattern = r"(\d+)"

result = []
while text:

    result.extend( [el.group() for el in re.finditer(pattern, text)])
    text = input()
print(' '.join(result))