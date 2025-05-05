numbers = [12, -7, 5, -3, -15, 9, 0, 4, -1]

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("Original list:", numbers)

print("Positive numbers in list:", positive_numbers)
print("Negative numbers in list:", negative_numbers)