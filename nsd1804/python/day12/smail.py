import smtplib   # 相当于邮件服务器的客户端
from email.mime.text import MIMEText  # 用于编写邮件正文
from email.header import Header   # 用于编写邮件的头部

msg = MIMEText('Python发送邮件测试\n', 'plain', 'utf8')  # plain表示纯文本
msg['From'] = Header('root', 'utf8')
msg['To'] = Header('zhangsan', 'utf8')
msg['Subject'] = Header('py email test', 'utf8')
sender = 'root'  # 发件人是本地的root
receivers = ['zhangsan', 'root']   # 收件人可以是多个
smtp_obj = smtplib.SMTP('localhost')   # 指定使用本机作为邮件服务器
smtp_obj.sendmail(sender, receivers, msg.as_string())
