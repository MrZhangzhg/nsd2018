import os
import tarfile
import hashlib
import pickle as p
from time import strftime

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup(src_dir, dst_dir, md5file):
    fname = "%s_full_%s.tar.gz" % \
            (os.path.basename(src_dir.rstrip('/')), strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    md5_dict = {}
    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            md5_dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        p.dump(md5_dict, fobj)

def incr_backup(src_dir, dst_dir, md5file):
    fname = "%s_incr_%s.tar.gz" % \
            (os.path.basename(src_dir.rstrip('/')), strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    new_md5 = {}
    with open(md5file, 'rb') as fobj:
        old_md5 = p.load(fobj)

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            new_md5[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        p.dump(new_md5, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in new_md5:
        if old_md5.get(key) != new_md5[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    # cp -r /etc/security /tmp
    # mkdir /tmp/backup
    src_dir = '/tmp/security'
    dst_dir = '/tmp/backup/'
    md5file = '/tmp/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
