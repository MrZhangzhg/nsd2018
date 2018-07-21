from random import randint

def quick_sort(num_list):
    if len(num_list) < 2:
        return num_list

    middle = num_list[0]
    smaller = []
    larger = []
    for i in num_list[1:]:
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)

    return quick_sort(smaller) + [middle] + quick_sort(larger)

if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(10)]
    print(alist)
    print(quick_sort(alist))
