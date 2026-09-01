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

# Write a program to search for an element in an array (linear search).
arr = [12, 343, 32, 65, 32, 2, 87, 964, 45]
search = int(input("enter a number: "))
for temp in arr:
    if search == temp:
        print(f"{search} found")
        break
    print(f"no {search}")

# Write a program to reverse the elements of an array.
arr = [12, 343, 32, 65, 32, 2, 87, 964, 45]
rev = list(reversed(arr))
print(rev)

# Write a program to find the second largest element in an array.
arr = [12, 343, 32, 65, 32, 2, 87, 964, 45]
sort = sorted(set(arr))
sec_largest = sort[-2]
print(sec_largest)

# Write a program to count the frequency of each element in an array.
from collections import Counter
arr = [12, 343, 32, 65, 32, 2, 87, 964, 45]
freq = Counter(arr)
for element, count in freq.items():
    print(f"element {element} -> count:{count}")

# Write a program to remove duplicate elements from an array.
arr = [12, 343, 32, 65, 32, 2, 87, 964, 45]
seen = []
for i in arr:
    if i not in seen:
        seen.append(i)
print(seen)

# Write a program to sort an array in ascending order (bubble sort).
arr = [12, 343, 32, 65, 32, 2, 87, 964, 45]
n = len(arr)
for i in range(n):
    isSwap = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            isSwap = True
    if not isSwap:
        break
print(arr)

# Write a program to merge two arrays into one.
arr_1 = [9, 5, 4, 2]
arr_2 = [33, 1, 6, 8]
merge = arr_1 + arr_2
print(merge)

# Write a program to find the sum of all even-indexed and odd-indexed elements separately.
arr = [1, 2, 3, 4]
n = len(arr)
even_index = 0
odd_index = 0
for i in range(n):
    if i%2==0:
        even_index += arr[i]
    else:
        odd_index += arr[i]
print(f"sum of even indices is {even_index}")
print(f"sum of odd indices is {odd_index}")
'''