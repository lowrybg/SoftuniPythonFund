import re
#TODO 60%
num = int(input())

pattern_star = r"[s, t, a, r]"
pattern_decr = r"@(?P<planet>[A-za-z]+)[0-9]?:(?P<population>[0-9]+)!(?P<attack>[A,D])!->(?P<soldier>[0-9]+)"
decripted = {}
for mes in range(num):
    line = input()
    match_decr = re.findall(pattern_star,line, flags=re.IGNORECASE)
    if match_decr:
        decripted[line] = ''
        for back in line:
            temp_num_back = ord(back) - len(match_decr)
            decripted[line] += chr(temp_num_back)
attacked = []
destroyed = []
for k in decripted.items():
    match_planet = re.finditer(pattern_decr,k[1])
    match_planet = [pl.groupdict() for pl in match_planet]
    for i in match_planet:
        if i["attack"] == 'A':
            attacked.append(i['planet'])
        elif i["attack"] == 'D':
            destroyed.append(i['planet'])

attacked = sorted(attacked, key=lambda x: x)
destroyed = sorted(destroyed, key=lambda x: x)
print(f"Attacked planets: {len(attacked)}")
for a in attacked:
    print(f"-> {a}")
print(f"Destroyed planets: {len(destroyed)}")
for d in destroyed:
    print(f"-> {d}")