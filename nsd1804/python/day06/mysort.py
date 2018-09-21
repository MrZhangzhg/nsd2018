from random import randint

def qsort(num_list):
    if len(num_list) < 2:
        return num_list

    middle = num_list[0]  # 假设第一个数是中间值
    smaller = []  # 比middle小的放在这里
    larger = []   # 比middle大的放在这里
    for i in num_list[1:]:
        if i <= middle:
            smaller.append(i)
        else:
            larger.append(i)

    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(10)]
    print(alist)
    print(qsort(alist))
