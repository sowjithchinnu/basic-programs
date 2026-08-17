
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
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)
'''
