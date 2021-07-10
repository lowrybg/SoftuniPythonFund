numbers = list(map(int,input().split()))


index = input()
count = 0
while index != 'End':
    index = int(index)
    if index < len(numbers):
        count +=1
        shoot_position_num = numbers[index]
        for n in range(len(numbers)):
            if numbers[n] < 0:
                continue
            if numbers[n] > shoot_position_num:
                 numbers[n] = numbers[n] - shoot_position_num
            else:
                numbers[n] = numbers[n] + shoot_position_num


        numbers[index] = -1

    index = input()

print(f"Shot targets: {count} -> {' '.join(map(str, numbers))}")

