"""fl = open("myfile.txt", 'x')
print("File is created.")"""

fl = open("myfile.txt", 'w')

ID = input("Enter your id:")
NAME = input("Enter your name:")
CITY = input("Enter your city:")

fl.write(f"ID:{ID}\n")
fl.write(f"NAME:{NAME}\n")
fl.write(f"CITY:{CITY}\n")

