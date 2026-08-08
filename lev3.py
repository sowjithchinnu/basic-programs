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
'''