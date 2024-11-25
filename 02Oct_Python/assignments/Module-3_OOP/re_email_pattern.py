import re

Name = input("Enter your Name:")
#===================================================#
Email = input("Enter your email:")
email_patter = "^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]{2,}$"
a = re.findall(email_patter,Email)
if a:
    print("Email is Valid....")
else:
    print("Invalid Email....")
#====================================================#
Mobile_no = (input("Enter your Mobile number:"))
if Mobile_no.isdigit() and int(len(Mobile_no)) == 10:
    print("Valid Mobile Number.")
else:
    print("Invalid mobile number.")
#=====================================================#
Password = input("Enter your Password:")
pass_pattern = "[A-Za-z0-9!@#%_]"
b = re.findall(pass_pattern,Password)
if b:
    print("Valid password")
else:
    print("Invalid password")
#=====================================================#
Confirm_Password = input("Confirm your password:")
confirm_pass_pattern = "[A-Za-z0-9!@#%_]"
c = re.findall(confirm_pass_pattern,Confirm_Password)
if c:
    print("Password Confirmed")
else:
    print("Password is not matching")
#======================================================#
print("===========================\nSigned in Successfully.")
