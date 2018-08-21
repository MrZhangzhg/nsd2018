def add(x, y):
    print(x + y)

def get_info(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    nums = [10, 5]
    add(nums[0], nums[1])
    add(*nums)  # 表示将列表拆开再传参

    get_info(age=23, name='alice')
    user = {'name': 'alice', 'age': 18}
    get_info(**user)  # 表示将字拆成key=val的形式再传参
