#16/06/2026
#function with no arrgument
def fun():
	return 10+20,2*3
print(fun())
a,b=fun()
print(a,b)

#function with arrgument
def f1(a,b):
	return a**b
print(f1(2,3))
a=f1(2,3)
print(a)

#function with variable length arrguments
def f2(*a):
	print(sum(a))
	print(a[0])
f2(1,2,3)
f2(10,20,30,40)
f2(35)

#function with positional arrguments
def f3(x,y):
	print(x,y)
f3(y=10,x=20)

#function with keyword arrguments
def f4(**kargs):
	print(kargs)
	print(len(kargs))
f4(x=10,y=20,z=30)
f4(a=1,b=2)
f4(n=100)

#function with call by value
def f5(x,y):
	print(x,y)
	x=100
	y=200
	print(x,y)
f5(10,20)
x=1
y=2
print(x,y)
x+=3
print(x,y)

def f6(x,y):
	x,y=y,x
	print(x,y)
x=10
y=20
f6(x,y)
print(x,y)

def f7(l):
	l[0]=100
l=[1,2,3]
f7(l)
print(l)

#Write a function that accepts a number and check weather its perfect number or not
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

#Write a program in which function accepts a list having even number of elements and swap the element and adjacent position
def f1(l):
	for i in range(0,len(l),2):
		l[i],l[i+1]=l[i+1],l[i]
	print(l)

l=[1,2,3,4,5,6]
if (len(l%2==0)):
	f1()
else:
	print("no even element")

#Write a program to count uppercase letter, lowercas letter, special symbols digits in given string using user define function
def count_upper(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    return count

def count_lower(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    return count

def count_digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    return count

def count_special(s):
    count = 0
    for ch in s:
        if not ch.isalnum() and not ch.isspace():
            count += 1
    return count

# Main Program
string = input("Enter a string: ")

print("Uppercase letters =", count_upper(string))
print("Lowercase letters =", count_lower(string))
print("Digits =", count_digits(string))
print("Special symbols =", count_special(string))