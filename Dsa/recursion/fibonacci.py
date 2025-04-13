# fibonacci series
def fibonacciSeries(n):
    if n <= 1:
        return 1
    else:
        return fibonacciSeries(n-1) + fibonacciSeries(n-2)



# Driver code
n = 5

for i in range(n):
    print(fibonacciSeries(i))