import pickle
"""以前的文件写入，只能写入字符串，如果希望把任意数据对象(数字、列表等)写入文件，
取出来的时候数据类型不变，就用到pickle了
"""

# shop_list = ["eggs", "apple", "peach"]
# with open('/tmp/shop.data', 'wb') as fobj:
#     pickle.dump(shop_list, fobj)

with open('/tmp/shop.data', 'rb') as fobj:
    mylist = pickle.load(fobj)

print(mylist[0], mylist[1], mylist[2])
