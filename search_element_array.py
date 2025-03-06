def search_element(arr,target):
    return target in arr

arr =[1,2,3,4,5,6]
target=int(input("enter search value:"))

print(search_element(arr,target))