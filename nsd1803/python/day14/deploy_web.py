import requests
import os
import hashlib
import tarfile
from urllib import request

def get_webdata(url):
    r = requests.get(url)
    return r.text

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def deploy(app):  # /var/www/packages/myproject_1.0.tar.gz
    os.chdir('/var/www/packages')
    tar = tarfile.open(app, 'r:gz')
    tar.extractall()
    tar.close()
    src = app.replace('.tar.gz', '')
    dst = '/var/www/html/mysite'
    if os.path.exists(dst):
        os.unlink(dst)
    os.symlink(src, dst)

if __name__ == '__main__':
    ver = get_webdata('http://192.168.122.73/live_version').strip()
    app_name = 'myproject_%s.tar.gz' % ver
    app_url = 'http://192.168.122.73/packages/' + app_name
    app_path = os.path.join('/var/www/packages', app_name)
    download(app_url, app_path)
    local_md5 = check_md5(app_path)
    remote_md5 = get_webdata(app_url + '.md5').strip()
    if local_md5 == remote_md5:
        deploy(app_path)
