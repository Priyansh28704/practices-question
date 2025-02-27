# n = int(input("enter the number"))
# if n>1:
        
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             print(n,"is not a prime number")
#             break
#     else:
#         print(n," is a prime number")
# else:
#     print(n,"is not a prime number")


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):  # Check from 2 to num-1
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")  
else:
    print("Not Prime")

