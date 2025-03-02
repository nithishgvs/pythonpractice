def test_dict():
    dict = {x: x * x for x in range(10)}
    print(dict)

    dict1 = {k: v * v for k, v in zip(['a', 'b'], range(2))}
    print(dict1)
    print(dict1.values())
    print(dict1.keys())
