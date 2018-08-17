from string import ascii_letters, digits
from keyword import iskeyword

first_chs = ascii_letters + '_'
other_chs = first_chs + digits

def check_id(idt):
    if iskeyword(idt):
        return '%s is keyword' % idt  # 函数有多个return，只会执行一个Return

    if idt[0] not in first_chs:
        return '1st invalid.'

    for ind, ch in enumerate(idt[1:]):
        if ch not in other_chs:
            return '第%s个字符不合法' % (ind + 2)

    return '%s是合法的' % idt

if __name__ == '__main__':
    idt = input("待检查的标识符: ")
    print(check_id(idt))
