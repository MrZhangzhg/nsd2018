import shutil

with open('/etc/passwd', 'rb') as sfobj:
    with open('/tmp/mima.txt', 'wb') as dfobj:
        shutil.copyfileobj(sfobj, dfobj) # 拷贝文件对象

shutil.copyfile('/etc/passwd', '/tmp/mima2.txt')
shutil.copy('/etc/shadow', '/tmp/')  # cp /etc/shadow /tmp/
shutil.copy2('/etc/shadow', '/tmp/')  # cp -p /etc/shadow /tmp/
shutil.move('/tmp/mima.txt', '/var/tmp/')  # mv /tmp/mima.txt /var/tmp/
shutil.copytree('/etc/security', '/tmp/anquan') # cp -r /etc/security /tmp/anquan
shutil.rmtree('/tmp/anquan')  # rm -rf /tmp/anquan
# 将mima2.txt的权限设置成与/etc/shadow一样
shutil.copymode('/etc/shadow', '/tmp/mima2.txt')
# 将mima2.txt的元数据设置成与/etc/shadow一样
# 元数据使用stat /etc/shadow查看
shutil.copystat('/etc/shadow', '/tmp/mima2.txt')
shutil.chown('/tmp/mima2.txt', user='zhangsan', group='zhangsan')

