import os
import requests
import sys
import hashlib
import tarfile

def check_version(remote_ver, local_ver):
    '用于判断服务器上是否有新版本的软件，有返回True，否则返回False'
    if not os.path.exists(local_ver):
        return True  # 如果本地版本文件不存在则返回True

    r = requests.get(remote_ver)
    with open(local_ver) as fobj:
        version = fobj.read()

    if version != r.text:
        return True

    return False

def check_md5(md5_url, local_fname):
    '文件没有损坏，返回True，否则返回False'
    r = requests.get(md5_url)
    m = hashlib.md5()
    with open(local_fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    if m.hexdigest() == r.text.strip():
        return True  # md5相同返回True，否则是False

    return False

def download(url, dst_name):
    r = requests.get(url)
    with open(dst_name, 'wb') as fobj:
        fobj.write(r.content)

def deploy(pkg, ver):
    os.chdir('/var/www/packages/')  # 切换到目标目录
    tar = tarfile.open(pkg, 'r:gz')  # 解压缩
    tar.extractall()
    tar.close()
    src_fname = '/var/www/packages/mp-%s' % ver
    if os.path.exists('/var/www/html/mysite'):
        os.unlink('/var/www/html/mysite')
    os.symlink(src_fname, '/var/www/html/mysite')

if __name__ == '__main__':
    remote_ver = 'http://192.168.4.3/deploy/live_version'
    local_ver = '/var/www/packages/live_verion'
    new_ver = check_version(remote_ver, local_ver)
    if not new_ver:  # 如果服务器上没有新版本软件则退出程序
        sys.exit(0)

    r = requests.get(remote_ver)
    ver = r.text.strip()
    soft_url = 'http://192.168.4.3/deploy/packages/mp-%s.tar.gz' % ver
    local_fname = '/var/www/packages/mp-%s.tar.gz' % ver
    download(soft_url, local_fname)  # 下载最新版本的文件
    md5_url = 'http://192.168.4.3/deploy/packages/mp-%s.tar.gz.md5' % ver
    file_ok = check_md5(md5_url, local_fname)
    if not file_ok:  # 如果下载的文件是损坏的，程序退出
        sys.exit(1)
    download(remote_ver, local_ver)  # 下载版本文件到本地
    deploy(local_fname, ver)   # 部署服务器
