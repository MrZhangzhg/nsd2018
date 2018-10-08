import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header

def send_mail(server, user, pwd, sender, receivers, msg):
    smtp_obj = smtplib.SMTP()
    # smtp_obj.starttls()
    smtp_obj.connect(server, 25)
    smtp_obj.login(user, pwd)
    smtp_obj.sendmail(sender, receivers, msg.as_string())

if __name__ == '__main__':
    msg = MIMEText('Python发送邮件测试\n', 'plain', 'utf8')
    msg['From'] = Header('zhangzg', 'utf8')
    msg['To'] = Header('zhangzhigang', 'utf8')
    msg['Subject'] = Header('py email test', 'utf8')
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    passwd = getpass.getpass()
    send_mail('smtp.126.com', sender, passwd, sender, receivers, msg)
