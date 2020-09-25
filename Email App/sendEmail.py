# Script for sending text email to a single recipient

import smtplib, os
from email.mime.text import MIMEText

gmailUser = os.environ.get('GMAIL_USER')
gmailPass = os.environ.get('GMAIL_PASS')

def send_email(user, pwd, recipient, subject):
    try:
        msg = "This is a test email"
        msg = MIMEText(msg)
        msg['Subject']= subject
        msg['From'] = user
        msg['To'] = recipient

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, pwd)

        server.sendmail(user, recipient, msg.as_string())
        server.close()

        print('Sent the email')

    except Exception as e:
        print(str(e))
        print('Failed to send email')

send_email(gmailUser, gmailPass, 'madnoh@hotmail.sg', 'Testing 123')