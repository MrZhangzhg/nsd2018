src_fname = '/bin/ls'
dst_fname = '/tmp/list'

with open(src_fname, 'rb') as src_fobj:
    with open(dst_fname, 'wb') as dst_fobj:
        while True:
            data = src_fobj.read(4096)
            if not data:
                break
            dst_fobj.write(data)
