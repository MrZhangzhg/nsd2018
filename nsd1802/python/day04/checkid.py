import sys
import keyword
import string

first_chs = string.ascii_letters + '_'
all_chs = first_chs + string.digits

def check_id(idt):
    if keyword.iskeyword(idt):
        return "%s is keyword" % idt

    if idt[0] not in first_chs:
        return "1st invalid"

    for ind, ch in enumerate(idt[1:]):
        if ch not in all_chs:
            return "char in postion #%s invalid" % (ind + 2)

    return "%s is valid" % idt


if __name__ == '__main__':
    print(check_id(sys.argv[1]))  # python3 checkid.py abc@123
