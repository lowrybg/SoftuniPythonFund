import re

pattern_title = r"<title>[\w\s]+<\/title>"
raw_content = ''

temp_content = ''

content = ''
for n in range(len(raw_content)):
    if raw_content[n] == '<':
        while raw_content[n] == '>':
            n += 1
            continue
    if raw_content[n] == '\\' and raw_content[n+1] == 'n':
        continue
    if raw_content[n].isalpha():
        content += raw_content[n]
    else:
        n += 1

print(content)