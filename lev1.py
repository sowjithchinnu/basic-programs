'''
# Write a program to print "Hello, World!" on the screen.
print("Hello, World!")

# Write a program to read two numbers and print their sum.
a = float(input("enter a number: "))
b = float(input("enter another number: "))
print("the sum is: ", a+b)

# Write a program to read two numbers and print their sum, difference, product and quotient.
a = float(input("enter a number: "))
b = float(input("enter another number: "))
sum = a+b
difference = a-b
product = a*b
quotient = a/b
print(sum, difference, product, quotient)

# Write a program to read the radius of a circle and print its area and circumference.
import math
radius = float(input("enter the radius: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius
print(area, circumference)

# Write a program to read the length and breadth of a rectangle and print its area and perimeter.
length = float(input("enter the length of the rectangle: "))
breadth = float(input("enter the breadth of the rectangle: "))
area = length*breadth
perimeter = 2*(length + breadth)
print(f"the area and the perimeter of the rectangle with length {length} and breadth {breadth} are {area}, {perimeter}")

# Write a program to swap two numbers using a third variable.
a = 45
b = 22
swap = a
a = b
b = swap
print(a, b)

# Write a program to swap two numbers without using a third variable.
a = 80
b = 71
a, b = b, a
print(a, b)

# Write a program to read a temperature in Celsius and convert it to Fahrenheit.
Celsius = float(input("enter the tempertature in celsius: "))
Fahrenheit = (Celsius * 1.8) + 32
print(f" the Celsius {Celsius} when converted into  Fahrenheit is {Fahrenheit}")

# Write a program to read the marks of 5 subjects and print the total and average.
maths = float(input("enter your math marks: "))
science = float(input("enter your science marks: "))
english = float(input("enter your english marks: "))
social = float(input("enter your social marks: "))
hindi = float(input("enter your hindi marks: "))
total = maths + science + english + social + hindi
average = total/5
print(f"the total of the 5 subjects is {total}, and the average is {average}")
'''

# Write a program to read seconds and convert them into hours, minutes and seconds.
total_seconds = int(input("enter the number of seconds: "))
remaining_seconds = total_seconds % 3600
hours = total_seconds // 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f" {total_seconds} seconds is equal to, {hours} hours {minutes} minutes and {seconds} seconds.")