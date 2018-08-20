try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('输入错误')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:
    print(result)  # 不发生异常才执行的代码
finally:
    print('Done')  # 不管异常是否发生都要执行的代码

# 不是必须把所有的语句写全，常用的有try-except和try-finally组合


