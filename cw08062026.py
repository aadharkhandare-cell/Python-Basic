#Q1 Write a program to check the given number is Amnstrong number
num = int(input("Enter a number: "))
original = num
sum_of_powers = 0
temp = num
digits = 0
while temp > 0:
    digits += 1
    temp //= 10
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if sum_of_powers == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")


#Q2 Write a program to check given no is pelindrome or not

num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print(original, "is a palindrome number.")
else:
    print(original, "is not a palindrome number.")

