#!/usr/bin/python3  
import smtplib  
sender_mail = 'swaroopmanchala9@gmail.com'  
receivers_mail = ['swaroopmanchala9@gmail.com']  
message = """From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message. Run in loop for 10 times
"""%(sender_mail,receivers_mail)

for i in range(0,1):
    try:
        password = "FKo@LcbY399"
        smtpObj = smtplib.SMTP('gmail.com',587)
        smtpobj.login(sender_mail,password)
        smtpObj.sendmail(sender_mail, receivers_mail, message)
        print("Successfully sent email")  
    except Exception:
        print("Error: unable to send email")  
