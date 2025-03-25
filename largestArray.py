def find_largest(arr):
    largest = arr[0]

    for i in range(1,len(arr)):
        if largest<arr[i]:
            largest = arr[i]
    return largest
        

arr = [10,2,30,5]

print(find_largest(arr))