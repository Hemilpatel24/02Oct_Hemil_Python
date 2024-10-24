data = []

n = int(input("Enter number of elements:"))
for i in range(n):
    city = input("Enter city names:")
    data.append(city)
print(tuple(data))