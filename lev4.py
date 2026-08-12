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
'''