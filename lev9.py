'''
# Write a program to check whether a number is prime, using a function/method.
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(isPrime(1012))

# Write a program to print all prime numbers between two given numbers a and b.
first = int(input("enter a number to start with: "))
last = int(input("enter the last number: "))
if last < first:
    print("the first number should be smaller than the last number")
elif last < 2:
    print("there are no prime numbers between them")
else:
    for i in range(max(2, first), last):
        isPrime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            print(i)

# Write a program to find the sum of digits of a number repeatedly until a single digit remains.
n = int(input("enter a number: "))
total = n
while n >= 10:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total
print(total)
'''