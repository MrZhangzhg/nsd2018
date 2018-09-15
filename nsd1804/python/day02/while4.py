# yn = input('Continue(y/n)? ')
# while yn not in ['n', 'N']:
#     print('working...')
#     yn = input('Continue(y/n)? ')
# DRY: Don't Repeat Yourself
##################################
while True:
    yn = input('Continue(y/n)? ')
    if yn in ['n', 'N']:
        break
    print('working...')


