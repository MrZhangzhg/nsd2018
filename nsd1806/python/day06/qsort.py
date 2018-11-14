from random import randint

def qsort(seq):
    if len(seq) < 2:
        return seq
    smaller = []
    larger = []
    middle = seq[0]   # 82
    for i in seq[1:]:
        if i <= middle:
            smaller.append(i)  # [4, 20, 31, 29, 77, 20]
        else:
            larger.append(i)   # [86, 97, 98]
    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)  # [82, 4, 20, 86, 97, 31, 29, 77, 98, 20]
    print(qsort(nums))
