import os
import time
import pickle as p


def save(fname):
    '''把记账的大列表取出，大列表中最后的一个小列表是最新记录，记录的倒数第二项
    是余额，取出余额，加上收入，是最新余额。
    生成新的记录，追加到大列表中。再把大列表存到文件。
    '''
    amount = int(input("amount: "))
    comment = input("comment: ")
    date = time.strftime('%Y-%m-%d')

    with open(fname, 'rb') as fobj:
        records = p.load(fobj)  # [['2018-11-14', 0, 0, 10000, '开始记账']]
        balance = records[-1][-2] + amount
        # record = ['2018-10-15', 0, 10000, 20000, 'salary']
        record = [date, 0, amount, balance, comment]
        # [['2018-11-14', 0, 0, 10000, '开始记账'], ['2018-10-15', 0, 10000, 20000, 'salary']]
        records.append(record)

    with open(fname, 'wb') as fobj:
        p.dump(records, fobj)

def cost(fname):
    amount = int(input("amount: "))
    comment = input("comment: ")
    date = time.strftime('%Y-%m-%d')

    with open(fname, 'rb') as fobj:
        records = p.load(fobj)
        balance = records[-1][-2] - amount
        record = [date, amount, 0, balance, comment]
        records.append(record)

    with open(fname, 'wb') as fobj:
        p.dump(records, fobj)

def view(fname):
    with open(fname, 'rb') as fobj:
        records = p.load(fobj)

    print('%-16s%-8s%-8s%-12s%-30s' % ('date', 'cost', 'save', 'balance', 'comment'))
    for record in records:
        print('%-16s%-8s%-8s%-12s%-30s' % tuple(record))

def show_menu():
    fname = 'record.data'
    if not os.path.exists(fname):
        init_data = [['2018-11-14', 0, 0, 10000, '开始记账']]
        with open(fname, 'wb') as fobj:
            p.dump(init_data, fobj)
    cmds = {'0': save, '1': cost, '2': view}
    prompt = """(0) save
(1) cost
(2) view
(3) quit
Please input your choice(0/1/2/3): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid choice. Try again.')
            continue
        if choice == '3':
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
