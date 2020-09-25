# Script for sending email plus attachments to multiple recipients

import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd


gmailUser = os.environ.get('GMAIL_USER')
gmailPass = os.environ.get('GMAIL_PASS')

def send_email(user, pwd, recipient, subject):
    try:
        # Create a sample DataFrame
        d = {'Col1': [1,2], 'Col2': [3,4]}
        df = pd.DataFrame(d)
        df_html = df.to_html()
        dfPart = MIMEText(df_html, 'html')

        # Recipients list
        recipients = ['madnoh@hotmail.sg', 'madnoh@icloud.com']

        # Container
        msg = MIMEMultipart('alternative')

        msg['Subject']= subject
        msg['From'] = user
        msg['To'] = ".".join(recipients)

        msg.attach(dfPart)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, pwd)

        server.sendmail(user, recipients, msg.as_string())
        server.close()

        print('Sent the email')

    except Exception as e:
        print(str(e))
        print('Failed to send email')

send_email(gmailUser, gmailPass, 'madnoh@hotmail.sg', 'Testing 123')