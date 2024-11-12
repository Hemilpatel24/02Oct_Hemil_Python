"""fl = open("studentsdata.txt", 'x')"""

fl = open("studentdata.txt", 'a')
n = int(input("Enter number of students:"))

for i in range(n):
    ID = input("Enter your id:")
    NAME = input("Enter your name:")
    CITY = input("Enter your city:")

fl.write(f"ID:{ID}\nNAME:{NAME}\nCITY:{CITY}\n=================================\n")



