import  re
line = input().split()
#TODO It gives 80%, not working if length of word is 2 chars
pattern = r"\d+"
deciphered = []
for n in range(len(line)):
    digits_in_word = re.findall(pattern, line[n])
    digits_in_word = [int(el) for el in digits_in_word]
    first_char = chr(digits_in_word[0])

    word = line[n][len(str(ord(first_char))):]
    switched = word[len(word)-1:] + word[1:len(word)-1] + word[:1]
    # switch_last = word[len(word):]
    finished_word = first_char + switched
    deciphered.append(finished_word)


print(*deciphered)