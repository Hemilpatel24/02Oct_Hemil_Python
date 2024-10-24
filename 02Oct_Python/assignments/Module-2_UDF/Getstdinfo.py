def stdinfo(id,name):
    print(f"ID:{id}\nNAME:{name}")

n = int(input("Enter numbers of students:"))
for i in range(n):
    p = int(input("Enter your ID:"))
    q = (input("Enter your NAME:"))

print(stdinfo(p,q))


