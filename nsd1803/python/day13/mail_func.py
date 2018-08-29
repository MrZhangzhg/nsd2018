from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

def send_msg(sender, receivers, subject, msg):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = SMTP('127.0.0.1')
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    sender = 'zzg@tedu.cn'
    receivers = ['root@localhost', 'zhangsan@localhost']
    subject = '邮件测试'
    msg = 'Python邮件测试\r\n'
    send_msg(sender, receivers, subject, msg)
