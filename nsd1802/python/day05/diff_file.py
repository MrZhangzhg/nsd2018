# cp /etc/passwd .
# cp /etc/passwd mima
# vim mima  -> 修改，与passwd有些区别

with open('passwd') as fobj:
    aset = set(fobj)

with open('mima') as fobj:
    bset = set(fobj)

with open('diff.txt', 'w') as fobj:
    fobj.writelines(bset - aset)
