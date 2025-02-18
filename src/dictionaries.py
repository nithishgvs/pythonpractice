def main():
    my_dict = {1: 2, "key": "value"}
    print(my_dict)
    print(my_dict[1])
    print(my_dict['key'])
    print(my_dict['key'].upper())
    print(my_dict['key'][::-1])
    print(my_dict.__contains__('Key'))
    d = {}
    d['animal'] = 'dog'
    d[5] = 555
    print(d)
    d = {'key1': {'nestedKey': 'nestedvalue'}}
    print(d['key1'])
    print(d['key1']['nestedKey'])


def main2():
    d = {}
    d['key1'] = 1
    d['key2'] = 2
    d['key3'] = 3
    print(d.pop('key1'))
    print(d)


if __name__ == "__main__":
    main2();
