import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.126.com'
mail_user = 'zhangzhigang79@126.com'
mail_pwd = getpass()
message = MIMEText('Python邮件发送测试\n', 'plain', 'utf8')
message['From'] = Header('zhangzhigang79@126.com', 'utf8')
message['To'] = Header('zhangzhigang79@126.com', 'utf8')
message['Subject'] = Header('python 1802 mail test', 'utf8')

sender = 'zhangzhigang79@126.com'
receivers = ['zhangzhigang79@126.com']
smtp_obj = smtplib.SMTP()
smtp_obj.connect(mail_host)
smtp_obj.login(mail_user, mail_pwd)
smtp_obj.sendmail(sender, receivers, message.as_string())
