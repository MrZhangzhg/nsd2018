import getpass
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP


def send_msg(msg, sender, receivers, subject, host, pwd):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = SMTP()
    smtp.connect(host)
    # smtp.starttls()  # 如果服务器要求安全传输，取消此行注释
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    msg = 'NSD1805发邮件测试\n'
    subject = '互联网邮件测试'
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    host = 'smtp.126.com'
    pwd = getpass.getpass()
    send_msg(msg, sender, receivers, subject, host, pwd)
