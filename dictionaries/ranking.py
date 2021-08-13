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
    if contest in contest_dict_data and [password in k for c, k in contest_dict_data.items()]:
        if username not in students_dict:
            students_dict[username] = {contest : int(points)}
        else:
            if contest not in students_dict[username]:

                students_dict[username].update({contest : int(points)})
            else:
                students_dict[username][contest] += points
    students = input()



print(students_dict)
