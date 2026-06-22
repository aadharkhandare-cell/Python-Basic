import random
import smtplib
import time
import uuid
from datetime import datetime
from email.message import EmailMessage
import qrcode

SENDER_EMAIL = "aadharkhandare@gmail.com"
APP_PASSWORD = "fmlj opej chyo optg"

user_email = input("Enter Email: ")

otp = str(random.randint(100000, 999999))

msg = EmailMessage()
msg["Subject"] = "OTP Verification"
msg["From"] = SENDER_EMAIL
msg["To"] = user_email
msg.set_content(f"Your OTP is {otp}. It is valid for 2 minutes.")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, APP_PASSWORD)
server.send_message(msg)
server.quit()

print("OTP Sent Successfully!")

start_time = time.time()

attempt = 1
verified = False

while attempt <= 3:

    entered_otp = input("Enter OTP: ")

    if time.time() - start_time > 120:
        print("OTP Expired!")
        break

    if entered_otp == otp:
        verified = True
        break

    print("Incorrect OTP")
    print("Attempts Left:", 3 - attempt)

    attempt += 1

if verified:

    session_id = "SID" + str(uuid.uuid4())[:8]

    login_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    status = "Active"

    qr_data = f"""
Session ID : {session_id}
Email : {user_email}
Login Time : {login_time}
Status : {status}
"""

    img = qrcode.make(qr_data)

    file_name = "/storage/emulated/0/Download/" + session_id + ".png"
    img.save(file_name)

    print("\nLogin Successful")
    print("Session ID:", session_id)
    print("QR Code Saved In Download Folder")
    print(file_name)

else:
    print("\nLogin Failed")