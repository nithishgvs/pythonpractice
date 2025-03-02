from collections import Counter
from collections import defaultdict


def counter_test():
    list1 = [1, 2, 3, 4, 5, 6, 2, 4, 3, 5, 7, 2, 1]
    print(Counter(list1))
    string = 'ddttertyfdgdfghgrheghjertgerhgthjerhth'
    print(Counter(string))


def defaultdict_test():
    d1 = {'k1': 1}
    print(d1['k1'])
    # print(d1['k2'])  # error
    d = defaultdict(object)
    print(d['k'])  # returns object <object object at 0x10210ce80>

    d2 = defaultdict(lambda: 'default value')
    print(d2['k'])  # returns default value


def test_counter():
    counter_test()
    sentence = "Whats the most common words in the sentence most common"
    counter = Counter(sentence.split(" "))
    print(counter)
    print(counter.most_common(2))  # 2 most common words


def test_defaultdict():
    defaultdict_test()
