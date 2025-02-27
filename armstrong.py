num = int(input("Enter a number: "))  
sum = 0  
temp = num  
num_digits = len(str(num))  # Count number of digits

while temp > 0:
    digit = temp % 10  # Get last digit
    sum += digit ** num_digits  # Add (digit ^ num_digits)
    temp //= 10  # Remove last digit
 
if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    