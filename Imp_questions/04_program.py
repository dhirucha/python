numbers = [5, 3, 8, 5, 12, 3, 9, 15, 8, 20, 17, 5, 2, 20, 1, 3, 4, 12, 6, 9]


unique_numbers = list(set(numbers))

unique_numbers.sort()

print("Original list (with duplicates):", numbers)
print("List after removing duplicates:", unique_numbers)