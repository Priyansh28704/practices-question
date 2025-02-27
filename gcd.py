a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b:
    a, b = b, a % b  # Apply Euclidean Algorithm

print("GCD is:", a)




# a = int(input("Enter first number: "))  
# b = int(input("Enter second number: "))  

# gcd = 1  # Initialize GCD as 1 (smallest possible GCD)

# # Find the smallest number between a and b
# smallest = min(a, b)

# # Check all numbers from 1 to smallest
# for i in range(1, smallest + 1):
#     if a % i == 0 and b % i == 0:  # If 'i' divides both numbers
#         gcd = i  # Update GCD

# print("GCD is:", gcd)
