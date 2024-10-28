#Write a Python program to get the Fibonacci series of given range.

def fibonacci(n):
    fib_seq = [0,1]
    for i in range(2,n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[:n]

num = int(input("Enter any positive integer:"))
print(fibonacci(num))