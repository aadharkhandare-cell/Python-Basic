#11/06/2026
#Q1 Write a program to count a number of alphabets,digits, special symbols in given string
#and also calculate uppercase and lowercase letters
s = input("Enter a String: ")
A=0
S=0
D=0
U=0
L=0
for i in s:
	if i.isalpha():
		A+=1
		if i.isupper():
			U+=1
		else:
			L+=1
	elif i.isdigit():
		D+=1
	else:
		S+=1
print("No of Uppercase Alphabets: ",U)
print("No. of Lowercase alphabets: ",L)
print("No. of Alphabets: ",A)
print("No of special symbols: ",S)
print("No. of digits: ",D)

#Q2 Write a program to take two string from user 
#if both string are equal then convert into uppercase and replace them
#if they are not equal then covert into lowercase and join 1st string with 2nd string
S1 = input("Enter 1st string: ")
S2 = input("Enter 2nd string: ")

if S1 == S2:
    S1 = S1.upper()
    S2 = S2.upper()
    print("Strings are equal")
    print(S1)
    print(S2)
else:
    S1 = S1.lower()
    S2 = S2.lower()
    result = S1 + S2
    print("Strings are not equal")
    print(result)

#Q3 Write program to declare list of integer.Now declare list of flotting point numbers.
#Creat a new list from list of integer which contains only positive numbers
l1 = [10, -5, 23, -8, 0, 15, -2]
l2 = [2.5, -3.4, 6.7, 0.0, -1.2]
positive_list = []
for i in l1:
    if i > 0:
        positive_list.append(i)

print("Integer List:", l1)
print("Floating List:", l2)
print("Positive Numbers List:", positive_list)

#Q4 Write a program to check entered number is in list or not
l = [10, 25, 30, 45, 50]
num = int(input("Enter a number to check: "))
if num in l:
    print("Number is present in the list.")
else:
    print("Number is not present in the list.")

	