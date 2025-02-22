def files():
    f = open('test.txt')
    print(f.read())
    f.seek(0)
    print(f.readlines())
    for line in open('test.txt'):
        print(line)


if __name__ == "__main__":
    files()
