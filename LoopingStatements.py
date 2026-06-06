#Q1 Write a program to check entered Number id multiple of 7 and 5 using short hand if else

a = int(input("Enter a number: "))
print("Number is multiple of 7 and 5") if a%7==0 and a%5==0 else print("Number is not multiple of 7 and 5")

#Q2 Write a program to print first n natural numbers in decending order 
n = int(input("Enter a number: "))
while n>0 :
    print(n)
    n-=1

#Q3 Write a program to print 2's table in the following format
## 2 * 1 = 2 .....
## 2 * 10 = 20

a=2
b=1
while b<=10:
    print(f"{a} * {b} = {a*b}")
    b+=1

#Q4 Write a progrma to print even numbers upto 100

a=0
while a<=100:
    print(a)
    a+=2

#Q5 Write a program to print addition of first n natural numbers

n=int(input("Enter a number: "))
sum=0
while n>0:
    sum+=n
    n-=1
print(f"Sum of natural numbers is: {sum}")

#Q6 Write a program to print addition of first n even numbers
n=int(input("Enter a number: "))
sum=0
while n>0:
    sum+=2*n
    n-=1
print(f"Sum of first {n} even numbers is: {sum}")

#Q7 Write a program to print A to Z characters 
a=65
while a<=90:
    print(chr(a))
    a+=1

#Q8 Write a program to print Aa to Zz characters
a=65
b=97
while a<=90 and b<=122:
    print(chr(a)+chr(b),end=" ")
    a+=1
    b+=1

#Q9 Write a program to display all numbers which are divisible by 13 and not by 3 between 100 and 500

n = 100
while n<=500 :
    if n%13==0 and n%3!=0 :
        print(n)
    n+=1
#HW...
#Q10 Write a program to find the sum of digits in given number 

n = int(input("Enter a number : "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
print(f"The sum of the number digit is :{sum}")

#Q11 Write a program to enter a number till user wants and at the end it should display sum of all the numbers entered

a=input("Do you wants to enter a Number???(yes/no)")
sum=0
while a=="yes" :
    n=int(input("Enter a Number :"))
    sum+=n
    a=input("Do you wants to enter a Number???(yes/no)")
print("Sum of entered numebers is : ",sum)

