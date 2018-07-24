import re
from collections import Counter

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        cpatt = re.compile(patt)
        result = Counter()

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)  # 如果匹配不到，返回None
                if m:
                    result.update([m.group()])

        return result


if __name__ == '__main__':
    c = CountPatt('access_log')
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE|Chrome'
    a = c.count_patt(ip)
    print(a)
    print(a.most_common(3))
    print(c.count_patt(br))
