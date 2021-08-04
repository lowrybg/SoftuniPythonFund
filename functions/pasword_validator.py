import math
data = input()
#TODO 40%

def pass_long(password):
    if len(password)<6 or len(password)>11:
        print('Password must be between 6 and 10 characters')
    else:
        return True



def only_alfanum(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")



    digit_count = 0
    for n in range(len(password)):
        if password[n].isdigit():
                digit_count +=1
    if digit_count <=2:
        print("Password must have at least 2 digits")
    else:
        return True


first = pass_long(data)
second = only_alfanum(data)
print(first)
print(second)
if first and second:
    print('Password is valid')
