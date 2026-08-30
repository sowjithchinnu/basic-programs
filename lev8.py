'''
# Write a program to read n elements into an array and print them.
n = int(input("enter the length of the array: "))
arr = []
for i in range(1, n+1):
    num = int(input(f"enter the number {i}: "))
    arr.append(num)
print(arr)

# Write a program to find the sum and average of all elements in an array.
arr = [1, 2, 3, 4, 5]
total = sum(arr)
average = total/len(arr)
print(f"sum => {total}, average => {average}")

# Write a program to find the largest and smallest element in an array.
arr = [31, 52, 13, 49, 35]
n = len(arr)
for i in range(n):
    isSwap = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            isSwap = True
    if not isSwap:
        break
print(f"the smallest element is {arr[0]}")
print(f"the largest element is {arr[-1]}")

# Write a program to count the number of even and odd elements in an array.
arr = [23, 54, 65, 77, 83, 20]
even_count = 0
odd_count = 0
for i in arr:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"even count = {even_count}, odd count = {odd_count}")
'''

# Write a program to search for an element in an array (linear search).
