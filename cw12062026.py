#12/06/2026

#Q1 Write a Python program to
#Declare a list of integers.
#Declare a list of floating point numbers.
#Create a new list containing only positive numbers from the integer list.
#Create another list containing numbers divisible by 3 from the integer list using list comprehension.
l=[-4,-3,-2,-1,0,1,2,3,4,5]
l1=[1.1,2.2,3.3]
l3=[]
for i in l:
    if i>0:
        l3.append(i)
print(l)
print(l1)
print(l3)
l2=[i for i in l if i%3==0]
print(l2)

#Q2 Write aprogram to a take list from the user
numbers = []
n = int(input("How many elements do you want to enter? "))
for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)
print("List is:", numbers)

#Q3 Write a Python program to separate even and odd numbers from a given list into two different lists.
L=[1,2,10,3,4,5]
l=[i for i in L if i%2==0]   
l1=[i for i in L if i%2==1]  

print(l)
print(l1)

#Q4 Write a Python program to rotate a list to the right by one position.
l=[1,10,2,4]
for i in l:
	print(l[-1:]+l[:-1])
	break

#Q5 Write a program to create a new tuple contain the multiple of 7 from the given tuple
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
t7 = []
for i in t:
    if i % 7 == 0:
        t7.append(i)
t7 = tuple(t7)
print(t7)

