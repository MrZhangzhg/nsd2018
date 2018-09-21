def gen_block(fobj):  # 接受文件对象，每生成10行返回给用户
    lines = []
    counter = 0
    for line in fobj:
        lines.append(line)
        counter += 1
        if counter == 10:
            yield lines  # 返回中间结果，生成器暂停运行
            lines = []  # 再次向生成器取值时，从此处继续执行
            counter = 0
    if lines:
        yield lines


if __name__ == '__main__':
    fobj = open('/tmp/mima')
    for block in gen_block(fobj):
        print(block)
        print()
    fobj.close()
