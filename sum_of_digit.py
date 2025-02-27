x=int(input("enter a number"))

sum=0

while x>0:
    sum += x%10
    x//=10

print(sum)