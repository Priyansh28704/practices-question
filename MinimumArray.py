def find_min(arr):
    min_val = arr[0] 
    for num in arr:
        if num < min_val:  
            min_val = num  
    return min_val

arr = [1,3 , 7, 5, 9, 2]
print(find_min(arr))
