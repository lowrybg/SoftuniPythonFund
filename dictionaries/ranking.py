contest_data = input()

contest_dict_data = {}
while not contest_data == 'end of contests':
    data = contest_data.split(':')
    contest_dict_data[data[0]] = []
    contest_dict_data[data[0]].append(data[1])

    contest_data = input()


students = input()
students_dict = {}
while not students == 'end of submissions':
    line = students.split('=>')
    contest, password, username, points = line
    points = int(points)
    for c, k in contest_dict_data.items():
        if password in k:
            my_bool = True
        else:
            my_bool = False
    if contest in contest_dict_data and my_bool:
        if username not in students_dict:
            students_dict[username] = {contest :  int(points)}
        else:
            if contest not in students_dict[username]:

                students_dict[username].update({contest : int(points)})
            else:
                if students_dict[username][contest] < points:
                    students_dict[username][contest] = points
    students = input()


max_num = 0
max_stud = ''
for es, v in students_dict.items():
    maxi = 0
    for e, z in v.items():
        maxi += z
        if maxi > max_num:
            max_num = maxi
            max_stud = es


print(f"Best candidate is {max_stud} with total {max_num} points.")
print('Ranking:')
students_dict = sorted(students_dict.items(), key=lambda x: (x[0]))



for stud, v in students_dict:
    print(stud)
    for q, w in sorted(v.items(),key=lambda x: -x[1]):
        print(f'#  {q} -> {w}')