if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6, 7]  # extra 7 will be ignored
    zipped_list = list(zip(list1, list2))

    print(zipped_list)

    for pair in zip(list1, list2):
        print(max(pair))
    print(list(map(lambda pair: max(pair), zip(list1, list2))))
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    zipped_dict = list(zip(d1, d2))
    print(zipped_dict)
    zipped_values= list(zip(d1.values(), d2.values()))
    print(zipped_values)
