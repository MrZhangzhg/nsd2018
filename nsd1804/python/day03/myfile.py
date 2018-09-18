# open('/tmp/abc.txt')  # 默认以r的方式打开，文件不存在则报错
# open('/tmp/abc.txt', 'w')  # 以w的方式打开，清空文件；文件不存在则创建
# cp /etc/passwd /tmp
f = open('/tmp/passwd')
data = f.read()
f.close()
print(data)
########################
f = open('/tmp/passwd')
data = f.read()   # 读到文件结束
print(data)
data = f.read()   # 文件指针已移动到结尾，没有数据可读
print(data)       # 无内容
f.close()
#################################
f = open('/tmp/passwd')
f.read(1)  # 可以指定读取的字节数
f.read(4096)   # 建议读4K，硬盘分区的默认block大小为4K
f.readline()   # 适合文本文件，读到\n结束
f.readlines()  # 适合文本文件，把内容全部读到列表中，每行是一个字符串项
f.close()
#####################################
f = open('/tmp/passwd')
for line in f:
    print(line, end='')   # 行尾有\n, print就不要再打印\n了，否则出现额外空行
f.close()
########################################
# cp /bin/ls /tmp/list
f = open('/tmp/list', 'rb')   # 非文本文件要以bytes类型打开
f.read(10)   # 可以把list的二进制数据读出
f.close()
########################################
f = open('/tmp/abc.txt', 'w')
f.write('hello world!\n')  # \n表示行尾
# cat /tmp/abc.txt   # 无内容，因为数据只写到了缓冲区
f.flush()   # 立即将数据同步至磁盘
f.writelines(['2nd line.\n', '3rd line.\n'])
f.close()
############################################
with open('/tmp/abc.txt', 'w') as f:  # with语句结束，文件自动关闭
    f.write('my test.\n')
##############################################
f = open('/tmp/passwd', 'rb')
f.tell()    # 显示文件指针位置
f.readline()
f.tell()
f.read(5)
f.seek(3, 0)   # 指针移动到开头以后的3个字节处
f.read(3)
f.seek(9, 1)
f.seek(-6, 2)
f.close()
##############################################
import sys
b = sys.stdin.readline()  # 标准输入，\n也会出现在变量b中
sys.stdout.write('hello world!\n')  # 标准输出，需要自己添加\n表示回车
sys.stderr.write('hello world!\n')  # 标准错误














