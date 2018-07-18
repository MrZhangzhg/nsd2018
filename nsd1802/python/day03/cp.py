f1 = open('/bin/ls', 'rb')
f2 = open('/root/ls', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
