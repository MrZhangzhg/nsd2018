import sys
from urllib.request import urlopen

def get_web(url, fname):
    html = urlopen(url)

    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

    html.close()

if __name__ == '__main__':
    get_web(sys.argv[1], sys.argv[2])

