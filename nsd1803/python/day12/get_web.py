from urllib import request

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download('http://www.tedu.cn/', '/tmp/tedu.html')
    download('http://images.sport.org.cn/Image/2013/05/22/0058327469.jpg', '/tmp/runner.jpg')
