from urllib.request import quote
import webbrowser

words = quote('hello world!')
search = 'https://www.baidu.com/s?wd=' + words
print(search)
webbrowser.open_new_tab(search)
