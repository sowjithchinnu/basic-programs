'''
# Write a program to display the first n terms of the Fibonacci series.
n = int(input("enter a number: "))
a = 0
b = 1
for i in range(n):
    print(a)
    a, b = b, a+b

# Write a program to find the sum of the first n terms of the Fibonacci series.
n = int(input("enter a number: "))
a = 0
b = 1
total = 0
for i in range(n):
    total += a
    a, b = b, a+b
print(total)

# Write a program to find the sum of the series 1 + 2 + 3 + ... + n.
n = int(input("enter a number: "))
total = n*(n +1) // 2
print(total)

# Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.
n = int(input("enter a number: "))
total = n*(n+1)*(2*n + 1)//6
print(total)

# Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.
n = int(input("enter a number: "))
total = 0
for i in range(1, n+1):
    total += 1/i
print(f"{total:.4f}")
'''
