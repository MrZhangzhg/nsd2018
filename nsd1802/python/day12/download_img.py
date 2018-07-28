import os
from get_url import get_url
from getweb import get_web

get_web('http://www.tedu.cn/', '/tmp/tedu.html')
img_url = r'http://[.\w/-]+\.(jpg|png|jpeg|gif)'
urls = get_url(img_url, '/tmp/tedu.html')
img_dir = '/tmp/images'

if not os.path.exists(img_dir):
    os.mkdir(img_dir)

for url in urls:
    fname = os.path.join(img_dir, url.split('/')[-1])
    try:
        get_web(url, fname)
    except:
        pass
