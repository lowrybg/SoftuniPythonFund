cards = input().split()
number = int(input())

first_half = []
second_half = []
first_card = cards[0]
last_card = cards[len(cards)-1]
result = []

for el in range(1, len(cards) // 2):
    first_half.append(cards[el])
for k in range (len(cards) // 2, len(cards) - 1):
    second_half.append(cards[k])

for num in range(number):
    temp = []
    for x in range(len(first_half)):

        temp.append(second_half[x])
        temp.append(first_half[x])
    result = temp
    first_half = result[:len(result)//2]
    second_half = result[len(result)//2:]
result.insert(0, first_card)
result.append(last_card)
print(result)
