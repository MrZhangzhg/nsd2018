# cp /etc/passwd /tmp/mima
# fobj = open('mima')  # 文件不存在，报错
fobj = open('/tmp/mima')  # 不指定打开模式，以r方式打开
data = fobj.read()  # read默认读取全部内容
print(data)  # 打印内容
data = fobj.read()  # 因为文件指针已经移动到尾部，没有数据可读，所在data是空串
print(data)
fobj.close()

fobj = open('/tmp/mima')
fobj.read(4)  # 指定读取4字节，建议一次读1024的倍数
fobj.readline()  # 适合文本文件，读一行
fobj.readlines()  # 适合文本文件，把所有行读到列表中
fobj.close()

fobj = open('/tmp/mima')
for line in fobj:
    print(line, end='')
fobj.close()

fobj = open('/tmp/mima', 'w')
fobj.write('Hello World!\n')  # 写数据时，先放到缓冲区
                              # 当数据量达到一定程度时，自动写入磁盘
fobj.flush()  # 立即将数据同步至磁盘
fobj.writelines(['3rd line.\n', 'new line.\n'])
fobj.close()  # 关闭文件时，数据自动写入磁盘

with open('/tmp/mima') as fobj:  # with语句结束，文件自动关闭
    print(fobj.readline())

fobj = open('/tmp/mima', 'rb')  # 非文本文件要加上b，文本文件也可以加b，表示bytes
fobj.tell()  #　返回文件指针的位置
fobj.seek(10, 0)  # 第一个数字是偏移量；第二个数字是相对位置，0表示开头，1是当前，2是结尾
fobj.read(4)  # 从当前位置读4字节，因为是bytes方式打开，所以显示b'xxxx'
fobj.seek(-5, 2)  # 移动到文件倒数第5个字节的位置。以'rb'才能写负数，'r'不行

import sys

a = sys.stdin.readline()  # 读取键盘输入，回车也作为一个字符\n读入
print(a)
sys.stdout.write(a)
sys.stderr.write(a)












