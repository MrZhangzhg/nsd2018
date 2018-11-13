import sys

def unix2dos(fname, end='\r\n'):
    new_fname = fname + '.txt'
    with open(fname) as src_fobj:
        with open(new_fname, 'w') as dst_fobj:
            for line in src_fobj:
                dst_fobj.write(line.rstrip() + end)

if __name__ == '__main__':
    unix2dos(sys.argv[1])
