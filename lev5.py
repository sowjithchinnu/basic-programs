'''
# Write a program to read a number and check whether it is prime or not.
n = int(input("enter a number: "))
if n <= 1:
    print(f"{n} is not a prime number")
else:
    is_prime = True
    
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime :
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

# Write a program to display all prime numbers from 1 to n.
n = int(input("enter a number: "))
if n <= 1:
    print("no prime numbers!")
else:
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

# Write a program to display the first n prime numbers.
n = int(input("enter a number: "))
if n <= 0:
    print("No prime numbers!")
count = 0
i = 2
while count < n:
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
        count += 1
    i += 1

# Write a program to check whether a number is an Armstrong number.
n = int(input("enter a number: "))
power = len(str(n))
total = 0
for digit in str(n):
    total += int(digit) ** power
if total == n:
    print("is an Armstrong number")
else:
    print("not an Armstrong number")

# Write a program to display all Armstrong numbers from 1 to n.
n = int(input("enter a number: "))
for i in range(1, n + 1):
    power = len(str(i))
    total = 0
    for digit in str(i):
        total += int(digit) ** power
    if total == i:
        print(i)

# Write a program to check whether a number is a perfect number.
n = int(input("enter a number: "))
total = 0
for i in range(1, n//2 + 1):
    if n % i ==0:
        total += i
if total == n and n>0:
    print("it is a perfect number")
else:
    print("it is not a perfect number")

# Write a program to check whether a number is a strong number (sum of factorials of its digits).
n = int(input("enter a number: "))
total = 0
for digit in str(n):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    total += fact
if total == n:
    print("it is a strong number")
else:
    print("not a strong number")

# Write a program to check whether a number is an automorphic number.
n = int(input("enter a number: "))
square = n*n
if str(square).endswith(str(n)):
    print("it is an automorphic number")
else:
    print("it is not an automorphic number")

# Write a program to check whether a number is a Harshad (Niven) number.
n = int(input("enter a number: "))
summ = 0
if n <= 0:
    print("it is not a Harshad number")
else:
    for digit in str(n):
        summ += int(digit)
    if n % summ == 0:
        print("it is a Harshad number")
    else:
        print("it is not a Harshad number")

# Write a program to find all factors (divisors) of a number n.
n = int(input("enter a number: "))
if n <= 0:
    print("there ain't no factors")
else:
    for i in range(1, n//2 + 1):
        if n % i == 0:
            print(i)
    print(n)
'''
