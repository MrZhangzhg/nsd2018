from urllib import request
import os
import re


def download(url, path):
    """ 下载网络资源到本地

    :param url: 资源网址
    :param path: 本地文件的路径
    :return: 没有返回值
    """
    html = request.urlopen(url)
    with open(path, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

def get_url(fname, patt, code='utf8'):
    ''' 用于将文件中的指定内容，保存到列表中

    :param fname: 本地文件
    :param patt: 在文件中匹配的正则表达式模式
    :param code: 打开文件时所用字符编码
    :return: 匹配内容的列表
    '''
    cpatt = re.compile(patt)
    result = []

    with open(fname, encoding=code) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                url = m.group()
                result.append(url)

    return result


if __name__ == '__main__':
    netease = 'http://www.163.com/'
    local_dir = '/tmp/netease/'
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    file163 = os.path.join(local_dir, '163.html')
    download(netease, file163)  # 下载网易首页

    img_patt = r'(http|https)://[\w./]+\.(jpg|gif|png|jpeg)'  # 图片url
    img_list = get_url(file163, img_patt, 'gbk')
    for url in img_list:
        fname = url.split('/')[-1]
        fname = os.path.join(local_dir, fname)
        download(url, fname)
