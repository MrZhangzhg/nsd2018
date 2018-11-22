from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(msg, subject, sender, receivers, server, username, password):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = smtplib.SMTP()
    smtp.connect(server, port=25)
    # smtp.starttls()    # 如果服务器要求加密，打开注释
    smtp.login(username, password)
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    msg = 'python internet mail test'
    subject = 'py邮件测试'
    passwd = getpass.getpass()
    inet_mail(msg, subject, sender, receivers, 'smtp.126.com', sender, passwd)
