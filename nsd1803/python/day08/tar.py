import tarfile
import os

########压缩##############
os.chdir('/etc')
tar = tarfile.open('/tmp/anquan.tar.gz', 'w:gz')
tar.add('security')
tar.add('hosts')
tar.close()

###########解 压################
# os.chdir('/var/tmp')
# tar = tarfile.open('/tmp/anquan.tar.gz')
# tar.extractall()
# tar.close()
