# 文件操作的三个步骤：打开、读写、关闭
# cp /etc/passwd /tmp
f = open('/tmp/passwd')  # 默认以r的方式打开纯文本文件
data = f.read()  # read()把所有内容读取出来
print(data)
data = f.read()  # 随着读写的进行，文件指针向后移动。
# 因为第一个f.read()已经把文件指针移动到结尾了，所以再读就没有数据了
# 所以data是空字符串
f.close()

f = open('/tmp/passwd')
data = f.read(4)  # 读4字节
f.readline()  # 读到换行符\n结束
f.readlines()  # 把每一行数据读出来放到列表中
f.close()

################################
f = open('/tmp/passwd')
for line in f:
    print(line,)
f.close()

##############################
f = open('图片地址', 'rb')  # 打开非文本文件要加参数b
f.read(4096)
f.close()

##################################
f = open('/tmp/myfile', 'w')  # 'w'打开文件，如果文件不存在则创建
f.write('hello world!\n')
f.flush()  # 立即将缓存中的数据同步到磁盘
f.writelines(['2nd line.\n', 'new line.\n'])
f.close()  # 关闭文件的时候，数据保存到磁盘

##############################
with open('/tmp/passwd') as f:
    print(f.readline())

#########################
f = open('/tmp/passwd')
f.tell()  # 查看文件指针的位置
f.readline()
f.tell()
f.seek(0, 0)  # 第一个数字是偏移量，第2位是数字是相对位置。
              # 相对位置0表示开头，1表示当前，2表示结尾
f.tell()
f.close()




