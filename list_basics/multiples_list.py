factor = int(input())
count = int(input())

result = []
counter = 1

while counter < count+1:
    result.append(factor*counter)
    counter += 1

print(result)