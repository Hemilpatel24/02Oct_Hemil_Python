file = open("Table_File.txt", 'x')
n = int(input("How many tables you want:"))

for i in range(n):
    n1 = int(input("Enter Table:"))
    for j in range(1,11):
        file.write(f"{n1}*{j}={n1*j}\n")
    file.write("=================\n")    
    




