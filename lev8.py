# Write a program to read n elements into an array and print them.
n = int(input("enter the length of the array: "))
arr = []
for i in range(1, n+1):
    num = int(input(f"enter the number {i}: "))
    arr.append(num)
print(arr)