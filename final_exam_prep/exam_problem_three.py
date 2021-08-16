first_line = input()

words_descriptions = first_line.split('|')
my_dict = {}

for el in words_descriptions:
    word_splitted_descr = el.split(':')
    word = word_splitted_descr[0].strip()
    description = word_splitted_descr[1]
    if word not in my_dict:
        my_dict[word] = []
        my_dict[word].append(description)
    else:
        my_dict[word].append(description)


command_args = input()
words_to_test = command_args.split('|')
command = input()
my_dict = sorted(my_dict.items(), key=lambda x: (x[0], -len(x[1])))
if command == 'Hand Over':
    for k, v in sorted(my_dict):
        print(k, end=' ')

elif command == 'Test':
    for w in words_to_test:
        w = w.strip()
        for k, v in my_dict:
            if w in k:
                print(f'{k}:')
                for d in sorted(v, key=len,reverse=True):
                    d = d.strip()
                    print(f' -{d}')


