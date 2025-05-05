def isArmstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num

print("Armstrong numbers between 1 and 500 are: ")

for i in range(1, 501):
    if isArmstrong(i):
        print(i)