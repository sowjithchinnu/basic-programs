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
while n >= 10:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total
print(n)

# Write a program to count the number of prime digits present in a number n.
n = int(input("enter a number: "))
prime_digits = {2, 3, 5, 7}
count = 0
for i in str(n):
    if int(i) in prime_digits:
        count += 1
print(count)

# Write a program to check whether a number is a palindrome and a prime at the same time.
n = int(input("enter a number: "))
num = n
rev = 0
while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num //= 10
palin = (rev == n)
if n < 2:
    isPrime = False
else:
    isPrime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            isPrime = False
            break
if isPrime and palin:
    print(True)
else:
    print(False)
'''