# function definition with recursive function
def ternarySearch(arr, x, l, r):
    while l <= r:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        
        if x == arr[mid1]:
            return mid1
        elif x == arr[mid2]:
            return mid2
        
        elif x < arr[mid1]:
            r = mid1 - 1
        elif x > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1

# Driver code
arr = [1,2,3,4,5,6,7,8,9,10]
l = 0
r = len(arr) - 1 
x = 10

result = ternarySearch(arr, x, l, r)
print("Searching element present at index:", result)
