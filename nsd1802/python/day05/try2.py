try:
    n = int(input("number: "))
    result = 100 / n
except (ValueError, ZeroDivisionError):
    print('invalid number')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:
    print(result)  # 异常不发生时才执行else子句
finally:
    print('Done')  # 不管异常是否发生都必须执行的语句

# 常用形式有try-except和try-finally
