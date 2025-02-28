from functools import reduce

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(reduce(lambda x, y: x + y, list))
