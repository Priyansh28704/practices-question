def palindrome(string):
    return string
string= input("enter the word:")
if (string==string[::-1]):
    print(string,"is palindrome")
else:
    print(string,"is not a palidrome")