# 导入自己编写的模块，可以把自己编写的模块放到/usr/local/lib/python3.6/site-packages
# 还可以设置环境变量PYTHONPATH，指向自己所写模块的路径
# 如果模块文件在一个目录中，可以把目录当作包
# mkdir rrr
# cp railway rrr/
# python3
# >>> import rrr.railway
# md5值：一种hash哈希算法，单向加密，相同的数据生成相同的乱码，不同的数据，生成
# 的乱码一定不同，不能通过乱码反推回原始数据
import hashlib

with open('/etc/passwd', 'rb') as fobj:
    data = fobj.read()

m = hashlib.md5(data)
print(m.hexdigest())

