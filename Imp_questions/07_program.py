import math

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}:"))
    numbers.append(num)
    
factorials = [math.factorial(n) for n in numbers]

print("Original list:", numbers)
print("Factorial list:",factorials)