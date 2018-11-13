stack = []

def push_it():
    item = input('item to push: ').strip()
    if item:  # 判断，如果字符串非空
        stack.append(item)

def pop_it():
    if stack:  # 判断，如果列表非空
        print('\033[31;1mFrom stack, popped: %s\033[0m' % stack.pop())
    else:
        print('\033[31;1mEmpty stack.\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    # 将函数保存到一个名为cmds的字典中
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) push it
(1) pop it
(2) view it
(3) quit
Please input your choice(0/1/2/3): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid input. Try again.')
            continue
        if choice == '3':
            break

        cmds[choice]()  # 根据用户的输入，在字典中取出函数，调用
        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_it()

if __name__ == '__main__':
    show_menu()
