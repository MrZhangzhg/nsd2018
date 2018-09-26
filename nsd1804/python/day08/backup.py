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

def full_backup(src_dir, dst_dir, md5file):
    fname = '%s_full_%s.tar.gz' % (
        os.path.basename(src_dir.rstrip('/')), time.strftime('%Y%m%d')
    )  # 去除源目录尾部的/，生成备份的目标文件名
    fname = os.path.join(dst_dir, fname)  # 组合绝对路径
    md5dict = {}  # 用于存储文件的md5值
    tar = tarfile.open(fname, 'w:gz')  # 把整个目录打个tar包
    tar.add(src_dir)
    tar.close()

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        p.dump(md5dict, fobj)

def incr_backup(src_dir, dst_dir, md5file):
    pass

if __name__ == '__main__':
    src_dir = '/tmp/security'
    dst_dir = '/tmp/backup'
    md5file = '/tmp/backup/md5.data'
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    if time.strftime('%a') == 'Wed':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
