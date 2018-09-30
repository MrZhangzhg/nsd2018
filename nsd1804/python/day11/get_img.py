from urllib import request

img_url = 'https://upload-images.jianshu.io/upload_images/1276176-ce4d97b8f2309161.jpg'
img_obj = request.urlopen(img_url)

with open('/tmp/uimg.jpg', 'wb') as fobj:
    while True:
        data = img_obj.read(4096)
        if not data:
            break
        fobj.write(data)
