import re
text = input()

pattern = r"\b(^|(?<=\s))[a-zA-Z0-9]+[-._]?[a-zA-Z0-9]+@[a-z]+[-.][a-z.]+\b"

emails = []

emails.extend([el.group()for el in re.finditer(pattern,text)])

print('\n'.join(emails))