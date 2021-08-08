import  math
import re
data = input()

pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"

# matches = re.finditer(pattern, data)
calories = [int(c.group('calories')) for c in re.finditer(pattern, data)]
item =  [i.group('item') for i in re.finditer(pattern, data)]
dates = [d.group('date') for d in re.finditer(pattern, data)]

print(f"You have food to last you for: {sum(calories)//2000} days!")

for k in range(len(item)):
    print(f"Item: {item[k]}, Best before: {dates[k]}, Nutrition: {calories[k]}")