# -*-coding=utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from toolkit import Toolkit
from email.mime.multipart import MIMEMultipart
from email import Encoders, Utils


class MailAtt():
    def __init__(self, smtp_server, from_mail, password, to_mail):
        self.server = smtp_server
        self.username = from_mail.split("@")[0]
        self.from_mail = from_mail
        self.password = password
        self.to_mail = to_mail

        # 初始化邮箱设置

    def send_txt(self, filename):
        # 这里发送附件尤其要注意字符编码，当时调试了挺久的，因为收到的文件总是乱码
        self.smtp = smtplib.SMTP_SSL(port=465)
        self.smtp.connect(self.server)
        self.smtp.login(self.username, self.password)
        #self.msg = MIMEMultipart()
        self.msg = MIMEText("content", 'plain', 'utf-8')
        self.msg['to'] = self.to_mail
        self.msg['from'] = self.from_mail
        self.msg['Subject'] = "459"
        self.filename = filename + ".txt"
        self.msg['Date'] = Utils.formatdate(localtime=1)
        content = open(self.filename.decode('utf-8'), 'rb').read()
        # print(content)
        #self.att = MIMEText(content, 'base64', 'utf-8')
        #self.att['Content-Type'] = 'application/octet-stream'
        # self.att["Content-Disposition"] = "attachment;filename=\"%s\"" %(self.filename.encode('gb2312'))
        #self.att["Content-Disposition"] = "attachment;filename=\"%s\"" % Header(self.filename, 'gb2312')
        # print(self.att["Content-Disposition"])
        #self.msg.attach(self.att)

        #self.smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())
        self.smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())
        self.smtp.quit()


def send_139():
    cfg = Toolkit.getUserData('data.cfg')
    sender = cfg['mail_user']
    passwd = cfg['mail_pass']
    receiver = cfg['receiver']
    msg = MIMEText('Python mail test', 'plain', 'utf-8')
    msg['From'] = Header('FromTest', 'utf-8')
    msg['To'] = Header('ToTest', 'utf-8')
    subject = 'Python SMTP Test'
    msg['Subject'] = Header(subject, 'utf-8')
    try:
        obj = smtplib.SMTP()
        obj.connect('smtp.126.com', 25)
        obj.login(sender, passwd)
        obj.sendmail(sender, receiver, msg.as_string())
    except smtplib.SMTPException as e:
        print(e)


def main():
    obj = MailAtt('info')
    obj.send_txt('html')

#send_139()
main()

