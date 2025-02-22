def main2():
    l = [1, 2, 3, 4, 5]
    for num in l:
        if num % 2 == 0:
            print('Even number: {x}'.format(x=num))


def main1():
    s = "This is a string"
    for ch in s:
        print(ch)
    tup = (1, 2, 3)
    for t in tup:
        print(t)


def main3():
    l = [(1, 2), (3, 4), (5, 6)]
    for t in l:
        print(t)
    print("-----------")

    for (t1, t2) in l:
        print(t1)
        print(t2)


def main():
    d = {"k1": 1, "k2": 2, "k3": 3};
    for item in d:
        print(item)
    for (k,v) in d.items():
        print(k,v)


if __name__ == "__main__":
    main()
