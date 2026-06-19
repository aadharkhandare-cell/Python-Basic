#Write a program to create a class student with instance variable student name, student ID, student mo no .Accept and print the details for one student
class student():
	def accept(self):
		self.name="abc"
		self.id=12
		self.number=1234567890
	def display(self):
		print(self.name,self.id,self.number)
s=student()
s.accept()
s.display()

#write a program to create a class custumer with cusromer id , costumer name, costumer emailid,mo no.Used constructor to initialize instance variable and print detail

class customer():
	def __init__(self):
		self.name="Adhar"
		self.id=50
		self.email="adhar@gmail.com"
		self.number=1010101010
	def display(self):
		print(self.name,self.id,self.email,self.number)
c1=customer()
c1.display()

#Write a program computer generate random number between 1 to 100.the user has to guise the no the program should give hits like to high and to low until correct guies is mate

import random
a = random.randint(1,100)
while True:
    n = int(input("Enter a number: "))
    if n == a:
        print("You guessed the correct number!")
        break
    elif n > a:
        print("Too high! Try a smaller number.")
    else:
        print("Too low! Try a greater number.")
			
            
#Write a program to create a secured password of user defined length .The password must content atleast uppercase letter ,lowercase letter ,one digit and one special.caracter . The remaining charecter should be selected randomly and print the final password
import random
import string
length = int(input("Enter password length: "))
if length < 4:
    print("Password length must be at least 4")
else:
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    all_chars = upper + lower + digits + special
    for i in range(length - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    final_password = "".join(password)
    print("Generated Password:", final_password)
    
    