import  math
nums = input().split()

count = int(input())
nums = [int(n) for n in nums]
for n in range(count):
    min_num = min(nums)
    nums.remove(min_num)

nums = [str(n) for n in nums]
print(", ".join(nums))

