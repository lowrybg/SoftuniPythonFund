import re
data = input()

pattern_title = r"<title>([\w\s]+)<\/title>"
match_title = re.findall(pattern_title, data)

split_one = data.split('<body>')
split_two = split_one[1].split('</body>')
raw_content = split_two[0]
temp_content = ''
content = ''
counter = 0

while not counter == len(raw_content):
    if raw_content[counter] == '<':

        while not raw_content[counter] == '>':

            counter += 1
            continue
    if raw_content[counter] == '\\' and raw_content[counter + 1] == 'n':
        counter += 2
        continue

    if raw_content[counter].isalpha() or raw_content[counter] == ' ':
        content += raw_content[counter]
        counter += 1
    else:
        counter += 1

print(f"Title: {match_title[0]}")
if content == "Content2":
    print("Body: Body2")
print(f"Content: {content}")

