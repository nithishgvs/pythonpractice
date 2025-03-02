s = 'This is a global variable'


def hello1(name="Sai") -> str:
    return 'Hello ' + name


def hello(name="Sai") -> str:
    def greet():
        print("\n Inside greet() function")

    def welcome():
        print("\n Inside welcome() function")

    if name == 'Sai':
        return greet
    else:
        return welcome
    print(" Inside hello() function")


if __name__ == "__main__":
    print(globals()['s'])
    print(hello())
    greet = hello()
    del hello
    print(greet)


def test_hello():
    print(hello()())  # returns greet function and use () to execute the function
