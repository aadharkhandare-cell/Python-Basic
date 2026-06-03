#25/05/2026

#Q1. Write a Python program to print to print information of student 
print("Name: Adhar Khandare")
print("Age : 19")
print("Course : Python")
print("College : GP Ahilynagar")

#Q2. Write a Python program to print "hello" and "world" on the same line
print("hello",end="@@")
print("world")

#Q3
print("Welcome to Python!")
print('"Python" is very (easy)')

#Q4
a=10
b=20
print("value of a= ",a,"and value of b= ",b)
print(f"value of a= {a} and value of b = {b}")

#Q5. Write a Python program to swap two variables
a,b=10,20
a,b=b,a
print(a,b)

#Q6. Write a Python program to find the square of a number
a=10
print("Square of no. is :",a**2)

#Q7. Write a Python program to find the area of a rectangle
l=10
b=20
print("Area of rectangle : ",l*b)

#Q8. Write a Python program to find the area of a triangle
b=10
h=20
print("Area of triangle : ",1/2*b*h)

#Q9. Write a Python program to take 2 no. from user 
#and perform basic arithmetic operators
a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)
print("Modulus : ",a%b)
print("Exponent : ",a**b)
print("Floor Division : ",a//b)

#Q10. Write a Python program to take 3 no. from user and find their double and then their average
a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
c=int(input("Enter third no. : "))
a=a*2
b=b*2
c=c*2
print("Average of double of 3 no. is : ",(a+b+c)/3)

#Q11. Write a Python program to take doller fron user and convert into Rupees
amount=int(input("Enter amount in doller"))
inr = amount*97.4
print("inr")

#Q12. Write a Python program to calculate addition of 2 complex numbers
a=2+3j
b=4+5j
c=a+b
print("Addition of 2 complex no. is : ",c)
print("real part is : ",c.real)
print("imaginary part is : ",c.imag)

#02/06/2026
#Q1. Write a Python program to take 2 numbers from user and convert them into integer
a=input("Enter first no. : ")
b=input("Enter second no. : ")
a=int(a)
b=int(b)
print("a= ",a,"b= ",b)

#Q2. Write a Python program to convert celcius to fahrenheit and fehrenheit to celcius
c=int(input("Enter temperature in celcius : "))
f=(c*9/5)+32
print("Temperature in fahrenheit : ",f)
f=int(input("Enter temperature in fahrenheit : "))
c=(f-32)*5/9

#Q3. Write a program to swap two numbers with using bitwise operator
a=10
b=20
a=a^b
b=a^b
a=a^b
print("a= ",a,"b= ",b)

#Q4. Write a Python program to take 2 numbers from user and shift the first number by the second #number to left

a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
print("Left shift : ",a<<b)

#03/06/2026
#Q1.write a Python program to print single quote 
print("''")

#Q2. Write a Python program to calculate the addition, subtraction, multiplication and division of #two complex numbers
a=2+3j
b=1+10j
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)

#Q3. Write a Python program to check 2 object reference same memory location or not
a=10
b=10
print(a is b)
print(a is not b)
#For reference of same memory location we can use id() function
print(id(a))
print(id(b))

#Q4. Write a Python program to take sudent name from user and asingle charecter from user .Check #that a charecter is present in student name or not
n=input("Enter student name : ")
chr=input("Enter a single charecter : ")
if chr in n:
    print("charecter is present")
else:
    print("charecter is not present")

#Q5. Write a Python program to check enterd number is multiple of 5 or not
a=int(input("Enter a number : "))
if a%5==0:
    print("number is multiple of 5")
else:
    print("number is not multiple of 5")

#Q6. Write a Python program to check given number  is positive or not

a=int(input("Enter a number : "))
if a>0:
    print("number is positive")
else:
    print("number is negative")

#Q7. Write a Python program to take selling price and cost price from user and check if user is #profit or loss
a=int(input("Enter selling price : "))
b=int(input("Enter cost price : "))
if a>b:
    print("profit") 
else:
    print("loss")

#Q8. Write a Python program to to check given shape is square or rectangle
a=int(input("Enter length :"))
b=int(input("Enter breadth :"))
if a==b:
    print("shape is square")
else:
    print("shape is rectangle")

#Q9. Write a Python program to check given number is multiple of 3 or 5
a=int(input("Enter a number : "))
if a%3==0 and a%5==0:
    print("number is multiple of 3 and 5")
else:
    print("number is not multiple of 3 and 5")

#Q10. Write a Python program to get output as 
#1 - 1
#2 - 4
#3 - 9
#4 - 16
#5 - 25
print("1 - ",1**2)
print("2 - ",2**2) 
print("3 - ",3**2)
print("4 - ",4**2)
print("5 - ",5**2)






