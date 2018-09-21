import os
import pickle as p
import time

def save_money(record, wallet):
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj) + amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write(
            '%-15s%-8s%-8s%-8s%-20s\n' % (date, amount, '', balance, comment)
        )

def cost_money(record, wallet):
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj) - amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write(
            '%-15s%-8s%-8s%-8s%-20s\n' % (date, '', amount, balance, comment)
        )

def query_money(record, wallet):
    print('%-15s%-8s%-8s%-8s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    with open(record) as fobj:
        for line in fobj:
            print(line, end='')
    with open(wallet, 'rb') as fobj:
        print('Latest Balance: %s' % p.load(fobj))

def show_menu():
    record = '/tmp/record.txt'
    wallet = '/tmp/wallet.data'
    cmds = {'0': save_money, '1': cost_money, '2': query_money}
    prompt = """(0) save money
(1) cost money
(2) query money
(3) quit
Please input your choice(0/1/2/3): """
    if not os.path.exists(wallet):
        with open(wallet, 'wb') as fobj:
            p.dump(10000, fobj)

    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid choice. Try again.')
            continue
        if choice == '3':
            break
        cmds[choice](record, wallet)

if __name__ == '__main__':
    show_menu()
