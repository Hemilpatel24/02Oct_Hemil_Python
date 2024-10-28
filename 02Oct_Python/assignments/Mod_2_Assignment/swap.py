#Write python program that swap two number with temp variable and without temp variable.

#--------using temp----------------#
"""num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Before swapping")
print(f"num1 is:{num1}")
print(f"num2 is:{num2}")
print("After swapping")
temp = num1
num1 = num2
num2 = temp
print(f"num1 is:{num1}")
print(f"num2 is:{num2}")"""
#-------------without temp----------#
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("Before swapping")
print(f"num1 is:{num1}")
print(f"num2 is:{num2}")
print("After swapping")
num1,num2 = num2,num1
print(f"num1 is:{num1}")
print(f"num2 is:{num2}")

