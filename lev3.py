'''
# Write a program to display all the natural numbers from 1 to n. (n is user input)
n = int(input("enter a number: "))
for i in range(1, 1+n):
    print(i)

# Write a program to display all natural numbers from 1 to n in reverse order.
n = int(input("enter a number : "))
while n>=1:
    print(n)
    n -= 1

# Write a program to display all even numbers from 1 to n.
n = int(input("enter a number: "))
for i in range(1, 1+n):
    if i % 2 == 0:
        print(i)

# Write a program to display all odd numbers from 1 to n.
n = int(input("enter a number: "))
for i in range(1, 1+n):
    if i % 2 != 0:
        print(i)

# Write a program to find the sum of all natural numbers from 1 to n.
n = int(input("enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# Write a program to find the sum of all even numbers from 1 to n.
n = int(input("enter a number: "))
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
print(sum)

# Write a program to find the sum of all odd numbers from 1 to n.
n = int(input("enter a number: "))
sum = 0
for i in range(1, 1+n, 2):
    sum += i
print(sum)

# Write a program to find the product of all natural numbers from 1 to n (factorial of n).
n = int(input("enter a number: "))
product = 1
for i in range(1, 1+n):
    product *= i
print(product)

# Write a program to display the multiplication table of a number n.
n = int(input("enter a number: "))
for i in range(1, 11):
    print(n, "multiplied by", i, "=", n*i )

# Write a program to display all multiples of a number m up to n terms.
m = int(input("enter a number: "))
n = int(input("decide how many multiples the number can have: "))
for i in range(1, n+1):
    print(m*i)

# Write a program to count how many numbers from 1 to n are divisible by 3.
n = int(input("enter a number: "))
count = 0
for i in range(1, 1+n):
    if i % 3 == 0:
        count += 1
print(count)

# Write a program to display all numbers from 1 to n that are divisible by 3 or 5.
n = int(input("enter a number: "))
for i in range(1, n+1):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i)
'''