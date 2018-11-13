def set_age(name, age):
    if not 0 < age < 150:
        raise ValueError('age out of range')
    print('%s is %d years old' % (name, age))

def set_age2(name, age):
    assert 0 < age < 150, 'age out of range'
    print('%s is %d years old' % (name, age))

if __name__ == '__main__':
    set_age('bob', 23)
    set_age2('bob', 233)
