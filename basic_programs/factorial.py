def factorial(n):
    result = 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
       

n = 5
result = factorial(n)
print(result)