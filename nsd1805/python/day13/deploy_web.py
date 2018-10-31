import requests
import os
import hashlib
import tarfile


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


def check_md5(md5_url, fname):
    # 读取远程md5文件中的值
    r = requests.get(md5_url)
    remote_md5 = r.text.strip()

    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    local_md5 = m.hexdigest()

    if local_md5 == remote_md5:
        return True  # 如果md5相同，表示文件在下载过程中未损坏

    return False


def deploy(app_path, deploy_dir):
    os.chdir(deploy_dir)  # 进入到部署目录，解压程序文件
    tar = tarfile.open(app_path, 'r:gz')
    tar.extractall()
    tar.close()

    fname = os.path.basename(app_path)  # 获取文件名
    # 获取解压文件的绝对路径
    src_dir = os.path.join(deploy_dir, fname.replace('.tar.gz', ''))
    web_link = '/var/www/html/nsd1805'
    if os.path.exists(web_link):  # 如果链接已存在，则删除
        os.unlink(web_link)
    os.symlink(src_dir, web_link)


if __name__ == '__main__':
    version_url = 'http://192.168.4.3/deploy/live_version'
    local_ver = '/var/www/download/live_version'
    new = check_version(version_url, local_ver)
    if not new:
        print('没有发现新版本')
        exit(1)

    # 下载最新的软件版本
    with open(local_ver) as fobj:
        version = fobj.read().strip()  # 获取版本号
    # 下载软件
    app_url = 'http://192.168.4.3/deploy/packages/core_py_%s.tar.gz' % version
    app_path = '/var/www/download/core_py_%s.tar.gz' % version
    download(app_url, app_path)

    # 校验md5值，如果文件损坏则中止程序
    md5_url = 'http://192.168.4.3/deploy/packages/core_py_%s.tar.gz.md5' % version
    file_ok = check_md5(md5_url, app_path)
    if not file_ok:
        print('文件在下载过程中已损坏')
        os.rename(local_ver, '/var/www/download/live_version.save')
        exit(2)

    # 如果应用文件是完好的，把它部署到服务器
    deploy_dir = '/var/www/deploy/'
    deploy(app_path, deploy_dir)
