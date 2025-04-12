# Selection sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
    
        # swap number
        arr[i], arr[min_idx] = arr[min_idx], arr[i]    

    return arr


#Driver code
arr = [15,5,45,38,90,34,56]
result = selectionSort(arr)
print("After selection sort: ",result)