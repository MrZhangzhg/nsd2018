from random import randint, choice

def exam():
    '出题，要求用户作答，答错三次，给出正确答案'
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)   # 降序排列
    op = choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!')
    else:
        print('Wrong Answer!')


def main():
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            break

if __name__ == '__main__':
    main()
