import  re

text = input()

pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>[0-9]+\.?[0-9]+)!(?P<quantity>[0-9]+)"

names = []
price = 0
while text != 'Purchase':

    match = re.match(pattern,text)
    if match:
        data = match.groupdict()
        names.append(data['name'])
        price += float(data['price'])*int(data['quantity'])


    text = input()

print('Bought furniture:')
if len(names) > 1:
    print(*[el for el in names],sep='\n')
print(f'Total money spend: {price:.2f}')