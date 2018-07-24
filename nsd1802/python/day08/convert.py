import os

class Convert:
    def __init__(self, fname):
        self.fname = fname

    def to_linux(self):
        dst_fname = os.path.splitext(self.fname)[0] + '.linux'
        with open(self.fname, 'r') as src_fobj:
            with open(dst_fname, 'w') as dst_fobj:
                for line in src_fobj:
                    line = line.rstrip() + '\n'
                    dst_fobj.write(line)

    def to_windows(self):
        dst_fname = os.path.splitext(self.fname)[0] + '.windows'
        with open(self.fname, 'r') as src_fobj:
            with open(dst_fname, 'w') as dst_fobj:
                for line in src_fobj:
                    line = line.rstrip() + '\r\n'
                    dst_fobj.write(line)


if __name__ == '__main__':
    c = Convert('/tmp/passwd')  # cp /etc/passwd /tmp
    c.to_linux()
    c.to_windows()
