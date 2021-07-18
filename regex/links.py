import  re
line = input()

pattern = r"w{3}.[a-zA-Z0-9-]+(\.[a-z]+)+"

while line:

    # match = re.match(pattern,line)

    result = ([el.group()for el in re.finditer(pattern,line)])
    if result:
        print(*result)

    line = input()