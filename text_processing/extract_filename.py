line = input().split('\\')

line_length = len(line) -1


splitted = line[line_length].split('.')

file_name = splitted[0]
ext = splitted[1]

print(f'File name: {file_name}')
print(f'File extension: {ext}')

