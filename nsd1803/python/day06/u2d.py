import sys

def unix2dos(fname):
    dst_fname = fname + '.txt'
    src_fobj = open(fname)
    dst_fobj = open(dst_fname, 'w')
    for line in src_fobj:
        line = line.rstrip() + '\r\n'
        dst_fobj.write(line)
    src_fobj.close()
    dst_fobj.close()

if __name__ == '__main__':
    unix2dos(sys.argv[1])
