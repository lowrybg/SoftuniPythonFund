text = input().split()

chars = {}
for n in range(len(text)):
    word = text[n]
    for n in range(len(word)):
        char = word[n]
        if char not in chars:
            chars[char] = char
            chars[char] = 0
            chars[char] += 1
        else:
            chars[char] += 1



for key, value in chars.items():
    print(f'{key} -> {value}')