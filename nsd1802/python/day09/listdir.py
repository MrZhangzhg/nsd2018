import os
import sys

def list_files(path):
    if os.path.isdir(path):
        print(path + ':')
        content = os.listdir(path)
        print(content)
        for fname in content:
            fname = os.path.join(path, fname)
            list_files(fname)

if __name__ == '__main__':
    list_files(sys.argv[1])
