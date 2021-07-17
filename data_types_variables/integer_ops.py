result = []
for n in range(4):
    nums = int(input())
    result.append(nums)

print(f'{((result[0]+result[1])//result[2])*result[3]}')