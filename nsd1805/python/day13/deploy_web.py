import requests
import os


def download(url, fname):
    'url: 服务器文件位置，fname是本地文件路径'
    r = requests.get(url)
    with open(fname, 'wb') as fobj:
        fobj.write(r.content)

def check_version(url, fname):
    'url: 远程服务器上live_version的路径，fname是本地文件路径'
    if not os.path.isfile(fname):
        download(url, fname)
        return True   # 本地没有live_version文件，有新版本

    r = requests.get(url)
    with open(fname) as fobj:
        local_version = fobj.read()

    if local_version != r.text:
        download(url, fname)
        return True   # 服务器和本地的live_version文件不一样，有新版本

    return False   # 服务器和本地的live_verion文件内容一致，没有新版本



def check_md5():
    pass


def deploy():
    pass


if __name__ == '__main__':
    version_url = 'http://192.168.4.3/deploy/live_version'
    local_ver = '/var/www/download/live_version'
    new = check_version(version_url, local_ver)
    if not new:
        exit()
    
