#19/06/20206

# Qrcode 
import qrcode
data = "https://www.google.com"
img = qrcode.make(data)
img.save("qrcode.png")
print("QR Code Generated!")


import qrcode
data = "https://www.google.com"
# create QR object
qr = qrcode.QRCode()
qr.add_data(data)
qr.make()
# print in terminal
qr.print_ascii()
# create image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("QR Code Generated!")

#To send the email using python code

import smtplib
from email.message import EmailMessage
mg=EmailMessage()
mg["Subject"]="python test mail"
mg["From"]="aadharkhandare@gmail.com"
mg["To"]="khandareapoorv@gmail.com"

mg.set_content("first demo mail")

#connet the python program to server
server=smtplib.SMTP("smtp.gmail.com")
server.starttls()

email="aadharkhandare@gmail.com"
password ="fmlj opej chyo optg"

server.login(email,password)
server.send_message(mg)
print("connected")