#04/06/2026

#Q1. Write a program to find Maximum between given 3 numbers

a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
c=int(input("Enter third no. : "))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")

#Q2. Write a program to check given year is leap year or not

y=int(input("Enter a year : "))
if ( y%4==0 and y%100!=0) or y%400==0 :
    print("Leap year")
else:
    print("Not a leap year")

#Q3. Write a program to calculate discount on price 
#If price is greater than 5000 and less than 10000 then disciunt will be 5%
#If price is greater than 10000 and less than 15000 then discount will be 10%
#If price is greater than 50000 then the discount will be 20%
#else no discount
#Print Final price after discount

p=int(input("Enter price : "))
if p>5000 and p<10000:
    print("Final price after discount : ",p-(p*5/100))
elif p>10000 and p<15000:
    print("Final price after discount : ",p-(p*10/100))
elif p>50000:
    print("Final price after discount : ",p-(p*20/100))
else:
    print("No discount")
    
#Q4. Write a program to calculate electricity bill based on following conditions
#If units in between 0 to 100 then 2 Rupees per unit
#If units in between 100 to 250 then 4 Rupees per unit
#If units are above 250 then 6 Rupees per unit
#Take current reading and last reading from user and calculate total bill and Print Current unit,last unit,total unit and total bill

c=int(input("Enter current reading : "))
l=int(input("Enter last reading : "))
u=c-l
if c>0 and c<100 and c>l:
    print("Current unit : ",c)
    print("Last unit : ",l)
    print("unit are : ",u)
    print(" bill is : ",u*2)
elif c>100 and c<250 and c>l:
    print("Current unit : ",c)
    print("Last unit : ",l)
    print("unit are : ",u)
    print(" bill is : ",u*4)
elif c>250 and c>l:
    print("Current unit : ",c)
    print("Last unit : ",l)
    print("unit are : ",u)
    print(" bill is : ",u*6)
else:
    print("Current unit must be greater than last unit!!! ")

#Q5. Write a program find discount depend on the following conditions
#If festival sell is on then 30% discount and if user having membership then 20% discount 
#If festival sell is off and if user having membership and cart value is greater than 5000 then 20% dicount 
#If user having memberdhip and cart value is less than 5000 then 10% discount 
#if user does not have membership then no discount

f=input("Is festival sell is (on/off)) : ")
m=input("Do you have membership (yes/no) : ")
c=int(input("Enter cart value : "))
if f=="on":
    print("Discount is : ",c*30/100)
    if m=="yes":
        print("Discount is :",c*20/100)
elif f=="off" and m=="yes" and c>5000:
    print("Discount is : ",c*20/100)
elif f=="off" and m=="yes" and c<5000:  
    print("Discount is : ",c*10/100)
else:    
    print("No discount")

#Q6. Write a program to allow online exam access only if student is registered, fee is paid, system time is within window
#If student is not regester then access denied
#if student is register and fee is not paid then access is denied
#If fee is paid and time is valid then exam started otherwise exam not startes

r=input("Are you registered (yes/no) : ")
if r=="no":
    print("Access denied")
else:
    f=input("Is fee paid (yes/no) : ")
    if f=="no":
        print("Access denied")
    else:
        t=int(input("Enter system time in 24 hr format : "))
        if t>=9 and t<=17:
            print("Exam started")
        else:
            print("Exam not started")

