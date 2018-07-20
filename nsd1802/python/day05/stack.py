stack = []

def push_it():
    item = input('item to push: ')
    stack.append(item)

def pop_it():
    if stack:
        print("from stack popped %s" % stack.pop())

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) push it
(1) pop it
(2) view it
(3) exit
Please input your choice(0/1/2/3): """

    while True:
        # input()得到字符串，用strip()去除两端空白，再取下标为0的字符
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid input. Try again.')
            continue

        if choice == '3':
            break

        cmds[choice]()


if __name__ == '__main__':
    show_menu()
