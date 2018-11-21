from urllib import request
import re
import os

def get_file(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def get_urls(patt, fname, charset='utf8'):
    url_list = []   # 将匹配到的网址放到列表中
    cpatt = re.compile(patt)   # 将模式编译，提升效率
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)   # 在每一行中匹配网址
            if m:
                url_list.append(m.group())

    return url_list

if __name__ == '__main__':
    url_163 = 'http://www.163.com'
    fname_163 = '/tmp/163.html'
    get_file(url_163, fname_163)
    img_patt = '(http|https)://[\w./]+\.(jpg|jpeg|gif|png)'
    img_list = get_urls(img_patt, fname_163, 'GBK')

    dst = '/tmp/163imgs/'
    if not os.path.exists(dst):
        os.mkdir(dst)
    for url in img_list:
        fname = url.split('/')[-1]
        fname = os.path.join(dst, fname)
        get_file(url, fname)
