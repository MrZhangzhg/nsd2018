import os

def get_fname():
    while True:
        fname = input('文件名：')
        if not os.path.exists(fname):
            break
        print('%s 已存在，请重试' % fname)

    return fname   # 用户输入的是abc.txt，返回值就是abc.txt，不是变量fname

def get_content():
    content = []
    print('请输入内容(输入end结束)：')
    while True:
        line = input('> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:  # 不同函数中的fname没有关系，可以用不同的名字
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ["%s\n" % line for line in content]
    wfile(fname, content)
