import re

def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 匹配不到是None，None为False；匹配到，非空是True
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict

if __name__ == '__main__':
    log_file = 'access_log'
    ip = '^(\d+\.){3}\d+'
    print(count_patt(log_file, ip))
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(log_file, br))

# >>> import count_patt
# >>> bash = 'nologin$|bash$'
# >>> count_patt.count_patt('/etc/passwd', bash)

