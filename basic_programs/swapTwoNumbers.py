a = 5
b = 10

print(f"Before swap {a} and {b}")

# method 1
# a, b = b, a

# method 2
# a = a + b
# b = a - b
# a = a - b

# method 3
a = a ^ b
b = a ^ b
a = a ^ b

print(f"Before swap {a} and {b}")


