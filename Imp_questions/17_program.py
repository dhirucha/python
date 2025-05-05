import random

multiples_of_4 = [i for i in range(40, 161) if i % 4 == 0 ]

matrix = []
for i in range(4):
    row = random.sample(multiples_of_4, 5)
    
    matrix.append(row)

print("Matrix which are multiples of 4 between 40 to 161:-")    
for row in matrix:
    print(row)