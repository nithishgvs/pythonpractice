x = 50


def global_practice():
    global x
    print("X is global value is %s" % x)
    x = 2
    print("X is global changed value is %s" % x)


if __name__ == "__main__":
    print("Value of x is %s" % x)
    global_practice()
    print("Value of x is %s" % x)
