import sys
from urllib.request import urlopen
from urllib.error import HTTPError

def get_web(url, fname):
    try:
        html = urlopen(url)
    except HTTPError as e:  # 返回HTTPError类的实例e
        print(e)
        if e.code == 403:
            print('权限不足')
        elif e.code == 404:
            print('没有那个地址')
        return

    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

    html.close()

if __name__ == '__main__':
    get_web(sys.argv[1], sys.argv[2])

