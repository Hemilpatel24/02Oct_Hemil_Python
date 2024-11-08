"""Write a Python program to sum of three given integers. However, 
if two values are equal sum will be zero."""

a = int(input("Enter Integer1:"))
b = int(input("Enter Integer2:"))
c = int(input("Enter Integer3:"))

if(a==b or a==c or b==c):
    print("The sum is Zero.")
else:
    sum = a+b+c
    print(f"The sum of given integers is {sum}")