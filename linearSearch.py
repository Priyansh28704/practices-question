def linear_search(arr,target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
    
arr = list(map(int,input("enter array:").split()))
target = int(input("enter target or search value in array:"))

result = linear_search(arr,target)

if result != -1:
    print ("element found at index:",result)
else:
    print("element not found    ")