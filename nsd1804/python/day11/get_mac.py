#!/usr/bin/env	python

import	subprocess
import	threading
import	os
import	sys

def	get_mac(ip):
     os.system('ping -c2 %s	&> /dev/null' % ip)
     result	 =	 subprocess.Popen('arp -n %s | tail -1' % ip, shell=True, stdout=subprocess.PIPE)
     arp = result.stdout.readline()
     if	':'	in	arp:
         ip	= arp.split()[0]
         mac = arp.split()[2]
         print ip, mac

def	main():
     if	len(sys.argv) != 2:
         print "Usage: %s subnet"	% sys.argv[0]
         sys.exit(1)
     subnet	= sys.argv[1].split('.')[:-1]
     ips = ('%s.%s'	% ('.'.join(subnet), i) for	i in range(1, 255))
     for line in ips:
         ip	= line.strip()
         t = threading.Thread(target=get_mac, args=(ip,))
         t.start()

if	__name__ == '__main__':
    sys.exit(main())
