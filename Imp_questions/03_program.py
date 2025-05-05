import random

numbers = [random.randint(1, 10) for _ in range(20)]
print("Generated list:", numbers)

target = int(input("Enter the number to search for:"))

positions = [index for index, value in enumerate(numbers) if value == target]

if positions:
    print(f"The number {target} occurs at positions: {positions}")
else:
    print(f"The number {target} does not exist in the list.")