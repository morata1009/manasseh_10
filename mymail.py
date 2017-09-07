#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',487)
s.starttls9()
s.login("neymar8971@gmail.com","password123")
message = "hi how r u"
s.sendmail("neymar8971@gmail.com","neymar8971@gmail.com",message)
s.quit() 
