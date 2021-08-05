data = input().split()

shortest = min(data, key=len)
longest = max(data, key=len)
result = 0
if len(shortest) != len(longest):
    for n in range(len(shortest)):
        temp_multi = ord(shortest[n]) * ord(longest[n])
        result += temp_multi
    left = longest[len(shortest):]
    left_ord = sum([ord(el) for el in left])
    result += left_ord
else:
    for n in range(len(data[0])):
        temp_multi = ord(data[0][n]) * ord(data[1][n])
        result += temp_multi


print(result)

