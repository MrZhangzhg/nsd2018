from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP
import getpass

def send_msg(host, pwd, sender, receivers, subject, msg):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = SMTP(host)
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    host = 'smtp.126.com'
    pwd = getpass.getpass()
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    subject = '邮件测试'
    msg = 'Python邮件测试\r\n'
    send_msg(host, pwd, sender, receivers, subject, msg)
