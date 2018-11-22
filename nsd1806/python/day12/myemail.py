from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 邮件正文，纯文本，字符编码
message = MIMEText('python邮件发送测试\n', 'plain', 'utf8')
message['From'] = Header('zzg@tedu.cn', 'utf8')  # 收件人
message['To'] = Header('zhangzhigang79@126.com', 'utf8')  # 发件人
message['Subject'] = Header('测试邮件', 'utf8')   # 主题
smtp = smtplib.SMTP('localhost')    # 本机作为邮件服务器发送邮件
sender = 'zzg@tedu.cn'   # 发件人
receivers = ['zhangzhigang79@126.com','root@localhost']  # 收件人列表
smtp.sendmail(sender, receivers, message.as_string())
