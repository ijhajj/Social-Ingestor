import traceback
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = 'i.jhajj@gmail.com'
gmail_pwd = 'Ip@Tarun2005'
to = 'aneya@ilandingvw.com'

def send_email(to, subject, text, html, **kwargs):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = gmail_user
        msg['To'] = to

        if kwargs.get('cc', None):
            msg['Cc'] = ','.join(kwargs.get('cc'))

        if kwargs.get('bcc', None):
            msg['Bcc'] = ','.join(kwargs.get('bcc'))
        msg['Subject'] = subject

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(text, 'html')

        msg.attach(part1)
        msg.attach(part2)

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()

    except Exception as e:
        traceback.print_exc()

#create the body of message (a plain text and an HTML version)
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.milkbasket.com"
html = """\
<html>
    <head></head>
    <body>
    <p>Hi<br>
    How are you?<br>
    Here is the <a href="http://www.bookmyshow.com">link</a> you wanted
    </p>
    </body>
</html>
"""

send_email(to, "<subject>", text, html, **{})
#send_email(to, "<subject>", text, html, **{'cc':[to],'bcc':[to]})
