from urllib import request

def get_file(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    url = 'https://upload-images.jianshu.io/upload_images/4468763-e584750f712161ce.jpg'
    fname = '/tmp/img.jpg'
    get_file(url, fname)
    # eog /tmp/img.jpg
