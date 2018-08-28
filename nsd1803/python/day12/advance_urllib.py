'''
标准的URL字符中不能包括汉字、一些标点符号等。为了能表示这些字符，需要编解码
'''

from urllib import request

r = request.quote('hello 达内')   # 编码成浏览器可读字符
print(r)
ur = request.unquote(r)
print(ur)

