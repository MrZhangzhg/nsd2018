a = 10
b = 20

if a < b:
    smaller = a
else:
    smaller = b

print(smaller)

s = a if a < b else b  # 和上面的if-else语句等价

print(s)
