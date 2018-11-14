from random import randint, choice

def exam():
    '出题，要求用户作答，答错三次，给出正确答案'
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)   # 降序排列
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            continue

        if answer == result:
            print('Very Good!')
            break
        print('Wrong Answer!')
        counter += 1
    else:
        print('%s%s' % (prompt, result))


def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye-bye')
            yn = 'n'

        if yn in 'nN':
            break

if __name__ == '__main__':
    main()
