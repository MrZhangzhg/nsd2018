import time
import os
import tarfile
import hashlib
import pickle as p

def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()


def full_backup(src_dir, dst_dir, md5_file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname, time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)
    md5dict = {}

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    for path, folders, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5_file, 'wb') as fobj:
        p.dump(md5dict, fobj)


def incr_backup(src_dir, dst_dir, md5_file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)
    md5dict = {}

    for path, folders, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5_file, 'rb') as fobj:
        old_md5 = p.load(fobj)

    with open(md5_file, 'wb') as fobj:
        p.dump(md5dict, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    src_dir = '/tmp/demo/security/'
    dst_dir = '/tmp/demo/backup/'
    md5_file = '/tmp/demo/backup/md5.data'
    if time.strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir, md5_file)
    else:
        incr_backup(src_dir, dst_dir, md5_file)

