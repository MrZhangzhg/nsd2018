from getpass import getpass

userdb = {}

def login():
    username = input('username: ')
    password = getpass('password: ')
    # if username not in userdb or userdb[username] != password:
    if userdb.get(username) != password:
        print('登陆失败')
    else:
        print('登陆成功')

def register():
    username = input('username: ')
    if username not in userdb:
        password = input('password: ')
        userdb[username] = password
    else:
        print('%s已存在' % username)

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = '''(0) 新用户注册
(1) 登陆
(2) 退出
请选择(0/1/2)：'''
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print('无效输入。请重试。')
            continue

        if choice == '2':
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
