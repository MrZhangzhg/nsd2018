def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('age out of range.')
    print('%s: %s' % (name, age))

def set_age2(name, age):
    assert 0 < age < 120, 'age out of range.'
    print('%s: %s' % (name, age))

if __name__ == '__main__':
    set_age('bob', 20)
    set_age2('alice', 188)
