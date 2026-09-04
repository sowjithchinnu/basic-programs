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

# Write a program to find the largest and smallest number that can be formed using the digits of n.
n = int(input("enter a number: "))
num = n
digits = []
while num > 0:
    digits.append(num%10)
    num //= 10
sort = sorted(digits)
smallest = int(''.join(map(str, sort)))
largest = int(''.join(map(str, list(reversed(sort)))))
print(f"the smallest and largest number that can be formed using the number {n} are {smallest} and {largest}")

# Write a program to convert a decimal number into its binary equivalent.
n = int(input("enter a number: "))
binary = ""
if n == 0:
    print("0")
else:
    while n > 0:
        binary = str(n%2) + binary
        n //= 2
    print(binary)

# Write a program to convert a binary number into its decimal equivalent.
n = input("enter a binary number: ")
power = 0
decimal = 0
for digit in (reversed(n)):
    if digit == '1':
        decimal += 2 ** power
    power += 1
print(decimal)

# Write a program to display a menu that lets the user repeatedly choose any of the above tasks until they choose to exit.
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def digitSum(n):
    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    return n
    
def palindromeAndPrime(n):
    num = n
    rev = 0
    while num > 0:
        last = num % 10
        rev = rev * 10 + last
        num //= 10
    palin = (rev == n)
    return palin and isPrime(n)

def decimalToBinary(n):
    binary = ""
    if n == 0:
        return "0"
    else:
        while n > 0:
            binary = str(n%2) + binary
            n //= 2
        return binary

while True:
    print("\n1. check prime")
    print("2. check the repeated sum of digits")
    print("3. check if is both palindrome and prime")
    print("4. convert decimal to binary")
    print("5. Exit")
    
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        n = int(input("enter a number: "))
        print(isPrime(n))
    elif choice == 2:
        n = int(input("enter a number: "))
        print(digitSum(n))
    elif choice == 3:
        n = int(input("enter a number: "))
        print(palindromeAndPrime(n))
    elif choice == 4:
        n = int(input("enter a number: "))
        print(decimalToBinary(n))
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("invalid choice")
'''