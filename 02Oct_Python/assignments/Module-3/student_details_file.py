"""fl = open("studentsdata.txt", 'x')"""

fl = open("studentdata.txt", 'a')

ID = input("Enter your id:")
NAME = input("Enter your name:")
CITY = input("Enter your city:")

fl.write(f"ID:{ID}\nNAME:{NAME}\nCITY:{CITY}\n=================================\n")



