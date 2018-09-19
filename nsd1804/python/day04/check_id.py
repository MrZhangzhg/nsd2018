import keyword
from string import ascii_letters, digits

first_chs = ascii_letters + '_'
other_chs = first_chs + digits

def check_id(idt):
    if keyword.iskeyword(idt):
        return '%s is a keyword' % idt

    if idt[0] not in first_chs:
        return '1st char invalid'

    for ind, ch in enumerate(idt[1:]):
        if ch not in other_chs:
            return 'char in position %s invalid' % (ind + 2)

    return '%s is valid' % idt

if __name__ == '__main__':
    idt = input('输入标识符：')
    print(check_id(idt))
