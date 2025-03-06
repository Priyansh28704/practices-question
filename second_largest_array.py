def largest_element(arr):
    if len(arr)<2:
        return None,None
    
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num!= first:
            second = num 
    
    return first,second


arr = [8,3,6,2,1,4,10]
first,second = largest_element(arr)
print("largest:",first)
print("second largest:",second)