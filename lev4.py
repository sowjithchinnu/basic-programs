'''
# Write a program to count the number of digits in a number n.
n = int(input("enter a number: "))
temp = abs(n)
count = 0 if temp > 0 else 1
while temp > 0:
    temp //= 10
    count += 1
print(count)

# Write a program to display all the digits of a number n (one per line).
n = int(input("enter a number: "))
temp = abs(n)
digits = []
if temp == 0:
    digits.append(temp)
while temp > 0:
    last = temp % 10
    digits.append(last)
    temp //= 10
for digits in reversed(digits):
    print(digits)

# Write a program to find the sum of all digits of a number n.
n = int(input("enter a number: "))
temp = abs(n)
total_sum = 0
while temp > 0:
    total_sum += temp % 10
    temp //= 10
print(total_sum)

# Write a program to find the product of all digits of a number n.
n = int(input("enter a number: "))
temp = abs(n)
product = 1 if temp > 0 else 0
while temp > 0:
    last = temp % 10
    product *= last
    temp //= 10
print(product)

# Write a program to reverse a number n.
n = int(input("enter a number: "))
temp = abs(n)
reverse = 0
if temp == 0:
    reverse = 0
while temp > 0:
    last = temp % 10
    reverse = reverse * 10 + last
    temp //= 10
if temp < 0:
    reverse = -reverse
print(reverse)

# Write a program to find the largest digit in a number n.
n = int(input("enter a number: "))
temp = abs(n)
maxx = 0
while temp > 0:
    last = temp % 10
    if last > maxx:
        maxx = last
    temp //= 10
print(maxx)

# Write a program to find the smallest digit in a number n.
n = int(input("enter a number: "))
temp = abs(n)
minn = 9
if temp == 0:
    minn = 0
while temp > 0:
    last = temp % 10
    if last < minn:
        minn = last
    temp //= 10
print(minn)

# Write a program to count the number of even digits and odd digits in a number n.
n = int(input("enter a number: "))
temp = abs(n)
even_count = 0
odd_count = 0
if temp == 0:
    even_count = 1
while temp > 0:
    last = temp % 10
    if last % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    temp //= 10
print(f"the number of even digits in the given number {n} are {even_count}")
print(f"the number of odd digits in the given number {n} are {odd_count}")

# Write a program to check whether a number n is a palindrome (reads the same reversed).
n = int(input("enter a number: "))
temp = abs(n)
real = n
palindrome = 0
while temp > 0:
    last = temp % 10
    palindrome = palindrome * 10 + last
    temp //= 10
if real == palindrome:
    print("is palindrome")
else:
    print("not a palindrome")
    
# Write a program to replace all zeros in a number n with the digit 5.
n = int(input("enter a number n: "))
temp = abs(n)
replace = 0 if temp > 0 else 5
multiplier = 1
while temp > 0:
    last = temp % 10
    if last == 0:
        last = 5
    replace += (last * multiplier)
    multiplier *= 10
    temp //= 10
if n < 0:
    replace = -replace
print(replace)

# Write a program to find the sum of the first and last digit of a number n.
n = int(input("enter a number: "))
temp = abs(n)
last_digit = temp % 10
while temp >= 10:
    temp //= 10
first_digit = temp
summ = first_digit + last_digit
print(summ)
'''