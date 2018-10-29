from urllib import request
import os


def download(url, path):
    html = request.urlopen(url)
    with open(path, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    netease = 'http://www.163.com/'
    local_dir = '/tmp/netease/'
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    file163 = os.path.join(local_dir, '163.html')
    download(netease, file163)




