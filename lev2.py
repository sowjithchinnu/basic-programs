'''
# Write a program to read a number and check whether it is even or odd.
number = int(input("enter a number: "))
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")
    
# Write a program to read a number and check whether it is positive, negative or zero.
number = int(input("enter a number: "))
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("the number is zero")

# Write a program to read three numbers and find the largest among them.
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")

# Write a program to read three numbers and find the smallest among them.
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))
if num1 <= num2 and num1 <= num3:
    print(f"{num1} is the smallest number")
elif num2 <= num1 and num2 <= num3:
    print(f"{num2} is the smallest number")
else:
    print(f"{num3} is the smallest number")
    
# Write a program to read a year and check whether it is a leap year or not.
year = int(input("enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("it is a leap year")
else:
    print("it is not a leap year")

# Write a program to read a character and check whether it is a vowel or a consonant.
char = str(input("enter a string: "))
lower = char.lower()
if len(char) == 1 and lower.isalpha():
    if lower in "aeiou":
        print("it is a vowel")
    else:
        print("it is a consonant")
else:
    print("enter a single valid alphabet")
'''