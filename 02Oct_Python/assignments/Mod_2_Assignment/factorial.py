#Write a Python program to get the Factorial number of given number.

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter positive integer:"))
print(factorial(num))