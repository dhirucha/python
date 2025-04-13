# with iterative approach
# finding factorial
def findingFactorial(n):
    result = 1
    if n == 0 or n == 1:
        return 1

    else:
        for i in range(2, n+1):
            result = result * i
        return result    
        

# Driver code
n = 8
result = findingFactorial(n)
print("The factorial of given number is:", result)