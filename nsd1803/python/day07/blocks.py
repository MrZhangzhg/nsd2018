def block(fobj):
    content = []
    counter = 0
    for line in fobj:
        content.append(line)
        counter += 1
        if counter == 10:
            yield content
            content = []
            counter = 0

    if content:
        yield content


if __name__ == '__main__':
    with open('/etc/passwd') as fobj:
        for lines in block(fobj):
            print(lines)
            print()

