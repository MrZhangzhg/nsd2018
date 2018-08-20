import pickle as p
# pickle存储器可以将任意的数据类型写入文件，还可以无损地取出

shop_file = '/tmp/shop.txt'
# shop_list = ['apple', 'eggs', 'banana']
# with open(shop_file, 'wb') as fobj:
#     p.dump(shop_list, fobj)  # 将列表写入文件

with open(shop_file, 'rb') as fobj:
    mylist = p.load(fobj)  # 从文件中取的数据仍然是列表

mylist[1]