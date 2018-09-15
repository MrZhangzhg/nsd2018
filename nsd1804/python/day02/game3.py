import random

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = """(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2): """
pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:
    ind = int(input(prompt))
    comuter = random.choice(all_choice)
    player = all_choice[ind]

    print("Your choice: %s, computer's choice: %s" % (player, comuter))
    if player == comuter:
        print('\033[32;1m平局\033[0m')
    elif [player, comuter] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
