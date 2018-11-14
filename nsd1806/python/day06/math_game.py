def exam():
    '出题，要求用户作答，答错三次，给出正确答案'

def main():
    while True:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in ['n', 'N']:
            break

if __name__ == '__main__':
    main()
