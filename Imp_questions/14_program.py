import random

random_set = set(random.sample(range(15, 45), 10))
print("Original Set:", random_set)

count_less_than_30 = sum(1 for num in random_set if num < 30)
print("Less than 30:", count_less_than_30)

filtered = {num for num in random_set if num > 35}
print("Set after deletion of greater than 35:", filtered)
