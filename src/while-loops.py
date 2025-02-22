def main2():
    x = 0
    while x < 10:
        print("x:%s is less than 10" % x)
        x = x + 1


def main1():
    x = 0
    while x < 10:
        print("x:%s is less than 10" % x)
        x = x + 1
    else:
        print("All done")


def main():
    x = 0
    while x < 10:
        print("x:%s is less than 10" % x)
        x = x + 1
        if x == 3:
            print("X is 3")
            break
        else:
            print("Continuing")
            continue

    else:
        print("All done")


if __name__ == "__main__":
    main();
