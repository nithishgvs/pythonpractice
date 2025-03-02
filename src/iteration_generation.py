def gen_exercise():
    # List comprehension (creates entire list in memory)
    nums_list = [x * x for x in range(5)]
    print(nums_list)  # [0, 1, 4, 9, 16]

    # Generator expression (yields values one by one)
    nums_gen = (x * x for x in range(5))

    print(next(nums_gen))  # 0
    print(next(nums_gen))  # 1
    print(next(nums_gen))  # 4


def test_gen():
    gen_exercise()
