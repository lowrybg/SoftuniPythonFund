import  math
numbers = [int(num) for num in input().split(' ')]


max = max(numbers)
min = min(numbers)
average = (max + min)/2
result = []

for num in numbers:
    if num > average:
        result.append(num)


sorted_result =sorted(result, key=int, reverse=True)

print(*sorted_result[:5], sep=' ')
if len(result) == 0:
    print('No')