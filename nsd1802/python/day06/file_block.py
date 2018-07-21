def blocks(fobj):
    block = []
    counter = 0
    for line in fobj:
        block.append(line)
        counter += 1
        if counter == 10:
            yield block  # 返回中间结果，下次取值，从这里继续向下执行
            block = []
            counter = 0
    if block:
        yield block

if __name__ == '__main__':
    fobj = open('/tmp/passwd')  # cp /etc/passwd /tmp
    for lines in blocks(fobj):
        print(lines)
        print()
    fobj.close()
