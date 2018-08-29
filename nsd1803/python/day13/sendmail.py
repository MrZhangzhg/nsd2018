from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

# plain表示纯文本文件
message = MIMEText('Python邮件测试\r\n', 'plain', 'utf8')
message['From'] = Header('zzg', 'utf8')  # 头部中的发件人
message['To'] = Header('root', 'utf8')  # 头部中的收件人
message['Subject'] = Header('邮件测试', 'utf8')  # 头部中的主题
sender = 'zzg@tedu.cn'  # 发件人
receivers = ['root@localhost', 'zhangsan@localhost']  # 收件人列表
smtp = SMTP('127.0.0.1')  # 创建SMTP对象
smtp.sendmail(sender, receivers, message.as_string())  # 发送邮件
