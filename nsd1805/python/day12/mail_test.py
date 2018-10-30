from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

message = MIMEText('这是一封发往本地的测试邮件\n', 'plain', 'utf8')
message['From'] = Header('root@tedu.cn', 'utf8')
message['To'] = Header('bob', 'utf8')
message['Subject'] = Header('测试邮件', 'utf8')

smtp = SMTP('127.0.0.1')
sender = 'root@tedu.cn'
receivers = ['bob', 'alice']
smtp.sendmail(sender, receivers, message.as_string())
