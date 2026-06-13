#10/06/2026
#Q1 Write a program to take string from user and iterate using for loop, with range function and whilw loop
# Using for loop
s = input("Enter a string: ")
for i in s:
    print(i,end="")
print()
    
# Using for loop with range()
s = input("Enter a string: ")
for i in range(len(s)):
    print(s[i],end="")
print()
 
# Using while loop
s = input("Enter a string: ")
i = 0
while i < len(s):
    print(s[i],end="")
    i += 1
print()

#Q2 Write a program to take a string from user and check  given string is palindrome or not
s = input("Enter a string: ")
reverse_s = s[::-1]
if s == reverse_s:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    

#Q3 Write a program to check both string are anagram or not
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
