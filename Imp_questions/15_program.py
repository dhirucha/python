marks = {
    'Subu': {'Maths': 88, 'Eng': 60, 'SST': 95},
    'Amol': {'Maths': 78, 'Eng': 68, 'SST': 89},
    'Raka': {'Maths': 56, 'Eng': 66, 'SST': 77}
}

print("Amol marks in english:", marks['Amol']['Eng'])

marks['Raka']['Maths'] = 77
print(marks['Raka']['Maths'])

sorted_dict = dict(sorted(marks.items()))

for name, subjects in sorted_dict.items():
    print(name, ":", subjects)