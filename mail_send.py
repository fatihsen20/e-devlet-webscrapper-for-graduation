import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def send_mail(from_mail, password, to_mail, subject, message):
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(from_mail, password)

        mesaj = MIMEMultipart()
        mesaj["From"] = from_mail  
        mesaj["Subject"] = subject
        mesaj["To"] = to_mail
        body = message

        body_text = MIMEText(body, "plain")
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Mail başarılı bir şekilde gönderildi.")
        mail.close()

    except:
        print("Hata:", sys.exc_info()[0])