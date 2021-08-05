line = input()

result = []
for n in range(len(line)):
    next_char = chr(ord(line[n]) + 3)
    result.append(next_char)
print("".join(result))