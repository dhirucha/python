# Insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j+1] = key


    return arr

#Driver code
arr = [4,3,5,90,1,4]
result = insertionSort(arr)
print("After insertion sort: ", result)