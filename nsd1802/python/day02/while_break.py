# yn = input('Continue(y/n): ')
#
# while yn not in 'nN':
#     print('running...')
#     yn = input('Continue(y/n): ')
# python DRY原则: Don't Repeat Yourself

while True:
    yn = input('Continue(y/n): ')
    if yn in ['n', 'N']:
        break
    print('running...')
#############################################
sum100 = 0
counter = 0

while counter < 100:
    counter += 1
    # if counter % 2:
    if counter % 2 == 1:
        continue
    sum100 += counter

print(sum100)

