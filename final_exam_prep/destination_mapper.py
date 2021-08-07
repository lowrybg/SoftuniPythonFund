import re

data = input()

pattern = r"(?<=(\=|\/))[A-Z][a-zA-Z]{2,}(?=(\1))"

matches = re.finditer(pattern,data)
result = [el.group() for el in matches]

counter = 0

for el in result:
    for k in el:
        counter += 1

print(f"Destinations: {', '.join(result)}")
print(f'Travel Points: {counter}')
