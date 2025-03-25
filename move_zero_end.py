def move_zero_to_end(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index],arr[i] = arr[i],arr[non_zero_index]
            non_zero_index += 1
    return arr

#arr = [1,0,2,0,3,4,5,0,6,0]
arr = list(map(int,input("enter array with zero:").split()))

print(move_zero_to_end(arr))