'''
# Write a program to find the length of a string without using an inbuilt function.
string = input("enter a string: ")
count = 0
for char in string:
    count += 1
print(count)

# Write a program to count the number of vowels and consonants in a string.
string = str(input("enter a string: "))
vowels = 0
consonants = 0
for char in string:
    if char.isalpha():
        if char in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
print(f"the number of vowels and consonants in the string are {vowels} and {consonants}")

# Write a program to count the number of words in a sentence.
string = str(input("enter a sentence: "))
words = string.split()
length = len(words)
print(length)

#  Write a program to reverse a string.
string = str(input("enter a string: "))
rev_str = string[::-1]
print(rev_str)

# Write a program to check whether a string is a palindrome.
string = str(input("enter a string: "))
rev_str = string[::-1]
if rev_str == string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
    
# Write a program to convert a string to uppercase and lowercase without inbuilt case functions.
string = str(input("enter a string: "))
upper = ""
lower = ""
for char in string:
    if 'a' <= char <= 'z':
        upper += chr(ord(char) - 32)
    else:
        upper += char
    if 'A' <= char <= 'Z':
        lower += chr(ord(char) + 32)
    else:
        lower += char
print('Uppercase: ', upper)
print('Lowercase: ', lower)

# Write a program to count the frequency of each character in a string.
string = input("enter a string: ")
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1
for char, count in freq.items():
    print(f"{char} -> {count}")

# Write a program to remove all spaces from a string.
string = input("enter a string: ")
no_space = string.replace(" ", "")
print(no_space)

# Write a program to check whether two strings are anagrams of each other.
first = input("enter a string: ").lower()
second = input("enter another string: ").lower()
if sorted(first) == sorted(second):
    print("they are Anagrams")
else:
    print("not Anagrams")

# Write a program to find the first non-repeating character in a string.
string = input("enter a string: ")
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1
found = False
for char in string:
    if freq[char] == 1:
        print(f"the first non-repeating character is {char}")
        found = True
        break
if not found:
    print("no non-repeating character")
'''