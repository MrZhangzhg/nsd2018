import re
import os
from urllib import request

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def search_url(fname, patt):
    patt_list = []
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                item = m.group()
                patt_list.append(item)

    return patt_list

if __name__ == '__main__':
    img_dirs = '/tmp/imgs'
    if not os.path.exists(img_dirs):
        os.mkdir(img_dirs)
    download('http://www.tedu.cn/', '/tmp/tedu.html')  # 获得达内首页
    img_patt = 'http://[\w./-]+\.(jpg|jpeg|gif|png)'  # 匹配图片URL
    img_list = search_url('/tmp/tedu.html', img_patt)
    for url in img_list:
        fname = url.split('/')[-1]  # 获得URL中的图片名
        fname = os.path.join(img_dirs, fname)  # 拼接出本地文件名
        try:
            download(url, fname)
        except:
            pass
