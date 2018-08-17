# https://yiyibooks.cn/

import shutil

f1 = open('/etc/passwd', 'rb')
f2 = open('/tmp/abcd', 'wb')
shutil.copyfileobj(f1, f2)
f1.close()
f2.close()
shutil.copyfile('/etc/passwd', '/tmp/xyz')
shutil.copy('/etc/passwd', '/tmp')
shutil.copy('/etc/passwd', '/tmp/aabb')
shutil.copy2('/etc/passwd', '/tmp/aabbcc')
shutil.copytree('/etc/security', '/tmp/anquan')
shutil.rmtree('/tmp/anquan')


import keyword
keyword.kwlist
keyword.iskeyword('pass')





