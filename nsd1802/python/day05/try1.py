try:
    n = int(input("number: "))
    result = 100 / n
    print(result)
except ValueError:
    print('invalid number')
except ZeroDivisionError:
    print('0 not allowed')
except KeyboardInterrupt:
    print('Bye-bye')
except EOFError:
    print('Bye-bye')

print('Done')
