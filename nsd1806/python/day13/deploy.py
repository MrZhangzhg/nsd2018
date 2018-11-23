import os
import requests
import hashlib
import tarfile

def check_version(ver_url, fname):
    # 如果本地没有版本文件，意味着有新版本
    if not os.path.exists(fname):
        return True

    # 如果本地版本文件和网上的版本不一样，有新版本
    r = requests.get(ver_url)
    with open(fname) as fobj:
        lver = fobj.read()
    if lver != r.text:
        return True

    # 如果上述两个条件都不满足，没有新版本
    return False

def download(url, fname):
    r = requests.get(url)
    with open(fname, 'wb') as fobj:
        fobj.write(r.content)

def check_md5(url, fname):
    # 计算本地md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    file_md5 = m.hexdigest()

    # 读取网上的md5值
    r = requests.get(url)
    if file_md5 == r.text.strip():
        return True   # 文件未损坏，返回True

    return False      # 文件已损坏，返回False


def deploy(app_fname):
    # 解压程序文件到部署目录
    os.chdir('/var/www/deploy/')
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall()
    tar.close()

    # 如果目标软链接已存在，则删除
    dest = '/var/www/html/nsd1806'
    if os.path.exists(dest):
        os.unlink(dest)

    # 创建软链接
    src = os.path.basename(app_fname.replace('.tar.gz', ''))
    src = os.path.join('/var/www/deploy', src)
    os.symlink(src, dest)

if __name__ == '__main__':
    ver_url = 'http://192.168.4.3/deploy/live_version'
    ver_fname = '/var/www/deploy/live_version'
    new_ver = check_version(ver_url, ver_fname)
    if not new_ver:
        print('没有新版本软件')
        exit(1)
    r = requests.get(ver_url)
    app_url = 'http://192.168.4.3/deploy/packages/web_pro_%s.tar.gz' % r.text.strip()
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join('/var/www/download/', app_fname)
    download(app_url, app_fname)
    md5_url = 'http://192.168.4.3/deploy/packages/web_pro_%s.tar.gz.md5' % r.text.strip()
    file_ok = check_md5(md5_url, app_fname)
    if not file_ok:
        print('文件已损坏')
        exit(2)
    deploy(app_fname)
    download(ver_url, ver_fname)    # 更新本地live_version
    print('部署完成!!!')
