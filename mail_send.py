import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def send_mail(from_mail, password, to_mail, subject, message_):
    """
    This function sends mail.

    Args:
        from_mail (str): Sender mail address.
        password (str): Sender mail password.
        to_mail (str): Receiver mail address.
        subject (str): Mail subject.
        message_ (str): Mail message.
    """
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(from_mail, password)

        message = MIMEMultipart()
        message["From"] = from_mail  
        message["Subject"] = subject
        message["To"] = to_mail
        body = message_

        body_text = MIMEText(body, "plain")
        message.attach(body_text)

        mail.sendmail(message["From"], message["To"], message.as_string())
        print("Mail delivery is successful.")
        mail.close()

    except:
        print("Exception:", sys.exc_info()[0])