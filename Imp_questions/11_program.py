name = ['Dhiru', 'Vir', 'Ram']
roll_numbers = [12,34,56]
marks = [89, 56, 76]

combined_lists = list(zip(name, roll_numbers, marks))

print(combined_lists)

name_tuple = tuple([item[0] for item in combined_lists])
rollNumbers_tuple = tuple([item[1] for item in combined_lists])
marks_tuple = tuple([item[2] for item in combined_lists])

print(name_tuple)
print(rollNumbers_tuple)
print(marks_tuple)

