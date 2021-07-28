import  math
nums = input().split(', ')
numbers = [int (n) for n in nums]

max_num = max(numbers)
cycle = math.ceil(max_num/10)
x = 1

while x < cycle+1:
    ten_s = x*10

    print(f'Group of {ten_s}\'s: {[int(num) for num in numbers if num <= ten_s and num > ten_s -10]}')
    x+=1
