
import smtplib

from .config import *

def send_mail(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        gstat = server.ehlo()
        print(gstat)
        server.starttls()
        server.login(EMAIL,PASSWORD)

        message = 'Subject: {}  {}'.format(subject, msg)
        server.sendmail(EMAIL,EMAIL,message)
        server.quit()
        print("Email sent successfully!!!!")

    except:
        print("Error in sending your email ...")


subject = "test email from python"
msg = "Hello World!!"

send_mail(subject,msg)