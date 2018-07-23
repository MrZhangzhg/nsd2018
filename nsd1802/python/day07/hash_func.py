# 加密：对称加密、非对称加密、单向加密
# 单向加密：加密只能向一个方向进行，相同的数据总是得到相同的“乱码”
# 不能根据结果回推源。用途：文件完整性校验、加密密码
import hashlib

f = open('/etc/passwd', 'rb')
data = f.read()
f.close()

m = hashlib.md5(data)
print(m.hexdigest())

# m = hashlib.md5()
# m.update(data)  # 每次读取一部分文件内容，更新至m对象
#

