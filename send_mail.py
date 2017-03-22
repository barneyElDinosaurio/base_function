#-*-coding=utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from toolkit import Toolkit
def send_139():
    cfg=Toolkit.getUserData('data.cfg')
    sender=cfg['mail_user']
    passwd=cfg['mail_pass']
    receiver=cfg['receiver']
    msg=MIMEText('Python mail test','plain','utf-8')
    msg['From']=Header('FromTest','utf-8')
    msg['To']=Header('ToTest','utf-8')
    subject='Python SMTP Test'
    msg['Subject']=Header(subject,'utf-8')
    try:
        obj=smtplib.SMTP()
        obj.connect('smtp.126.com',25)
        obj.login(sender,passwd)
        obj.sendmail(sender,receiver,msg.as_string())
    except smtplib.SMTPException,e:
        print e

send_139()
