#16/06/2026
#write a function that accepts a number and check weather its perfect number or not
def perfect(n):
	sum=0
	for i in range(1,n):
		if n%i==0:
			sum+=i
	if sum==n:
		print("perfect no")
	else:
		print("not perfect no")
perfect(10)

print()

#write a program in which function accepts a list having even number of elements and swap the element and adjacent position
def f1(l):
	for i in range(0,len(l),2):
		l[i],l[i+1]=l[i+1],l[i]
	print(l)

l=[1,2,3,4,5,6]
if (len(l)%2==0):
	f1(l)
else:
	print("no even element")

print()

#write a program to count uppercase letter, lowercas letter, special symbols digits in given string using user define function
def count_characters(s):
    upper = lower = digit = special = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        else:
            special += 1

    print("Uppercase letters :", upper)
    print("Lowercase letters :", lower)
    print("Digits            :", digit)
    print("Special symbols   :", special)

s = input("Enter a string: ")
count_characters(s)

print()


'''Science={'Adhar','Apoorv','Omkar','Tushar','Shree'}
Arts={'Rushikesh','Adhar','Om','Kartik'}
Commerce={'Pratham','Adhar','Om','Ram'}
while True:
	for i in Science:
			print(i,end=", ")
	for i in Arts:
			print(i,end=", ")
	for i in Commerce:
			print(i,end=", ")'''
            
            