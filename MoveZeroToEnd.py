def Move_zero(arr):
    count =0

    for i in range(len(arr)):
        if arr[i] !=0:
            arr[count],arr[i] = arr[i],arr[count]

            count += 1
    return arr

arr = list(map(int,input("enter array").split()))

print(Move_zero(arr))

