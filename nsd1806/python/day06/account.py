import os
import pickle as p

def save(record):


def cost(record):


def view(record):


def show_menu():
    record = 'record.data'
    if not os.path.exists(record):
        init_data = [['2018-11-14', 0, 0, 10000, '开始记账']]
        with open(record, 'wb') as fobj:
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
        cmds[choice](record)

if __name__ == '__main__':
    show_menu()
