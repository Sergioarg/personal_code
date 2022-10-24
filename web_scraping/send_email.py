import smtplib

from email.mime.text import MIMEText



def send_emial(textfile):
    """send_emial - this function send an emial

    Args:
        text_file (str): text to send to email
    """
    with open(textfile, 'rb') as fb:
        # Create text/plain message
        msg = MIMEText(fb.read)

    me = 'sergio_ramos63@yahoo.com'
    you = 'est.sramos227@smart.edu.co'

    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()
