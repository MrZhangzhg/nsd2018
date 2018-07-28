import sys
from urllib.request import urlopen
from urllib.request import Request

def get_web(url, fname):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    request = Request(url, headers=header)
    html = urlopen(request)

    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

    html.close()

if __name__ == '__main__':
    get_web(sys.argv[1], sys.argv[2])

