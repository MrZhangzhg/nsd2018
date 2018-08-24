# http://down.51cto.com
# 正则表达式必知必会

import re

data = 'my phone number: 15012348765'
m = re.search('.+(\d+)', data)
print(m.group())
print(m.group(1))  # 1表示正则模式中()内的匹配

# 默认+/*都是贪婪匹配，也就是尽可能匹配的更多，在其后面加上?就让?右边的模式
# 尽量多的匹配
m = re.search('.+?(\d+)', data)
print(m.group(1))
