# 异常处理：把有可能发生异常的语句，放到try里执行，发生异常跳转到异常处理代码
# 把不发生异学点才执行的语句放到else中。不管是否发生异常都要执行的语句，放到
# finally中
try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('Invalid input')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:
    print(result)
finally:
    print('Done')
