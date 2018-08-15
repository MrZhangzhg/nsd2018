# yn = input('Continue(y/n)? ')
#
# while yn not in ['n', 'N']:
#     print('running...')
#     yn = input('Continue(y/n)? ')
#
# DRY: Don't Repeat Yourself  不要重复自己
#
while True:
    yn = input('Continue(y/n)? ')
    if yn in ['n', 'N']:
        break
    print('running...')

