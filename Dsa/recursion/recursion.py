
# with recursive approach
# finding factorial
def findingFactorial(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n*findingFactorial(n-1)

# Driver code
n = 8
result = findingFactorial(n)
print("The factorial of given number is:", result)