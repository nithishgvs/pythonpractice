from collections import OrderedDict


def ordered_dict():
    ordered_dict = OrderedDict()
    ordered_dict['z'] = 1
    ordered_dict['y'] = 2
    ordered_dict['a'] = 4
    ordered_dict['b'] = 44
    ordered_dict['c'] = 11
    for k, v in ordered_dict.items():
        print(k, v)


def test_ord():
    ordered_dict()