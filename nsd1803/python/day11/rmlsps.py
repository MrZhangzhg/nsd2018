whitesps = ' \r\n\v\f\t'

def rmlsps(astr):
    for i in range(len(astr)):
        if astr[i] not in whitesps:
            return astr[i:]
    else:
        return ''

if __name__ == '__main__':
    print(rmlsps('  \thello  '))
    print(rmlsps(''))

