import requests
import os
import hashlib
import tarfile
from urllib.request import urlopen

def get_pack_name(version):
    '返回下载的软件包url'
    version_url = 'http://192.168.122.17/deploy/%s_version' % version
    r = requests.get(version_url)
    ver = r.text.strip()
    url = 'http://192.168.122.17/deploy/packages/wordpress-%s.tar.gz' % ver
    return url

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def download(url):
    '下载软件包，返回软件包的绝对路径'
    html = urlopen(url)
    fname = url.split('/')[-1]
    fname = os.path.join('/var/tmp', fname)

    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)
    html.close()

    return fname


def check_package(fname):
    '校验软件包是否完好，没问题返回True，否则返回False'
    local_md5 = check_md5(fname)
    local_name = os.path.basename(fname)
    url = 'http://192.168.122.17/deploy/packages/' + local_name + '.md5'
    r = requests.get(url)
    remote_md5 = r.text.strip()
    if local_md5 == remote_md5:
        return True

    return False

def deploy(fname):
    '将下载的软件包部署到web服务器'
    web_root = '/var/www'
    os.chdir(web_root)
    tar = tarfile.open(fname, 'r:gz')
    tar.extractall()
    tar.close()
    dst_fname = fname.replace('.tar.gz', '')
    dst_fname = os.path.basename(dst_fname)
    dst_fname = os.path.join(web_root, dst_fname)
    link = '/var/www/html/wordpress'
    if os.path.islink(link):
        os.unlink(link)
    os.symlink(dst_fname, '/var/www/html/wordpress')

if __name__ == '__main__':
    prompt = """(0) 最新版本
(1) 上一个版本
请选择(0/1)："""
    choice = input(prompt)
    if choice == '0':
        version = 'live'
    elif choice == '1':
        version = 'last'
    url = get_pack_name(version)
    fname = download(url)
    fileok = check_package(fname)
    if fileok:
        deploy(fname)
    else:
        print('下载的文件已损坏，请重新下载')
