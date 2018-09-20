# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
# except ValueError:
#     print('无效的数字')
# except ZeroDivisionError:
#     print('无效的数字')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')
################################
try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError):
    print('无效的数字')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
else:   # 异常不发生才会执行的语句
    print(result)
finally:   # 不管异常是否发生，都会执行
    print('Done')
# try-except 和 try-finally 用得较多




