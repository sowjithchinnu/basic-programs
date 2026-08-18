
'''# Write a program to read a number and check whether it is prime or not.
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
'''

# Write a program to check whether a number is a perfect number.
