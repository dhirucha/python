names = {'Alice', 'Bob', 'Anil', 'Amol', 'Brijesh'}

names_start_A = {name for name in names if name.startswith('A')}
names_start_B = {name for name in names if name.startswith('B')}

print(names_start_A)
print(names_start_B)

