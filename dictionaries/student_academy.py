n = int(input())

my_dict = {}


for _ in range(n):
    name = input()
    grade = float(input())

    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(grade)

filtered = {}
for key, value in my_dict.items():
    av_grade = sum(value)/len(value)

    if av_grade >= 4.5:
        filtered[key] = av_grade


for key, value in sorted(filtered.items(), key=lambda x: x[1], reverse=True):
    print(f'{key} -> {value:.2f}')
