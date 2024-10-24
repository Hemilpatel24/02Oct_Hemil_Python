dict = {}

n = int(input("Enter the number of pairs you want:"))

for i in range(n):
    X = (input("Enter the Key:"))
    Y = (input("Enter the Values:"))

data = X,Y
print(dict(data))
