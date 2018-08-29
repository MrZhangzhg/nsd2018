'pip3 install requests'

import requests

payload = {'wd': 'centos7'}
r = requests.get('http://www.baidu.com/s', params=payload)
# 相当于访问http://www.baidu.com/s?wd=centos7
