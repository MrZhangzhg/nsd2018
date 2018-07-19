py_str = 'hello world!'
py_str.capitalize()
py_str.title()
py_str.center(50)
py_str.center(50, '#')
py_str.ljust(50, '*')
py_str.rjust(50, '*')
py_str.count('l')  # 统计l出现的次数
py_str.count('lo')
py_str.endswith('!')  # 以!结尾吗？
py_str.endswith('d!')
py_str.startswith('a')  # 以a开头吗？
py_str.islower()  # 字母都是小写的？其他字符不考虑
py_str.isupper()  # 字母都是大写的？其他字符不考虑
'Hao123'.isdigit()  # 所有字符都是数字吗？
'Hao123'.isalnum()  # 所有字符都是字母数字？
'  hello\t    '.strip()  # 去除两端空白字符，常用
'  hello\t    '.lstrip()
'  hello\t    '.rstrip()
'how are you?'.split()
'hello.tar.gz'.split('.')
'.'.join(['hello', 'tar', 'gz'])
'-'.join(['hello', 'tar', 'gz'])



