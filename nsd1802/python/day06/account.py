import pickle
import os
import time


def cost(wallet, record):
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) - amount
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % (date, amount, '', balance, comment)
        )

def save(wallet, record):
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) + amount
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % (date, '', amount, balance, comment)
        )

def query(wallet, record):
    print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'cost', 'save', 'balace', 'comment'))
    with open(record) as fobj:
        for line in fobj:
            print(line, end='')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj)
    print("Latest Balance: %d" % balance)


def show_menu():
    cmds = {'0': cost, '1': save, '2': query}
    prompt = """(0) cost
(1) save
(2) query
(3) exit
Please input your choice(0/1/2/3): """
    wallet = 'wallet.data'
    record = 'record.txt'
    if not os.path.exists(wallet):
        with open(wallet, 'wb') as fobj:
            pickle.dump(10000, fobj)

    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print()
            choice = '3'

        if choice not in '0123':
            print('Invalid input. Try again.')
            continue

        if choice == '3':
            break
        cmds[choice](wallet, record)

if __name__ == '__main__':
    show_menu()
