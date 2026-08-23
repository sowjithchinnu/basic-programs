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
'''
