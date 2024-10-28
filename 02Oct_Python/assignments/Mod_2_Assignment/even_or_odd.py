#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

num = int(input("Enter any positive number:"))

if(num==0 or num%2==0):
    print(f"{num} is an Even Number.")
else:
    print(f"{num} is an Odd Number.")
