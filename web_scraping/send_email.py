#!/usr/bin/env python3
import smtplib
import ssl

# Email libraries import
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

G = "\033[92m"
Re = "\033[m"


def send_emial(email_from, password, email_to, subject):
    """send_emial - this function send an emial

    Args:
    """

    # subject = 'Created succesfully.'
    message = MIMEMultipart()
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = subject

    text = "Schedule of class for the day created succesfully."

    part1 = MIMEText(text, 'plain')
    message.attach(part1)

    # text = message.as_string()

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, text)

    print(f'{G}Email Reminder Sent.{Re}')


if __name__ == '__main__':

    email_from = ''
    password = ''
    email_to = ''
    subject = '.'

    send_emial(email_from, password, email_to, subject)
