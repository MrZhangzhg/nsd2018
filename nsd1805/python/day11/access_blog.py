# from urllib import request
# import time
#
# url = 'http://luning.blog.sohu.com/324571791.html'
# header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#
# for i in range(10):
#     r = request.Request(url, headers=header)
#     html = request.urlopen(r)
#     data = html.read()
#     time.sleep(0.2)
####################################
import webbrowser
import time

url = 'http://luning.blog.sohu.com/324571791.html'

for i in range(10):
    webbrowser.open_new_tab(url)
    time.sleep(0.5)
