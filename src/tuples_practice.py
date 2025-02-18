def main():
    t = (1, 2, 3, 4)
    print(len(t))
    print(t[-1])
    # returns index
    print(t.index(2))
    print(t.count(5))


if __name__ == "__main__":
    # tuple is immutable
    main();
